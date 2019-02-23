from items import *
global max_weight_allowed

"""This file is referred to by various functions in game.py to ascertain where different exits lead to
and to enable the efficient reporting of different room names, which items are in them and the movement
of items from those rooms into the inventory of the player in player.py"""


room_outside = {
    "name": "Outside",

    "description":
    """It's your first day. Lighten up... Please don't tell me I have to
teach you how to open a door... Please.""",

    "description_alt":
    """Yep. Its interesting isn't it? The outside world. Its a shame you are
NOT ALLOWED to associate yourself with it until AFTER you've done what we've
paid you to do!""",

    "exits": {"north": "Main"},

    "items": [item_rock],

    "props": [],

    "consumables": [],

    "song": "outside.mp3",

    "song_alt": "outside_alt.mp3",

    "menu_art":
"\n" \
"\n" \
"  ___            _           _       _         \n" \
" / _ \   _   _  | |_   ___  (_)   __| |   ___  \n" \
"| | | | | | | | | __| / __| | |  / _` |  / _ \ \n" \
"| |_| | | |_| | | |_  \__ \ | | | (_| | |  __/ \n" \
" \___/   \__,_|  \__| |___/ |_|  \__,_|  \___| \n" \
"\n",


    "entry_art":
"\n" \
"\n" \
"  _____           _                   _                      ___            _           _       _                     \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _     / _ \   _   _  | |_   ___  (_)   __| |   ___              \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | | | | | | | | | __| / __| | |  / _` |  / _ \             \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   | |_| | | |_| | | |_  \__ \ | | | (_| | |  __/  _   _   _  \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |    \___/   \__,_|  \__| |___/ |_|  \__,_|  \___| (_) (_) (_) \n" \
"                                                  |___/                                                               \n" \
"\n",

    "required_items": [],

    "required_current_quest_min": 1,

    "visited": False
}


room_main = {
    "name": "The Main Office",

    "description":
    """You see an abundance of smartly dressed
people at their desks. They're speaking but the telephone rings make it difficult
to hear them... One guy seems to be eating a turkey sandwich... Maybe its chicken...
Same thing... Right?""",

    "description_alt":
    """The phones are still ringing. The guy who was eating a turkey or chicken sandwich
is now taking shots from his desk. You wonder to yourself, what have I gotten myself in
for? You kind of like it, you think?""",

    "exits": {"south": "Outside", "east": "Security", "west": "Spoons", "north": "Kitchen"},

    "items": [item_newspaper],

    "props": [],

    "consumables": [],

    "song": "main.mp3",

    "song_alt": "main_alt.mp3",

    "menu_art":
"\n" \
"\n" \
" __  __           _              ___     __    __   _                \n" \
"|  \/  |   __ _  (_)  _ __      / _ \   / _|  / _| (_)   ___    ___  \n" \
"| |\/| |  / _` | | | | '_ \    | | | | | |_  | |_  | |  / __|  / _ \ \n" \
"| |  | | | (_| | | | | | | |   | |_| | |  _| |  _| | | | (__  |  __/ \n" \
"|_|  |_|  \__,_| |_| |_| |_|    \___/  |_|   |_|   |_|  \___|  \___| \n" \
"\n",

    "entry_art":
"\n" \
"\n" \
"  _____           _                   _                     __  __           _              ___     __    __   _                            \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    |  \/  |   __ _  (_)  _ __      / _ \   / _|  / _| (_)   ___    ___              \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | |\/| |  / _` | | | | '_ \    | | | | | |_  | |_  | |  / __|  / _ \             \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   | |  | | | (_| | | | | | | |   | |_| | |  _| |  _| | | | (__  |  __/  _   _   _  \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   |_|  |_|  \__,_| |_| |_| |_|    \___/  |_|   |_|   |_|  \___|  \___| (_) (_) (_) \n" \
"                                                  |___/                                                                                     \n" \
"\n",

    "required_items": [],

    "required_current_quest_min": 1,

    "visited": False
}

room_kitchen = {
    "name": "The Kitchen",

    "description":
    """There seems to be an awful song from the seventies playing here... Kirill
must be around here somewhere... surely. Anyway, at least now you can make
the tea...""",

    "description_alt":
    """Hungry are you? Can't you wait to take a break AFTER you've found the 
missing guy? Ok, whatever. There's plenty of sandwiches here. They aren't yours
but I guess the world owes you something? Right? Of course it does! It sounds
like Kirill's Greatest Hits is still playing on the radio?""",

    "exits":  {"south": "Main"},

    "items": [item_milk, item_sugar, item_teabags],

    "props": [
        {
            "id": "kettle",
            "name": "kettle",
            "use_action": "player.inventory.append(item_tea); player.inventory.remove(item_teabags); player.inventory.remove(item_milk); player.inventory.remove(item_sugar)",
            "use_condition": "item_sugar in player.inventory and item_milk in player.inventory and item_teabags in player.inventory",
            "use_comment": "You now have a lovely cuppa. Now go get it to Kirill!"
        }
    ],

    "consumables": [
        {
            "id": "sandwiches",
            "name": "sandwiches",
            "consume_action": "add_strength(2)",
            "consume_comment": "Yum. This must belong to that guy who's eating the ham or turkey sandwich in the office. But what do you care? You're now strong enough to carry more kilograms!"
        }
    ],

    "song": "kitchen.mp3",

    "song_alt": "kitchen_alt.mp3",

    "menu_art": 
"\n" \
"\n" \
" _  __  _   _            _                     \n" \
"| |/ / (_) | |_    ___  | |__     ___   _ __   \n" \
"| ' /  | | | __|  / __| | '_ \   / _ \ | '_ \  \n" \
"| . \  | | | |_  | (__  | | | | |  __/ | | | | \n" \
"|_|\_\ |_|  \__|  \___| |_| |_|  \___| |_| |_| \n" \
"\n",

    "entry_art": 
"\n" \
"\n" \
"  _____           _                   _                     _  __  _   _            _                                 \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    | |/ / (_) | |_    ___  | |__     ___   _ __               \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | ' /  | | | __|  / __| | '_ \   / _ \ | '_ \              \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   | . \  | | | |_  | (__  | | | | |  __/ | | | |  _   _   _  \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   |_|\_\ |_|  \__|  \___| |_| |_|  \___| |_| |_| (_) (_) (_) \n" \
"                                                  |___/                                                               \n" \
"\n",

    "required_items": [],

    "required_current_quest_min": 2,

    "visited": False
}

room_security = {
    "name": "The Security Suite",

    "description":
    """There is a guy who seems to be half asleep in the corner.
There's a sea of old style tube TV monitors from nineteen ninety.
Looks like the budget hasn't quite stretched. Well... So much for
a future of pay rises?""",

    "description_alt":
    """The security guy is completely asleep now, a bottle of gin
has since appeared. It must be hard work looking at CCTV cameras
all day? But there's that huge hammer that you didn't spot before,
maybe that might be useful for something?""",

    "exits": {"west": "Main", "south": "Kirill"},

    "items": [item_id],

    "props": [],

    "consumables": [],

    "song": "security.mp3",

    "song_alt": "security_alt.mp3",

    "menu_art": 
"\n" \
"\n" \
" ____                                 _   _               ____            _   _           \n" \
"/ ___|    ___    ___   _   _   _ __  (_) | |_   _   _    / ___|   _   _  (_) | |_    ___  \n" \
"\___ \   / _ \  / __| | | | | | '__| | | | __| | | | |   \___ \  | | | | | | | __|  / _ \ \n" \
" ___) | |  __/ | (__  | |_| | | |    | | | |_  | |_| |    ___) | | |_| | | | | |_  |  __/ \n" \
"|____/   \___|  \___|  \__,_| |_|    |_|  \__|  \__, |   |____/   \__,_| |_|  \__|  \___| \n" \
"                                                 |___/                                    \n" \
"\n",

    "entry_art": 
"\n" \
"\n" \
"  _____           _                   _                     ____                                 _   _               ____            _   _                       \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    / ___|    ___    ___   _   _   _ __  (_) | |_   _   _    / ___|   _   _  (_) | |_    ___              \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   \___ \   / _ \  / __| | | | | | '__| | | | __| | | | |   \___ \  | | | | | | | __|  / _ \             \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |    ___) | |  __/ | (__  | |_| | | |    | | | |_  | |_| |    ___) | | |_| | | | | |_  |  __/  _   _   _  \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   |____/   \___|  \___|  \__,_| |_|    |_|  \__|  \__, |   |____/   \__,_| |_|  \__|  \___| (_) (_) (_) \n" \
"                                                  |___/                                                    |___/                                                 \n" \
"\n",

    "required_items": [],

    "required_current_quest_min": 1,

    "visited": False
}

room_spoons = {
    "name": "Spoons",

    "description":
    """You've just walked in and can see Jing, that other lecturer, sat down near
the window. She says that Kirill had started taking up singing lessons down in
the Opera House... Perhaps we should check there. She asks you to buy her a drink.
You refuse... Because there is much more important business at hand.""",

    "description_alt":
    """Jing has since got up and started busting a move. She must have gotten 
offended because you didn't buy her a drink. You really need to learn to have 
a heart. Never mind. Don't even think about having a dance! Go open that door!""",

    "exits": {"east": "Main", "south": "Opera"},

    "items": [],

    "props": [],

    "consumables": [
        {
            "id": "beer",
            "name": "beer",
            "consume_action": "add_strength(1)",
            "consume_comment": "This is some good stuff, you can now carry more kilograms!"
        },
        {
            "id": "jager",
            "name": "jager",
            "consume_action": "add_strength(1)",
            "consume_comment": "Who knew something this German could be this good?, you can now carry more kilograms!"
        },
        {
            "id": "vodka",
            "name": "vodka",
            "consume_action": "add_strength(1)",
            "consume_comment": "As this is russian, it is only natural that it makes you stronger, you can now carry more kilograms!"
        }
    ],

    "song": "spoons.mp3",

    "song_alt": "spoons_alt.mp3",

    "menu_art":
"\n" \
"\n" \
"  ____                                         \n" \
" / ___|   _ __     ___     ___    _ __    ___  \n" \
" \___ \  | '_ \   / _ \   / _ \  | '_ \  / __| \n" \
"  ___) | | |_) | | (_) | | (_) | | | | | \__ \ \n" \
" |____/  | .__/   \___/   \___/  |_| |_| |___/ \n" \
"         |_|                                   \n" \
"\n",

    "entry_art":
"\n" \
"\n" \
"  _____           _                   _                     ____                                               __   \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    / ___|   _ __     ___     ___    _ __    ___     _  \ \  \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   \___ \  | '_ \   / _ \   / _ \  | '_ \  / __|   (_)  | | \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |    ___) | | |_) | | (_) | | (_) | | | | | \__ \    _   | | \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   |____/  | .__/   \___/   \___/  |_| |_| |___/   ( )  | | \n" \
"                                                  |___/            |_|                                     |/  /_/  \n" \
"\n",

    "required_items": [],

    "required_current_quest_min": 3,

    "visited": False
}

room_opera = {
    "name": "The Opera House",

    "description":
    """Hmm... It seems like those singing lessons that Jing was talking
about are paying off. This is music to your ears, you think to yourself.
You take a closer look, but clearly this isn't the guy you're looking for.
What you do notice, however, is a mysterious door with "Pandora's Box" 
written on it. Perhaps it's important?""",

"description_alt":
    """So you're back? Let's break open that door and see what's behind
it once and for all then?. Yeah, there's still a Russian guy singing on 
the stage.""",

    "exits": {"north": "Spoons", "south": "Pandora"},

    "items": [],

    "props": [],

    "consumables": [],

    "song": "opera.mp3",

    "song_alt": "opera_alt.mp3",

    "menu_art":
"\n" \
"\n" \
"   ___                                    _   _                                \n" \
"  / _ \   _ __     ___   _ __    __ _    | | | |   ___    _   _   ___    ___   \n" \
" | | | | | '_ \   / _ \ | '__|  / _` |   | |_| |  / _ \  | | | | / __|  / _ \  \n" \
" | |_| | | |_) | |  __/ | |    | (_| |   |  _  | | (_) | | |_| | \__ \ |  __/  \n" \
"  \___/  | .__/   \___| |_|     \__,_|   |_| |_|  \___/   \__,_| |___/  \___|  \n" \
"         |_|                                                                   \n" \
"\n",

    "entry_art":
"\n" \
"\n" \
"  _____           _                   _                      ___                                    _   _                                           \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _     / _ \   _ __     ___   _ __    __ _    | | | |   ___    _   _   ___    ___              \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | | | | | '_ \   / _ \ | '__|  / _` |   | |_| |  / _ \  | | | | / __|  / _ \             \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   | |_| | | |_) | |  __/ | |    | (_| |   |  _  | | (_) | | |_| | \__ \ |  __/  _   _   _  \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |    \___/  | .__/   \___| |_|     \__,_|   |_| |_|  \___/   \__,_| |___/  \___| (_) (_) (_) \n" \
"                                                  |___/            |_|                                                                              \n" \
"\n",

    "required_items": [],

    "required_current_quest_min": 3,

    "visited": False
}

room_pandora = {
    "name": "Pandora's Box",

    "description":
    """You enter a dark room. You hear a roaring sound coming from the far
corner of the room, followed by a mighty grunt. Suddenly, the light comes
on. It's Kirill! He's fighting a grizzly bear and seems to be winning!""",
    
    "description_alt":
    """You enter a dark room. You hear a roaring sound coming from the far
corner of the room, followed by a mighty grunt. Suddenly, the light comes
on. It's Kirill! He's fighting a grizzly bear and seems to be winning!""",

    "exits": {"south": "Spoons", "east": "Kitchen"},

    "items": [],

    "props": [],

    "consumables": [],

    "song": "pandora.mp3",

    "song_alt": "pandora.mp3",

    "menu_art":
"\n" \
"\n" \
"██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ██████╗  █████╗ ███████╗    ██████╗  ██████╗ ██╗  ██╗ \n" \
"██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗╚██╗██╔╝ \n" \
"█████╔╝ ███████║██╔██╗ ██║██║  ██║██║   ██║██████╔╝███████║███████╗    ██████╔╝██║   ██║ ╚███╔╝  \n" \
"██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██║   ██║██╔══██╗██╔══██║╚════██║    ██╔══██╗██║   ██║ ██╔██╗  \n" \
"██║     ██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║  ██║██║  ██║███████║    ██████╔╝╚██████╔╝██╔╝ ██╗ \n" \
"╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ \n" \
"\n",

    "entry_art":
"\n" \
"\n" \
"███████╗███╗   ██╗████████╗███████╗██████╗ ██╗███╗   ██╗ ██████╗     ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ██████╗  █████╗ ███████╗    ██████╗  ██████╗ ██╗  ██╗ \n" \
"██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██║████╗  ██║██╔════╝     ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗╚██╗██╔╝ \n" \
"█████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝██║██╔██╗ ██║██║  ███╗    ██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██████╔╝███████║███████╗    ██████╔╝██║   ██║ ╚███╔╝  \n" \
"██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║██║╚██╗██║██║   ██║    ██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██║   ██║██╔══██╗██╔══██║╚════██║    ██╔══██╗██║   ██║ ██╔██╗  \n" \
"███████╗██║ ╚████║   ██║   ███████╗██║  ██║██║██║ ╚████║╚██████╔╝    ██║     ██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║  ██║██║  ██║███████║    ██████╔╝╚██████╔╝██╔╝ ██╗ \n" \
"╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ \n" \
"\n",

    "required_items": [item_hammer, item_sword],

    "required_current_quest_min": 5,

    "visited": False
}

room_kirill = {
    "name": "Kirill's Office",

    "description":
    """This must be where Kirill spends his working day... Right?
Perhaps you're missing something, because the only thing that's here
to drink the tea you just made is the model Linux penguin in the corner.""",

    "description_alt":
    """Yep, nothing has changed since the last time you were in here.
So... Are you gonna go and find Kirill or not?""",

    "exits": {"north": "Security"},

    "items": [item_penguin, item_putin, item_cash, item_sword],

    "props": [],

    "consumables": [],

    "song": "kirill.mp3",

    "song_alt": "kirill_alt.mp3",

    "menu_art":
"\n" \
"\n" \
" _  __  _          _   _   _   _            ___     __    __   _                            \n" \
"| |/ / (_)  _ __  (_) | | | | ( )  ___     / _ \   / _|  / _| (_)   ___    ___              \n" \
"| ' /  | | | '__| | | | | | | |/  / __|   | | | | | |_  | |_  | |  / __|  / _ \             \n" \
"| . \  | | | |    | | | | | |     \__ \   | |_| | |  _| |  _| | | | (__  |  __/  _   _   _  \n" \
"|_|\_\ |_| |_|    |_| |_| |_|     |___/    \___/  |_|   |_|   |_|  \___|  \___| (_) (_) (_) \n" \
"\n",

    "entry_art":
"\n" \
"\n" \
"  _____           _                   _                     _  __  _          _   _   _   _            ___     __    __   _                            \n" \
" | ____|  _ __   | |_    ___   _ __  (_)  _ __     __ _    | |/ / (_)  _ __  (_) | | | | ( )  ___     / _ \   / _|  / _| (_)   ___    ___              \n" \
" |  _|   | '_ \  | __|  / _ \ | '__| | | | '_ \   / _` |   | ' /  | | | '__| | | | | | | |/  / __|   | | | | | |_  | |_  | |  / __|  / _ \             \n" \
" | |___  | | | | | |_  |  __/ | |    | | | | | | | (_| |   | . \  | | | |    | | | | | |     \__ \   | |_| | |  _| |  _| | | | (__  |  __/  _   _   _  \n" \
" |_____| |_| |_|  \__|  \___| |_|    |_| |_| |_|  \__, |   |_|\_\ |_| |_|    |_| |_| |_|     |___/    \___/  |_|   |_|   |_|  \___|  \___| (_) (_) (_) \n" \
"                                                  |___/                                                                                                \n" \
"\n",

    "required_items": [item_id, item_tea],

    "required_current_quest_min": 2,

    "visited": False
}



rooms = {
    "Outside": room_outside,
    "Main": room_main,
    "Kitchen": room_kitchen,
    "Security": room_security,
    "Spoons": room_spoons,
    "Opera": room_opera,
    "Pandora": room_pandora,
    "Kirill": room_kirill
}
