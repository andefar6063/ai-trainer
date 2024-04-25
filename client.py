import os
from openai import OpenAI
from utils import get_json_data, console_log

class AIClient():
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
        self.json_data = get_json_data()
        self.teacher = None
        self.question = None

    def get_teacher(self, prompt):
        while True:
            user_input = input(prompt).lower()
            for key, value in self.json_data.items():
                if user_input == key.lower() or user_input == value["command_key"].lower():
                    self.teacher = key
                    return
            print("Invalid input. Please try again.")

    def get_question(self, prompt):
        self.question = input(prompt).lower()

    def client_completion(self):
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4",
                temperature=0,
                messages=[
                    {"role": "system", "content": self.json_data[self.teacher]["content"]},
                    {"role": "user", "content": self.question}
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return "An error occurred while processing your request."