#!/usr/bin/python3

#Goal of the game is to get every item to reception

#local imports
from map import rooms
from player import *
from items import *
from gameparser import *

def list_of_items(items): #Outputs a given set of items
    '''This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string).'''

    output = "" #Creates an empty output string to be appened to 
    for item in items: #For loop iterating through all items in the items set
        output += (", " + item['name']) #Creates the output
    return output[2:] #Removes the "," that occurs at the start of the list

def print_room_items(room): #Outputs all items in a given room
    '''This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed.'''

    output = "There is " 
    item_list = list_of_items(room['items'])
    output = output + item_list + " here\n"
    print(output)

def print_inventory_items(items): #Prints user inventory and information included (carry weight and max carry weight)
    '''This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items().'''

    output = "You have "
    if len(items) > 0:
        for item in items:
            output += item["name"] + ", "
        output = output[:-2] #Again, removes all unneeded commas and whitespace
    else:
        output += "no items"
    output += "\n"
    print(output)
    print('You have a maximum carry weight of', max_carry_weight) #Outputs the users max carry weight 
    print('You currently have a carry weight of', get_current_weight(inventory)) #Outputs users current carry weight

def print_room(room): #Outputs information about the current room and any items
    '''This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc.'''

    print("\n", room["name"].upper(), "\n")
    print(room["description"], "\n")
    if len(room['items']) > 0:
        print_room_items(room)

def exit_leads_to(exits, direction): #Outputs currently avalible exits
    '''This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads.'''

    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to): #Outputs all avalible rooms a player can go from the current room and the direction
    '''This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads.'''

    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items): #Outputs all the actions a user can preform
    '''This function displays the menu of available actions to the player.'''

    print("You can:")
    #For loop of avalible exits
    for direction in exits:
        #Outputs the exits name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for room_item in room_items:
        print("TAKE", room_item['id'].upper(), " to take ", room_item['name'].upper(), "which weighs", room_item['weight'])

    for inv_item in inv_items:
        print("DROP", inv_item['id'].upper(), " to drop ", inv_item['name'].upper(), "which weighs", inv_item['weight'])

    print("What do you want to do?")

def is_valid_exit(exits, chosen_exit): # function to check if an exit is valid
    '''This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().'''

    bool = False #Bool variable to check if exit entered by the user is valid
    for exit in exits: #For loop through exits
        if exit == chosen_exit: #Checks of the input exit exists
            bool = True #If it does, bool is set to TRUE
    return bool #Value is then returned

def get_current_weight(inventory): #Function that finds the users current carry weight
    total_weight = 0 #Creates variable to track total weight
    for item in inventory: #For loop through player's inventory
        total_weight += item['weight'] #Adds weight values to the users total_weight variable
    return total_weight

def is_pickup_valid(inventory, item): #Function to check that a user can pick up an item
    current_weight = get_current_weight(inventory) #Gets the users current carry weight 
    if (current_weight + item['weight']) > 5: #Checks if the current weight + new item is > 5
        return False #If new weight > 5 then they cannot get the item 
    else: 
        return True #If not the can collect the item

def get_total_num_items(): #Gets the total number of items in the game world 
    total_in_inv = len(inventory) #Gets the number of items in player's inventory
    total_in_rooms = 0
    for room in rooms: #For loop through rooms
        for item in rooms[room]['items']: #Loop the counts all items in the game world 
            total_in_rooms += 1
    total_items = total_in_inv + total_in_rooms
    return total_items #Returns total items in the game world plus including the players inventory

def is_game_won(): #Function to see if all items are in reception
    num_items_in_recp = 0 #Varibale for total number of items in reception is created
    for items in rooms['Reception']['items']: #For loop through the items in reception
        num_items_in_recp += 1 #Adds to count of items in reception
    total_items = get_total_num_items()
    if total_items == num_items_in_recp: #Compares values for winning condition
        return True
    else:
        return False

def execute_go(direction): #Go command to change rooms
    global current_room #Variable is set to global so it can be appened later in the function
    exits = current_room['exits']
    if is_valid_exit(exits, direction):
        current_room = rooms[current_room['exits'][direction]]
    else:
        print("You cannot go there.")

def execute_take(item_id): #Take command to pick up items
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    success = False
    for items in current_room['items']: #For loop through room's items
        if items['id'] == item_id:
            if is_pickup_valid(inventory, items) == True: #Checks if an item can be picked up
                current_room['items'].remove(items) #Removes item from current room item array
                inventory.append(items) #Adds the item to the users inventory
                print(item_id, " added to inventory") #Outputs message showing item has been aquired
                success = True

    if success == False:
        print("You cannot take that")

def execute_drop(item_id): #Function to drop an item
    success = False
    for items in inventory: #For loop through inventory
        if item_id == items['id']:
            current_room['items'].append(items) #Adds item to room's item array
            inventory.remove(items) #Removes item from player inventory
            print(items['name'], "dropped") #Outputs message showing item has been dropped
            success = True
    if success == False:
        print("You cannot drop that")

def execute_command(command): #Command sorting function
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Be more specific! Where do you want to Go?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Be more specific! What do you want to Take?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Be more specific! What do you want to Drop?")

    else:
        print("You make no sense! Try again.")


def menu(exits, room_items, inv_items): #Print out all informationt to player
    '''This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.'''

    #Display menu
    print_menu(exits, room_items, inv_items)

    #Read player's input
    user_input = input("> ")

    #Normalise the input
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input


def move(exits, direction): #Gets the next room to move to
    '''This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction".'''

    #Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main(): #main game loop
    won = False #Sets bool win condition to False to start game
    # Main game loop

    #Welcome message for the player when the game starts
    print("Welcome to my game!" + "\n" + "Your objective is to get every item to reception" + "\n" + "Good Luck!")

    #Checks game win status
    while won == False:
        #Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        #Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        #Execute the player's command
        execute_command(command)

        #Checks if game is won
        won = is_game_won()

        # if game is won, print winning message
        if won == True:
            print("Congratulations!" + "\n" + "You have won the game") #"\n" creates a new line in the print

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
