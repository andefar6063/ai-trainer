from utils import clear_screen, console_log

def help():
    print("""Here are all the commands you can use!\n
          +-----------------------------------------------------------------------------------+
          | 'new-data': Sends you to the create teacher page.                                 |
          |                                                                                   |
          | 'help': Shows the page you are seeing right now.                                  |    
          |                                                                                   |
          | 'question': Sends you to the question page, where you are able to ask a question. |
          +-----------------------------------------------------------------------------------+""")
    user_input = input("Return to the main page: ['y' or 'n'] ").lower()
    while user_input not in ["y", "n"]:
        clear_screen()
        help()
    if user_input == "y":
        clear_screen()
        return
    clear_screen()
    help()
    
    