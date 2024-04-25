import asyncio

from utils import clear_screen, console_log
from pages.help import help
from pages.question import question
from pages.new_data import person

page_data = {
    "help": help,
    "question": question,
    "new-person": person
}

def get_user_input():
    print("\nHello and welcome to the AI-Teacher!\n")
    return input("What are you interested in doing? ['question', 'help', 'new-person'] : ")

async def execute_action(action):
    if action in page_data:
        clear_screen()
        if asyncio.iscoroutinefunction(page_data[action]):
            await page_data[action]()
        else:
            page_data[action]()
    else:
        print("I did not understand that... Please retry")

async def main():
    clear_screen()
    while True:
        user_input = get_user_input()
        await execute_action(user_input)

if __name__ == "__main__":
    asyncio.run(main())