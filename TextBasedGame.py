# Kelly Perez
# Scorched Earth

import time

# Initializing dictionary of rooms.
rooms = {  # Starting room, no items.
    'Spaceship': {'name': 'Spaceship', 'item': [], 'East': 'Mars', 'wayout': 'East and Exit', 'exit': 'The Exit',
                  'desc': 'A high tech spaceship, the last relic of Earth. \n\nThe smell is sterile, with a slight tinge of ozone.'},

    'Mars': {'name': 'Mars', 'item': ['armor'], 'West': 'Spaceship', 'North': 'Venus', 'East': 'Uranus',
             'South': 'Mercury', 'wayout': 'East, North, West, South, and Exit', 'exit': 'The Exit',
             'desc': 'A barren red planet with almost no oxygen. Devoid of any and all life. \n\nGlittering in the sand you see armor, forged by the God of War, Mars himself. \n\nPower radiates from the very fibers weaved into it during its creation. \n\nFrom here you can see Earth, which was once a beautiful blue marble. \n\nEven from here, you can see the glowing magma upon the cracks of its withered surface.'},

    'Venus': {'name': 'Venus', 'item': ['potion'], 'East': 'Titan', 'South': 'Mars', 'wayout': 'South, East, and Exit',
              'exit': 'The Exit',
              'desc': "With an atmosphere so thick you could cut it with a knife, seeing anything is nearly impossible. Clambering about the desolate landscape, your foot hits a tiny bottle. Within this nearly minuscule glass container is a swirling and technicolor elixer. Taking this potion will protect your mind from insanity leashed upon you as you face Cthulhu."},

    # Boss room, no items.
    'Titan': {'name': 'Titan', 'item': [], 'West': 'Venus', 'wayout': 'East and Exit', 'exit': 'The Exit',
              'desc': "The frozen wasteland of this moon is daunting, and horrid on the senses. \n\nWandering about this small rock is Cthulhu, an alien lifeform no one could possibly imagine. \n\nIt's highly advisable to have all six items before coming here. \n\nTemping fate and not obtaining all the items will surely cause your untimely demise."},

    'Mercury': {'name': 'Mercury', 'item': ['mjolnir'], 'East': 'Saturn', 'North': 'Mars',
                'wayout': 'North, East, and Exit', 'exit': 'The Exit',
                'desc': "Scorching hot as this planet is nestled closest to the Sun. The heat is absolutely unbearable. \n\nA flash of light happens so fast, you would have missed it - if the astronomical BOOM didn't accompany it. \n\nYou run towards the direction of the sound and are met with a sight like no other. \n\nThor, the God of Thunder stands before you holding Moljnir, ready to hand you his hammer. \n\nAre you brave enough to accept it? Meh, we'll see."},

    'Saturn': {'name': 'Saturn', 'item': ['terraformer'], 'West': 'Mercury', 'wayout': 'West and Exit',
               'exit': 'The Exit',
               'desc': "Saturn and it's beautiful rings. \n\nThe sight would be pleasant if the atmosphere wasn't actively trying to murder you. \n\nThe gravity on this planet nearly crushes you to your core, hardly able to move and clearly inhospitable. \n\nStruggling against the vapid storms to traverse this desolate landscape, \n\nyou stumble across a terraformer that will aid you on your journey to create a new home for humanity."},

    'Uranus': {'name': 'Uranus', 'item': ['oxidizer'], 'West': 'Mars', 'North': 'Pluto',
               'wayout': 'West, North, and Exit', 'exit': 'The Exit',
               'desc': "A massive pale blue ice giant, icy cold, and unforgiving! \n\nYou float through the ether of this luminous body, pelted by ice chunks, \n\nyou find as if by some cosmic joke a device that turns foul gases into breathable oxygen."},

    'Pluto': {'name': 'Pluto', 'item': ['aquafier'], 'South': 'Uranus', 'wayout': 'South and Exit', 'exit': 'The Exit',
              'desc': "Humanity once said Pluto was no longer a planet, boy were they wrong. \n\nIce-covered and fractured you see what appears to be frozen rivers pelted across the planet's surface, \n\nas if the landscape comes alive all on its own. In the distance, you spot some kind of mythical machine. \n\nUpon closer inspection, you realize this machine creates water, a vital resource to keep yourself alive."},

    'Exit': {'name': 'the Exit', 'item': '', 'wayout': "Game over man - game over"}
}

# Initializing position, directions, and inventory.
position = rooms['Spaceship']
directions = ['North', 'East', 'South', 'West', 'Exit']
inventory = []


def main():
    print(
        'Earth has been scorched from nuclear fallout. In a war, no one could have predicted. \n\nHumanities only escape; a spaceship to seek out the planets and moons within our solar system, searching for a hospitable location to restart society.\n\nThere’s one problem though, something that had never been confirmed before; alien lifeforms. \n\nSearching the planets and moons provide lifelines to assist with survival. Our only downfall would be finding Cthulhu before obtaining all items needed to defeat him and survive thereafter.\n\nEach planet will have a vital element to increase your chances of survival. You’ll need to gain six items in total. \n\nMjolnir hammer of Thor, sanity potions, a terraforming machine, armor blessed by Mars, an oxidizer, and a water purifier. \n\nThe objects you find will assist in vanquishing Cthulhu or help you survive after, but, finding the ancient entity before you obtain all pieces will cause you to meet your unfortunate death.')
    # Initializing time barrier to read story.
    time.sleep(3)


#
def instructions():
    print(
        "\n**********Welcome to Scorched Earth********** \n\n----Instructions----\n\nCollect the 6 items on the planets to defeat Chuthulu and win. If you meet Cthulhu before obtaining all 6 items, you DIE a painful death. \n\nTo move type: North, South, West, East, or Exit to quit the game. \n\nTo aquire the item on the planet, type 'get item name'\n\n")
    # Initializing time barrier to read instructions.
    time.sleep(3)


# Displays current room, room description, items in the room, inventory and possible exits.
def room_info(position, inventory, rooms):
    print(f'You are on {position["name"]}')
    print(position['desc'])
    print(f'Your current inventory: {inventory}\n')
    if position['item']:
        # If there's a way to get this to f-string, please let me know. I couldn't figure it out.
        print('Laying on the floor, you see: {}'.format(', '.join(position['item'])))
    print(f'Your exits are: {position["wayout"]}')


# Calling Story line.
main()
# Calling instructions.
instructions()

# Initializing gaming loop.
while True:

    if position == rooms['Titan'] and len(inventory) > 5:
        print(
            '\n\nYou have obliterated Cthulhu and avoided becoming one of his Faceless! You also collected the items necessary to start a new life on Titan, saving humanity. See you in the next game!')
        break

    elif position == rooms['Titan'] and len(inventory) < 6:
        print(
            '\n\nYou have reached Cthulhu without obtaining all the items! You die a slow and painful death!\nCthulhu has morphed you into one of his many faceless! Try again.')
        break

    # Display room and all important information.
    room_info(position, inventory, rooms)

    # Get user input.
    user_input = input('State your coordinates: ').capitalize().strip()

    # Exit game.
    if user_input.lower() == 'exit':
        print('\nYou just let Cthulhu win! You have exited the game. See you next time.')
        break

    if user_input in directions:
        # Moves player in direction if valid.
        if user_input in position:
            position = rooms[position[user_input]]

        # Error for going in a direction that doesn't exist.
        else:
            print('\nYou walk yourself into a wall. Good job! You remain in your current room:\n')
    # Noticed putting in empty input didn't do anything, so I added this.
    elif not user_input:
        print('------Cannot divide by zero, try again!------')

    # Getting item and removing it from the planet once it's in inventory.
    elif user_input.lower().split()[0] == 'get':
        item = user_input.lower().split()[1]

        if item in position['item']:
            position['item'].remove(item)
            inventory.append(item)
    # Invalid input.
    else:
        print('Input does NOT compute! Try again!')

