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
        try:
            client.add_message_to_thread(input("Type here: "))
            client.run_assistant()
        except Exception as e:
            console_log(f"Error while processing your message: {str(e)}", "red")
            continue
        console_log("\n")
        try:
            choice = input("Would you like to close the thread: ['y' or 'n'] ").strip().lower()
            if choice not in ['y', 'n']:
                raise ValueError("Invalid input. Please type 'y' or 'n'.")
            if choice == "y":
                message_active = False
        except ValueError as ve:
            console_log(str(ve), "yellow")
            continue

    user_return = input("Return to the main page: ['y' or 'n'] ").lower()

    if user_return == "y":
        clear_screen()
        return
    else:
        clear_screen()
        question()