#!/usr/bin/python3
#Game 1 programming task

#Importing the rooms from the map given, and importing the string module
from map import rooms
import string


def remove_punct(text):
    '''This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation.'''

    #This strips all the text of its punctuation 
    no_punc_input = ""
    #For loop to iterate through the code removing all charaters and whitespace 
    for char in text:
        #This NAND gate checks if hte current charater is a letter, if it's not no change is made to no_punc_input
        if (not char.isalpha()) and (not char.isspace()):
            char = ""
        #If the letter being currently viewed is a letter then it is added to the variable no_punc_input
        else:
            no_punc_input = no_punc_input + char
    #Returning the value for no_punc_input
    return no_punc_input
    
    
def remove_spaces(text):
    '''This function is used to remove leading and trailing spaces from a string.
    It takes a string and returns a new string with does not have leading and
    trailing spaces. '''

    #The python function .strip() ensures all chars have been stripped from the beginning and the end of the string
    text = text.strip()
    return text


def normalise_input(user_input):
    '''This function removes all punctuation, leading and trailing
    spaces from a string, and converts the string to lower case.'''

    #This section of code functions very similarly to remove_punc, 
    normalised = ""
    for char in user_input:
        if (not char.isalpha()) and (not char.isspace()):
            char = ""
        else:
            normalised = normalised + char

    #Utilising the .strip() and .lower() modules to normalise the text
    normalised = normalised.strip()
    normalised = normalised.lower()
    #Returns the final value
    return normalised

def display_room(room):
    '''This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc.'''

    #This displays the room and its description, the \n indicates a new line from the next print
    print("\n" + room["name"].upper() + "\n\n" + room["description"] + "\n")

    
def exit_leads_to(exits, direction):
    '''This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads'''

    #This code shows what exits are avalible to the user, and capsizes the direction needed for inout
    leads_to = exits[direction]
    print("'" + rooms[leads_to]["name"] + "'")

def print_menu_line(direction, leads_to):
    '''This function prints a line of a menu of exits. It takes two strings: a
    direction (the name of an exit) and the name of the room into which it
    leads (leads_to).'''

    #This shows where a user is able to go, the direction and what it leads to
    print("Go " + direction.upper() + " to " + leads_to +".")


def print_menu(exits):
    '''This function displays the menu of available exits to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    menu should, for each exit, call the function print_menu_line() to print
    the information about each exit in the appropriate format. The room into
    which an exit leads is obtained using the function exit_leads_to().
    For example, the menu of exits from Reception may look like this:'''

    #This function pulls the last group of functions together, showing the user where they can go and asking them where they want to go (Although not yet taking the input)
    print("You can:")
    for direction, leads_to in exits.items():
        print_menu_line(direction.upper(), rooms[leads_to]["name"])
    print("Where do you want to go?")

def is_valid_exit(exits, user_input):
    '''This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "user_input" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().'''

    #The code checks that user has entered a valid room input when prompted, returning an error if not
    try: 
        exits[user_input]
        return True
    except KeyError:
        return False


def menu(exits):
    '''This function, given a dictionary of possible exits from a room, prints the
    menu of exits using print_menu() function. It then prompts the player to type
    a name of an exit where she wants to go. The players's input is normalised
    using the normalise_input() function before further checks are done.  The
    function then checks whether this exit is a valid one, using the function
    is_valid_exit(). If the exit is valid then the function returns the name
    of the chosen exit. Otherwise the menu is displayed again and the player
    prompted, repeatedly, until a correct choice is entered.'''

    # Loops until the user enter a valid room input
    while True:
        print_menu(exits)
        destination = input()
        destination = normalise_input(destination)
        if is_valid_exit(exits, destination) == False:
            print("Input invalid!")
        else:
            return destination

def move(exits, direction):
    '''This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction".'''

    index = [exits][0][direction]
    newroom = rooms[index]
    return newroom

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
