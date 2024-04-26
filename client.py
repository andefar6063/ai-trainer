import os
from openai import OpenAI
from utils import get_json_data, console_log

class AIClient():
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
        self.json_data = get_json_data()
        self.trainer = None
        self.question = None

    def get_trainer(self, prompt):
        while True:
            user_input = input(prompt).lower()
            for key, value in self.json_data.items():
                if user_input == key.lower() or user_input == value["command_key"].lower():
                    self.trainer = key
                    return
            console_log("Invalid input. Please try again.", "red")

    def get_question(self, prompt):
        self.question = input(prompt).lower()

    def client_completion(self):
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4",
                temperature=0,
                max_tokens=100,
                messages=[
                    {"role": "system", "content": self.json_data[self.trainer]["content"]},
                    {"role": "user", "content": self.question}
                ]
            )
            return completion.choices[0].message.content
        except:
            return "An error occurred while processing your request."