from utils import clear_screen, show_json_data, console_log
from client import AIClient
        
def question():
    print("Here are all the teachers you can use!\n")
    show_json_data()

    client = AIClient()
    client.get_teacher("Choose your teacher: ")
    client.get_question("What is your question? ")
    result = client.client_completion()
    
    print(result)
    
    user_return = input("Return to the main page: ['y' or 'n'] ").lower()

    if user_return == "y":
        clear_screen()
        return
    else:
        clear_screen()
        question()

if __name__ == "__main__":
    question()

