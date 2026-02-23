# Course: IT-140-H7801
# Assignment: Create a text adventure
# Date: 2023/10/11
# Name: Rickey Partridge
# Description: Project 2

# Introduction to show player game instructions
def show_instructions():
    print('Welcome to a A Space Adventure\n')
    print('You wake up alone on a space station. The ship is slowly drifting towards the planet below.'
          '\nCollect the six items and enter the Bridge to correct course. Good luck!')
    print('Movement: North, South, East, West')
    print('Add to Inventory: get item')
    print('Type quit to exit game.\n')


# Show player status function. Called in game loop
def show_status(group):
    print('-' * 30)  #
    print('You are in the {}'.format(current_room))
    print('Your current inventory: {}\n'.format(Inventory))
    if group['item']:
        print('Item in room: {}'.format(''.join(group['item'])))
        print('')


# Start game function called to inform player the game has started.


def game_start():
    # print game start
    print('***GAME START***\n')


# Create Inventory empty list
Inventory = []

# define directions
directions = ['North', 'South', 'East', 'West']
# Set current room as dining hall
current_room = 'Dining Hall'
# set starting room as current room
starting_room = current_room

# define item list
Item = ['Key card', 'Password', 'Wrench', 'Air lock manual', 'Anti-viral', 'Hex bolts']


# Define main
def main():
    # define global variable for current room. Create dictionary of rooms, directions, and items.
    global current_room
    rooms = {'Dining Hall': {'name': 'the Dining Hall', 'North': 'Quarters', 'South': 'Engine Room', 'West': 'Library',
                             'item': 'none'},
             'Library': {'name': 'the Library', 'East': 'Dining Hall', 'South': 'Gym', 'item': 'Key card'},
             'Gym': {'name': 'the Gym', 'North': 'Library', 'item': 'Hex bolts'},
             'Quarters': {'name': 'Crew Sleeping Quarters', 'South': 'Dining Hall', 'item': 'Password'},
             'Engine Room': {'name': 'the Engine Room', 'North': 'Dining Hall', 'East': 'Lab', 'item': 'Wrench'},
             'Lab': {'name': 'the Laboratory', 'West': 'Engine Room', 'North': 'Med Bay', 'item': 'Anti-viral'},
             'Med Bay': {'name': 'the Med Bay', 'South': 'Lab', 'East': 'Bridge', 'item': 'Air lock manual'},
             'Bridge': {'name': 'the Bridge', 'West': 'Med Bay', 'item': 'none', 'Boss': 'Captain Riggs'}

             }

    # Call and show game instructions
    show_instructions()
    # Call Start game
    game_start()

    # Start gameplay loop
    while True:
        show_status(rooms[current_room])  # Call show status function

        # Get case-insensitive user input using .title
        command = input('Enter your move: ').title()

        # Win Condition IF all items are collected before entering the Bridge
        if command in directions:
            if command in rooms[current_room]:
                current_room = rooms[current_room][command]
                if rooms[current_room]['name'] == 'the Bridge' and len(Inventory) == 6:
                    print('Congratulations! You have defeated Captain Riggs and saved the ship! You WIN!')
                    break  # End game on WIN

                # Lose Condition IF all items are not collected when entering the Bridge
                elif rooms[current_room]['name'] == 'the Bridge' and len(Inventory) != 6:
                    print('You failed to collect all 6 items. Captain Riggs attacks!\n'
                          'As everything fades to black, you hear the captain laughing.\n'
                          'GAME OVER You lose!')
                    break  # End game on LOSE
            # Invalid direction message
            else:
                print('\nThere is a wall in that direction. Please try again.')

        # get items and append to inventory
        elif command == 'Get Item':
            if rooms[current_room]['item'] != 'none':
                Inventory.append(rooms[current_room]['item'])

                print("You picked up : ", rooms[current_room]['item'])  # notify of item pick-up
                print(Inventory)
                rooms[current_room]['item'] = 'none'
            else:
                print("No items to collect in this room")  # response if item already collected

        # allow player to quit game
        elif command == 'quit':
            print('Game over. Thanks for playing!')
            break
        # message for invalid input
        else:
            print('Invalid input')


main()
