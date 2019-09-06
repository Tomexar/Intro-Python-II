from room import Room
from player import Player
from items import Item
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


item = {
    'sword': Item('sword', 'this is a sword'),
    'lantern': Item('lantern', 'this is a lantern'),
    'armor': Item('Armor',  'a set of chainmail armor')
    }

room['foyer'].items = [item['lantern']]

room['overlook'].items = [item['sword']]

room['treasure'].items = [item['armor']]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def newPlayer():
    return Player(name = 'tommy', currentRoom = room['outside'])

player = newPlayer()

def checkMove(player):
    print(f'{player.currentRoom}')

    moves = player.move()

    command = ''
    action = ''

    while command not in moves.keys():
        command = input("Where do you want to go ")

        if command == 'Q':
            print('Exiting Game')
            sys.exit()
        
        if command == 'B':
            print('This is the backpack')

        try:
            if command =='N':
                player.currentRoom = player.currentRoom.n_to
            if command =='S':
                player.currentRoom = player.currentRoom.s_to
            if command =='E':
                player.currentRoom = player.currentRoom.e_to
            if command =='W':
                player.currentRoom = player.currentRoom.w_to
        except AttributeError:
            print('this is a dead end')
        return command

player_move = None

while player_move is not 'Q':
    move_player = checkMove(player)
            