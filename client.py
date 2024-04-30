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
                    print(self.trainer)
                    return
            console_log("Invalid input. Please try again.", "red")

    def create_thread(self):
        self.thread = self.client.beta.threads.create()

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
            
            def on_tool_call_delta(self, delta, snapshot):
                if delta.type == 'code_interpreter':
                    if delta.code_interpreter.input:
                        print(delta.code_interpreter.input, end="", flush=True)
                if delta.code_interpreter.outputs:
                    print(f"\n\noutput >", flush=True)
                    for output in delta.code_interpreter.outputs:
                        if output.type == "logs":
                            print(f"\n{output.logs}", flush=True)

        with self.client.beta.threads.runs.stream(
                thread_id=self.thread.id,
                assistant_id=self.json_data[self.trainer]["key"],
                instructions="Please address the user as User.",
                event_handler=EventHandler(),
        ) as stream:
            stream.until_done()

    """
    async def run_assistant(self):
        try:
            run = self.client.beta.threads.runs.create_and_poll(
                thread_id=self.thread.id,
                assistant_id=self.json_data[self.trainer]["key"],
                instructions="Please address the user as User."
            )
        except Exception as e:
            print(e)
            return

        while run.status != 'completed':
            await asyncio.sleep(1)  # Adjust sleep time as needed
            run.poll()  # Poll the run status

        if run.status == 'completed': 
            messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
            for message in messages:
                print(message.content)
        else:
            print(run.status)"""




    