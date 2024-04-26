from utils import clear_screen, show_json_data, console_log
from client import AIClient
        
def question():
    console_log("Here are all the trainers you can use!\n")
    show_json_data()

    client = AIClient()
    client.get_trainer("Choose your trainer: ")
    client.get_question("What is your question? ")
    result = client.client_completion()
    
    console_log("\n")
    if result != "An error occurred while processing your request.":
        console_log(result, "blue")
    else:
        console_log(result, "red")
    console_log("\n")
    user_return = input("Return to the main page: ['y' or 'n'] ").lower()

    if user_return == "y":
        clear_screen()
        return
    else:
        clear_screen()
        question()

if __name__ == "__main__":
    question()

