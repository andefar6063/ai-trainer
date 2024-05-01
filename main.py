import asyncio

from utils import clear_screen, console_log
from pages.help import help
from pages.chat import question
from pages.new import person

page_data = {
    "help": help,
    "start": question,
    "new": person
}

def get_user_input():
    console_log("\nHello and welcome to the AI-Trainer!\n")
    return input("What are you interested in doing? ['start', 'help', 'new'] : ")

async def execute_action(action):
    if action in page_data:
        clear_screen()
        if asyncio.iscoroutinefunction(page_data[action]):
            await page_data[action]()
        else:
            page_data[action]()
    else:
        console_log("I did not understand that... Please retry", "red")

async def main():
    clear_screen()
    while True:
        user_input = get_user_input()
        await execute_action(user_input)

if __name__ == "__main__":
    asyncio.run(main())