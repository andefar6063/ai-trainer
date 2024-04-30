import os
import json
from colorama import Fore

def clear_screen():
    """Clear the terminal screen."""
    os.system("clear")

def get_json_data():
    """Get json data from the trainer file."""
    with open("./trainers.json", "r") as file:
        json_data = json.load(file)
    return json_data

def show_json_data():
    """Show json data from the trainer file."""
    for trainer_key, trainer_info in get_json_data().items():
        print(f"Command for {trainer_info['name']}: {trainer_info['command_key']}\n")

def console_log(data, color=None):
    """Print using colorama for colors"""
    if color is "red":
        print(Fore.RED, data)
    elif color is "green":
        print(Fore.GREEN, data)
    elif color is "blue":
        print(Fore.BLUE, data)
    else:
        print(Fore.RESET, data)