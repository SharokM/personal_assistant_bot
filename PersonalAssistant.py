class PersonalAssistant:
  def __init__(self, todos, birthdays, contacts):
    self.todos = todos 
    self.birthdays = birthdays
    self.contacts = contacts

# add todo 
  def add_todo(self, new_item):
    self.todos.append(new_item)

# remove todo
  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      index = self.todos.index(todo_item)
      self.todos.pop(index)
      return f"\n{todo_item} was successfully removed from to-do list."
    else:
      return "Item not found in to-do list."

# get todo list 
  def get_todos(self):
    return self.todos

# get birthday list 
  def get_birthdays(self):
    return self.birthdays

# get contact list 
  def get_contacts(self):
    return self.contacts

# get specific birthday 
  def get_birthday(self, name):
    if name in self.birthdays:
      return f"\n{name}'s birthday is on {self.birthdays[name]}"
    else:
      return f"\nNo birthday found with {name}! Please add it."

# add new birthday 
  def add_birthday(self, name, date):
    if name in self.birthdays:
      return f"\n{name}'s details have already been added."
    else:
      self.birthdays[name] = date
      return f"\n{name}'s birthday was successfully added."

# remove birthday 
  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      return f"\n{name}'s birthday was successfully removed."
    else:
      return "Error occurred while removing the birthday, please try again later."

# get contact 
  def get_contact(self, name):
    if name in self.contacts:
      return f"\n{name} is a {self.contacts[name]}"
    else:
      return 'Not Found'

# add new contact 
  def add_contact(self, name, title):
    if name in self.contacts:
      return f"\n{name}'s details have already been added."
    else:
      self.contacts[name] = title
      return f"\n{name}'s contact was successfully added"


# remove contact 
  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name)
      return f"\n{name}'s contact was successfully removed."
    else:
      return "Error occurred while removing the birthday, please try again later."

