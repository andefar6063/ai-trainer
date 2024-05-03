from utils import clear_screen, console_log

def help():
    print("""Here are all the commands you can use!\n
          +-----------------------------------------------------------------------------------+
          | 'new': Sends you to the create teacher page.                                 |
          |                                                                                   |
          | 'help': Shows the page you are seeing right now.                                  |    
          |                                                                                   |
          | 'start': Sends you to the question page, where you are able to ask a question. |
          +-----------------------------------------------------------------------------------+""")
    while True:
        try:
            user_input = input("Return to the main page: ['y' or 'n'] ").lower().strip()
            if user_input not in ["y", "n"]:
                raise ValueError("Please enter 'y' or 'n' only.")
            if user_input == "y":
                clear_screen()
                break
        except ValueError as ve:
            console_log(str(ve), "yellow")
            continue
        except Exception as e:
            console_log(f"Unexpected error: {str(e)}", "red")
            continue
    