class PersonalAssistant:

  def __init__(self):
    self.contacts = {
        'Ann': 'Marketing Coordinator',
        'Chelsea': 'Software Developer',
        'Nichole': 'Sales Representative',
        'Max': 'Technical Writer'
    }
    self.todos = []

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self,todo_item):
    if todo_item in self.todos:
      index = self.todos.index(todo_item)
      self.todos.pop(index)
    else:
      print("Item not found in to-do list.")

  
  def get_todos(self):
    return self.todos
  
  def get_birthday(self, name):
    if (name.lower() == "robin"):
        print("Robin's birthday in July 4th. Remember to buy a gift!")
    elif (name.lower() == "alice"):
        print("Alice's birthday is on December 12th. Don't forget to send her a card!")
    elif (name.lower() == "john"):
        print("John's birthday is on March 22nd. Maybe plan a surprise party!")
    elif (name.lower() == "emma"):
        print("Emma's birthday is on September 15th. Consider getting her flowers & chocolates!")
    elif (name.lower() == "Kwesi"):
        print("Kwesi's birthday is on November 30th. Get him a replacement for the lunch you ate out of the work fridge?")
    else:
        print("Sorry, I don't have information on that person's birthday. Please try adding more people to the list, or search another name.")




  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return 'Not Found'


assistant = PersonalAssistant()
assistant.add_todo("Finish the react project")
assistant.add_todo("Email the project report")
assistant.add_todo("Scrum Meeting at 10 AM")
assistant.remove_todo("Email the project report")
assistant.add_todo("Clear schedule for team lunch on Friday")
print(assistant.get_contact("bob"))
print(assistant.get_contact("Wilfred II"))
print(assistant.get_todos())
print(assistant.get_birthday("Robin"))





