#!/usr/bin/python3

from map import rooms
import string
import re


def remove_punct(text): #Removes all punctuation from user inout
    no_punc = "" #Creates a variable to have charaters added to when required
    for char in text: #For loop through text
        if (not char.isalpha()) and (not char.isspace()):
            char = ""
        else:
            no_punc = no_punc + char #If the view charaters is a letter its added to no_punc
    return no_punc
    
def remove_spaces(text): #Function that uses the .strip() function to remove spaces
    text = text.strip()
    return text


def normalise_input(user_input): #Function to normalise the users input
    normalised = ""
    for char in user_input:
        if (not char.isalpha()) and (not char.isspace()): #NAND gate to normalise the users inout to just the required text 
            char = ""
        else:
            normalised = normalised + char
            
    normalised = normalised.strip() #Strips the input
    normalised = normalised.lower() #Makes all charaters lower case
    return normalised #Returns normalised
    
def display_room(room): #Displays the current room and its description
	print("\n", room["name"].upper(), "\n")
	print(room["description"], "\n")
    
def exit_leads_to(exits, direction): #Displays the exits to the current room and thier direction
    if exits[direction] != "":
        print(exits[direction])

def print_menu_line(direction, leads_to): #Displays where the user can go and what direction they need to go in
    print("Go ", direction.upper(), "to ", leads_to)

def print_menu(exits): 
    print("You can:")
    for exit in exits:
        print_menu_line(exit, exits[exit])
    print("Where do you want to go?")

def is_valid_exit(exits, user_input): #Checks that the users selected choice is valid by being within the rooms avalible exits
    bool = False
    for exit in exits:
        if exit == user_input:
            bool = True
    return bool

def menu(exits):
    # Repeat until the player enter a valid choice
    for exit in exits: 
        # Display menu
        print_menu(exits)
        # Read player's input
        choice = input()
        # Normalise the input
        choice_normalised = normalise_input(choice)
        # Check if the input makes sense (is valid exit)
        if is_valid_exit(exits, choice_normalised) == True:
            return choice_normalised
        else:
            print("Invalid Direction, Please Try Again")


def move(exits, direction): #Function for moving the plater around the map
    new_current_room = exits[direction]
    return rooms[new_current_room]


# This is the entry point of our program
def main():
    # Start game at the reception
    current_room = rooms["Reception"]

    # Main game loop
    while True:
        # Display game status (room description etc.)
        display_room(current_room)
        # What are the possible exits from the current room?
        exits = current_room["exits"]
        # Show the menu with exits and ask the player
        direction = menu(exits)
        # Move the protagonist, i.e. update the current room
        current_room = move(exits, direction)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
