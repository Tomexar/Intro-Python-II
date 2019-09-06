# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        if(self.items ==[]):
            return f'You entered the {self.name}. \n {self.description}'
        else:
            for i in self.items:
                return f'You entered the {self.name}. \n {self.description} \n On the ground is a "{i.name}"'