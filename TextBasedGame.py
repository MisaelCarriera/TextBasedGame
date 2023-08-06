# Misael Carriera

#commands available for each room
rooms = {
    'Freight Train' : {'Left' : 'Egypt', 'item' : 'No Items'},
    'Egypt' : {'Up' : 'Prehistoric Era','Right' : 'Freight Train', 'item' : 'Gold'},
    'Prehistoric Era' : {'Left' : 'Conductors Room', 'Right' : '1800s', 'Up' : '200 B.C','Down' : 'Egypt', 'item' : 'Dinosaur Egg'},
    'Conductors Room' : {'Right' : 'Prehistoric Era', 'item' : 'No Items'},
    '1800s' : {'Left' : 'Prehistoric Era', 'Up' : '1500s', 'item' : 'Top Hat'},
    '1500s' : {'Down' : '1800s', 'item' : 'Monalisa'},
    '200 B.C' : {'Down' : 'Prehistoric Era', 'Right' : '1700s', 'item' : 'Han Dynasty Sword'},
    '1700s' : {'Left' : '200 B.C', 'item' : 'American Flag'}
} 

#All items available to collect
items = ['Gold', 'Dinosaur Egg', 'Top Hat', 'Monalisa', 'Han Dynasty Sword', 'American Flag']

#intructions for the user to follow
def Intructions():
    print()
    print('-------------------------')
    print('The Time Traveling Train')
    print('-------------------------')
    print()
    print('Welcome to my Time Traveling Train')
    print('There are six items you must collect before reaching me ')
    print('You do not know where I am, but I know where you are')
    print('If you make it to me before collecting all six items you lose')
    print()
    print('Commands:')
    print('Type Left,Right, Up, or Down to move between rooms')
    print('Type "Take" to collect items')
    print()
    print('Do not enter the boss room before collecting all six items or you lose')
    print('Good Luck')

def user_status():
    print('--------------------------------')
    print('You are in {}'.format(current_room))
    print('The item in this room is {}'.format(rooms[current_room]['item']))
    print('Inventory: ', inventory)
    print('--------------------------------')

#starting Room
current_room = 'Freight Train'
#items held
inventory = []
#player move set 
player_moves = ['Up','Down','Left','Right','Take']
Intructions()
user_status()

while current_room != 'Conductors Room':
    #user move input
    player_move_command = input('\n Which way would you like to travel: ')

    #player move condition
        #item collection
    if player_move_command == 'Take':
        print('\n What item would you like to take? ')
        item = input()
        if item in items:
            inventory.append(item)
            print('Item collected')
            user_status
            
        else:
            print('This item is not here') 
    #movement
    elif player_move_command in player_moves:
        player_move_command = player_move_command
        if player_move_command in rooms[current_room].keys():
            current_room = rooms[current_room][player_move_command]
            user_status()
        else:
            #if they type invalid move
            print('Not valid input')

            #if the player wants to quit
    elif player_move_command == 'exit':
            print('Thanks for playing')
            break

    else:
        #invalid input
        print('Not valid move')
#if the playe does not have all items a lose screen is prompted
if  len(inventory) != 6:
    print('You have been taken')
    print('You will now spend all iternity wondering the Time Scape')

else:
    print('-----------------------------')
    print()
    print('NOOOOOOOOOOO!!!')
    print('I have been defeated!')
    print('You were a formidable foe')
    print('You are free to leave')
    print()
    print('You Win!')
print('----------------------------------')
