import json

from utils import clear_screen, console_log, show_json_data, get_json_data, create_assistant

def person():
    console_log("Here are all the trainers you have at the moment!\n")
    show_json_data()

    while True:
        userName = input("Please type NAME: ").strip()
        userInstructions = input("Please type INSTRUCTIONS (press ENTER to skip): ").strip() or None
        
        if userName:
            break
        else:
            console_log("NAME is required. Please try again.", "red")
            clear_screen()

    try:
        person_key = create_assistant(userName, userInstructions)
        if person_key is None:
            raise Exception("Assistant creation failed. Please check the details and try again.")

        command_key = [i[0].upper() for i in userName.split()]
        json_data = get_json_data()
        person_id = int(list(json_data.keys())[-1]) + 1 if json_data else 1
        
        person_dict = {
            str(person_id): {
                "name": userName,
                "command_key": "".join(command_key),
                "key": person_key
            }
        }

        with open("./trainers.json", "w") as file:
            json.dump({**json_data, **person_dict}, file, indent=4)
        
    except Exception as e:
        console_log(f"Error occurred: {e}", "red")
        if input("Would you like to retry? ['y' or 'n'] ") == "y":
            clear_screen()
            person()   
        else:
            pass
