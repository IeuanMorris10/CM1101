from items import *
import map

# Hold the name of the player, blank by default:
#global player_name
#player_name = ""

# Declare what the player is holding at outset
inventory = [item_phone, item_wallet]

# How many kilograms can the player carry?
max_weight_allowed = 3

# Start game at the reception
current_room = map.rooms["Outside"]

# Setting the default quest, i.e. that at the start of play
current_quest = 1

# Total weight carried. Automatically updated when needed.
weight_carried = 0

# DEBUG
skip_to_end = False # FALSE FOR RELEASE
if skip_to_end:
    max_weight_allowed = 7
    inventory.append(item_sword)
    inventory.append(item_hammer)
    current_room = map.rooms["Opera"]
    current_quest = 5
