import json
from PersonalAssistant import PersonalAssistant


with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays:
    todo_list = json.load(todos)
    birthday_list = json.load(birthdays)
    assistant = PersonalAssistant(todo_list, birthday_list)

done = False

while not done:
    user_command = input("""
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list
    ***** Birthdays *****
    4: Get Birthdays
    5: Add Birthday
    6: Remove Birthday

    Select a number or type 'Exit' to quit: 
    
    """)
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todos()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list")
        print(f"\n {assistant.get_todos()}")
    # Get Birthdays
    elif user_command == "4":
        print("\nYour birthday list: \n")
        for name in assistant.get_birthdays():
            print(name)
        user_name = input("\nEnter the name to get the birthday: ")  
        print(assistant.get_birthday(user_name))
    # Add Birthdays
    elif user_command == "5": 
        name_to_add = input("\nEnter the name of the person's name: ")
        birthday = input("Their birthday e.g. 01/01/1901: ")
        print(assistant.add_birthday(name_to_add, birthday))
        print(f"\n{name_to_add}'s birthday has been added!")   
       # Remove Birthdays
    elif user_command == "6":
        print("\nRemove a birthday")
        for name in assistant.get_birthdays():
            print(name)
        remove_name = input("\nEnter the name to be deleted: ") 
        print(f"\n{assistant.remove_birthday(remove_name)}")

    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")



with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays:
    json.dump(assistant.get_birthdays(), write_birthdays)
    json.dump(assistant.get_todos(), write_todos)

