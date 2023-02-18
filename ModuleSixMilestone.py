# Kelly Perez
# Move Between Rooms Game

# Room initialization.
rooms = {'Great Hall': {'name': 'Great Hall', 'south': 'Bedroom', 'text': 'You are in the Great Hall.', 'exit': 'Exit','wayout': 'South or Exit'},
    'Bedroom': {'name': 'the bedroom', 'east': 'Cellar', 'north': 'Great Hall', 'text': 'You are in the Bedroom.', 'exit': 'Exit','wayout': 'East, North, Exit'},
    'Cellar': {'name': 'the Cellar', 'west': 'Bedroom', 'text': 'You are in the Cellar.', 'exit': 'Exit', 'wayout': 'West and Exit'},
    'Exit': {'name': 'The Exit', 'text': "You have made it to the Exit!", 'wayout': "none"}
    }
# Initializing possible inputs.
directions = ['north', 'south', 'east', 'west', 'exit']

# Initializing starting position.
position = rooms['Great Hall']

# Define main to print out current room and exits.
def main():
    print('{}.'.format(position['name']))
    print('Your exits are: {}.'.format(position['wayout']))

# Game loop.
while True:
    if position['name'] == 'The Exit':
        print('Congratulations! You actually just walked into the dragons mouth! Good game! See you next time.')
        break
    # Display current location and exits.
    main()
    # Get user input.
    user_input = input('\nDo you know the way?')
    # Movement.
    if user_input.lower() in directions:
        if user_input.lower() in position:
            position = rooms[position[user_input.lower()]]
        else:
            # Invalid directions for given room.
            print('You walk yourself into a brick wall. Good job! You remain in your current room:')
    # Invalid commands.
    else:
        print('Invalid input')