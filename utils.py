import os
import json

def clear_screen():
    """Clear the terminal screen."""
    os.system("clear")

def get_json_data():
    with open("./teachers.json", "r") as file:
        """Get json data from the teacher file."""
        json_data = json.load(file)
    return json_data

def show_json_data():
    for teacher_key, teacher_info in get_json_data().items():
        print(f"Command for {teacher_info['name']}: {teacher_info['command_key']}\n")

def console_log(data, color):
    pass

