from map import rooms
from player import *
from items import *
from gameparser import *
import string

# Dictionaries containing all of the quest data.


# Details for the first quest
quest_1 = {
    "id": 1,

    "name": "The New Guy",

    "description": "Collect your ID card from security. You'll need it to access a lot of places. KEEP IT ON YOU AT ALL TIMES!!!",

    "criteria": """(item_id in player.inventory)""",

    "name_art": 
"\n" \
".___________. __    __   _______    .__   __.  ___________    __    ____      _______  __    __  ____    ____ \n" \
"|           ||  |  |  | |   ____|   |  \ |  | |   ____\   \  /  \  /   /     /  _____||  |  |  | \   \  /   / \n" \
"`---|  |----`|  |__|  | |  |__      |   \|  | |  |__   \   \/    \/   /     |  |  __  |  |  |  |  \   \/   /  \n" \
"    |  |     |   __   | |   __|     |  . `  | |   __|   \            /      |  | |_ | |  |  |  |   \_    _/   \n" \
"    |  |     |  |  |  | |  |____    |  |\   | |  |____   \    /\    /       |  |__| | |  `--'  |     |  |     \n" \
"    |__|     |__|  |__| |_______|   |__| \__| |_______|   \__/  \__/         \______|  \______/      |__|     \n" \
"\n"
}

# Details for the second quest
quest_2 = {
    "id": 2,

    "name": "Tea Connoisseur",

    "description": "Make Kirill some tea. That's your job, after all.",

    "criteria": """(item_tea in player.inventory) and (player.current_room == map.rooms["Kirill"])""",

    "name_art":
"\n" \
" _____             ____                        _                          \n" \
"|_   _|__  __ _   / ___|___  _ __  _ __   ___ (_)___ ___  ___ _   _ _ __  \n" \
"  | |/ _ \/ _` | | |   / _ \| '_ \| '_ \ / _ \| / __/ __|/ _ \ | | | '__| \n" \
"  | |  __/ (_| | | |__| (_) | | | | | | | (_) | \__ \__ \  __/ |_| | |    \n" \
"  |_|\___|\__,_|  \____\___/|_| |_|_| |_|\___/|_|___/___/\___|\__,_|_|    \n" \
"                                                                          \n" \
"\n"
}

# Details for the third quest
quest_3 = {
    "id": 3,

    "name": "Search and Rescue",

    "description": "Find Kirill. He's gone missing, and his tea is going cold.",

    "criteria": """(player.current_room == map.rooms["Opera"])""",

    "name_art":
"\n" \
" ____                      _                       _   ____                            \n" \
"/ ___|  ___  __ _ _ __ ___| |__     __ _ _ __   __| | |  _ \ ___  ___  ___ _   _  ___  \n" \
"\___ \ / _ \/ _` | '__/ __| '_ \   / _` | '_ \ / _` | | |_) / _ \/ __|/ __| | | |/ _ \ \n" \
" ___) |  __/ (_| | | | (__| | | | | (_| | | | | (_| | |  _ <  __/\__ \ (__| |_| |  __/ \n" \
"|____/ \___|\__,_|_|  \___|_| |_|  \__,_|_| |_|\__,_| |_| \_\___||___/\___|\__,_|\___| \n" \
"                                                                                       \n" \
"\n"
}

# Details for the fourth quest
quest_4 = {
    "id": 4,

    "name": "Forced Entry",

    "description": """Look for Kirill in Pandora's Box. You may need to force your way in, so go and find something to break that door open with!
make sure that you are strong enough to carry it. Go eat or drink something if you cant pick it up!""",

    "criteria": """(item_hammer in player.inventory)""",

    "name_art":
"\n" \
" _____                      _   _____       _               \n" \
"|  ___|__  _ __ ___ ___  __| | | ____|_ __ | |_ _ __ _   _  \n" \
"| |_ / _ \| '__/ __/ _ \/ _` | |  _| | '_ \| __| '__| | | | \n" \
"|  _| (_) | | | (_|  __/ (_| | | |___| | | | |_| |  | |_| | \n" \
"|_|  \___/|_|  \___\___|\__,_| |_____|_| |_|\__|_|   \__, | \n" \
"                                                     |___/  \n" \
"\n"
}

# Details for the fifth quest
quest_5 = {
    "id": 5,

    "name": "Pandora's Box",

    "description": "Go back to the Opera House with the hammer and see what's behind that mysterious door. Before you go, you'd better take that sword from his office too, just in case.",

    "criteria": """(player.current_room == map.rooms["Pandora"])""",

    "name_art":
"\n" \
" ____                 _                 _       ____             \n" \
"|  _ \ __ _ _ __   __| | ___  _ __ __ _( )___  | __ )  _____  __ \n" \
"| |_) / _` | '_ \ / _` |/ _ \| '__/ _` |// __| |  _ \ / _ \ \/ / \n" \
"|  __/ (_| | | | | (_| | (_) | | | (_| | \__ \ | |_) | (_) >  <  \n" \
"|_|   \__,_|_| |_|\__,_|\___/|_|  \__,_| |___/ |____/ \___/_/\_\ \n" \
"                                                                 \n" \
"\n"
}


# Dictionary of quest IDs referred to in game.py
quest_numbers = {
    1: quest_1,
    2: quest_2,
    3: quest_3,
    4: quest_4,
    5: quest_5
}
