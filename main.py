class PersonalAssistant:

  def __init__(self):
    self.contacts = {
        'Ann': 'Marketing Coordinator',
        'Chelsea': 'Software Developer',
        'Nichole': 'Sales Representative',
        'Max': 'Technical Writer'
    }
    self.todos = []

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return 'Not Found'


assistant = PersonalAssistant()
print(assistant.get_contact("bob"))
