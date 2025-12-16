class PersonalAssistant:
  def __init__(self, todos, birthdays):
    
    self.todos = todos 
    self.birthdays = birthdays

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      index = self.todos.index(todo_item)
      self.todos.pop(index)
      return f"\n{todo_item} was successfully removed from to-do list."
    else:
      return "Item not found in to-do list."

  def get_todos(self):
    return self.todos

  def get_birthdays(self):
    return self.birthdays

  def get_birthday(self, name):
    if name in self.birthdays:
      return f"\n{name}'s birthday is on {self.birthdays[name]}"
    else:
      return f"\nNo birthday found with {name}! Please add it."

  def add_birthday(self, name, date):
    if name in self.birthdays:
      return f"\n{name}'s details have already been added."
    else:
      self.birthdays[name] = date
      return f"\n{name}'s birthday was successfully added."

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      return f"\n{name}'s birthday was successfully removed."
    else:
      return "Error occurred while removing the birthday, please try again later."


  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return 'Not Found'



