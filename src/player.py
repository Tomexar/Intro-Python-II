# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []

    def move(self):
        direction = {}

        if hasattr(self.currentRoom, 'n_to'):
            direction['N'] = self.currentRoom.n_to.name
        if hasattr(self.currentRoom, 's_to'):
            direction['S'] = self.currentRoom.s_to.name
        if hasattr(self.currentRoom, 'e_to'):
            direction['E'] = self.currentRoom.e_to.name
        if hasattr(self.currentRoom, 'w_to'):
            direction['W'] = self.currentRoom.w_to.name
        return direction

    def __str__(self):
        return (f'{self.currentRoom}')

def held_items(self):
    return','.join(str(item) for item in self.items)      
        
