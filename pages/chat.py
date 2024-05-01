from client import AIClient
from utils import clear_screen, show_json_data, console_log

        
async def question():
    console_log("Here are all the trainers you can use!\n")
    show_json_data()

    client = AIClient()
    client.get_trainer("Choose your trainer: ")
    client.create_thread()
    message_active = True
    while message_active:
        console_log("\n")
        client.add_message_to_thread(input("Type here: "))
        client.run_assistant()
        console_log("\n")
        if input("Would you like to close the thread: ['y' or 'n'] ") == "y":
            message_active = False
        else:
            continue

    user_return = input("Return to the main page: ['y' or 'n'] ").lower()

    if user_return == "y":
        clear_screen()
        return
    else:
        clear_screen()
        question()