import os
from typing_extensions import override
from openai import OpenAI, AssistantEventHandler
from utils import get_json_data, console_log

class AIClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.json_data = get_json_data()
        self.trainer = None
        self.thread = None

    def get_trainer(self, prompt):
        while True:
            user_input = input(prompt).lower()
            for key, value in self.json_data.items():
                if user_input == key.lower() or user_input == value["command_key"].lower():
                    self.trainer = key
                    console_log(f"Selected trainer: {self.trainer}", "green")
                    #console_log(f"Trainer key: {self.json_data[self.trainer]["key"]}", "green")
                    return
            console_log("Invalid input. Please try again.", "red")

    def create_thread(self):
        self.thread = self.client.beta.threads.create()
        if "initial_prompt" in self.json_data[self.trainer]:
            self.add_message_to_thread(self.json_data[self.trainer]["initial_prompt"])

    def add_message_to_thread(self, content):
        self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=content,
        )

    def run_assistant(self):
        class EventHandler(AssistantEventHandler):    
            @override
            def on_text_created(self, text) -> None:
                print(f"\nassistant > ", end="", flush=True)
                
            @override
            def on_text_delta(self, delta, snapshot):
                print(delta.value, end="", flush=True)
                
            def on_tool_call_created(self, tool_call):
                print(f"\nassistant > {tool_call.type}\n", flush=True)

        with self.client.beta.threads.runs.stream(
                thread_id=self.thread.id,
                assistant_id=self.json_data[self.trainer]["key"],
                event_handler=EventHandler(),
        ) as stream:
            stream.until_done()




    