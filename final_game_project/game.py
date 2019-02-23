#!/usr/bin/python3
# coding=utf-8

# Dynamic game state
import map
import player

# Third-party libraries
import pyttsx3
import pygame

# Built-in libraries
import sys
import os
import importlib
import time
import string

# External game functions
from gameparser import *
from animation import *

# Static resources
from items import *
from quests import *
import anim_bear
import anim_door
import credits

# Global variables
tts_engine = None # Reference to text-to-speech engine
skip_long_parts = False # For debugging and testing, set by adding "fast" after game.py in command line
audio_supported = True # Cleared if the audio system cannot start.
player_name = "" # Name of the player

def opening():
    """This function is called prior to the game loop, as such it shows its contents
    prior to the game actually starting"""
    global player_name
    # Clear screen
    cls()
    # Start playing initial soundtrack
    # global set_song
    set_song(player.current_room["song"])

    if skip_long_parts:
        take_player_name()
        return

    # ASCII art to promt user to use speakers
    print(
"\n" \
"\n" \
"████████╗██╗   ██╗██████╗ ███╗   ██╗     ██████╗ ███╗   ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗██████╗     ███████╗██████╗ ███████╗ █████╗ ██╗  ██╗███████╗██████╗ ███████╗██╗ \n" \
"╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██╔═══██╗████╗  ██║    ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ██╔════╝██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗██╔════╝██║ \n" \
"   ██║   ██║   ██║██████╔╝██╔██╗ ██║    ██║   ██║██╔██╗ ██║     ╚████╔╝ ██║   ██║██║   ██║██████╔╝    ███████╗██████╔╝█████╗  ███████║█████╔╝ █████╗  ██████╔╝███████╗██║ \n" \
"   ██║   ██║   ██║██╔══██╗██║╚██╗██║    ██║   ██║██║╚██╗██║      ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ╚════██║██╔═══╝ ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗╚════██║╚═╝ \n" \
"   ██║   ╚██████╔╝██║  ██║██║ ╚████║    ╚██████╔╝██║ ╚████║       ██║   ╚██████╔╝╚██████╔╝██║  ██║    ███████║██║     ███████╗██║  ██║██║  ██╗███████╗██║  ██║███████║██╗ \n" \
"   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═══╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ \n" \
"\n" \
"\n"
)
    # Hold script for 5 seconds
    time.sleep(5)
    # Clear screen
    cls()
    # Hold script for 2 seconds
    time.sleep(2)
    # Tron welcomes player
    text_to_speech("Welcome!")
    # Tron ASCII introduction
    print(
# Double backslash must be properly escaped in TRON 5000's nose
"\n" \
"████████╗██████╗  ██████╗ ███╗   ██╗    ███████╗ ██████╗  ██████╗  ██████╗  \n" \
"╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║    ██╔════╝██╔═████╗██╔═████╗██╔═████╗ \n" \
"   ██║   ██████╔╝██║   ██║██╔██╗ ██║    ███████╗██║██╔██║██║██╔██║██║██╔██║ \n" \
"   ██║   ██╔══██╗██║   ██║██║╚██╗██║    ╚════██║████╔╝██║████╔╝██║████╔╝██║ \n" \
"   ██║   ██║  ██║╚██████╔╝██║ ╚████║    ███████║╚██████╔╝╚██████╔╝╚██████╔╝ \n" \
"   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝  \n" \
"\n" \
"                __________                 \n" \
"         ______/ ________ \______          \n" \
"       _/      ____________      \_        \n" \
"     _/____________    ____________\_      \n" \
"    /  ___________ \  / ___________  \     \n" \
"   /  /           \ \/ /           \  \    \n" \
"  /  /            /    \            \  \   \n" \
"  |  \           / _  _ \           /  |   \n" \
"__|\_____   ___   //  \\\\   ___   _____/|__ \n" \
"[_       \     \  X    X  /     /       _] \n" \
"__|     \ \                    / /     |__ \n" \
"[____  \ \ \   ____________   / / /  ____] \n" \
"     \  \ \ \/||.||.||.||.||\/ / /  /      \n" \
"      \_ \ \  ||.||.||.||.||  / / _/       \n" \
"        \ \   ||.||.||.||.||   / /         \n" \
"         \_   ||_||_||_||_||   _/          \n" \
"           \     ........     /            \n" \
"            \________________/             \n" \
"\n" \
"\n" \
"\n" \
"██╗   ██╗ ██████╗ ██╗   ██╗██████╗      ██████╗ ██╗      █████╗ ███╗   ███╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗███████╗     █████╗ ███████╗███████╗██╗███████╗████████╗ █████╗ ███╗   ██╗████████╗ \n" \
"╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ██╔════╝ ██║     ██╔══██╗████╗ ████║██╔═══██╗██╔══██╗██╔═══██╗██║   ██║██╔════╝    ██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║╚══██╔══╝ \n" \
" ╚████╔╝ ██║   ██║██║   ██║██████╔╝    ██║  ███╗██║     ███████║██╔████╔██║██║   ██║██████╔╝██║   ██║██║   ██║███████╗    ███████║███████╗███████╗██║███████╗   ██║   ███████║██╔██╗ ██║   ██║    \n" \
"  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ██║   ██║██║     ██╔══██║██║╚██╔╝██║██║   ██║██╔══██╗██║   ██║██║   ██║╚════██║    ██╔══██║╚════██║╚════██║██║╚════██║   ██║   ██╔══██║██║╚██╗██║   ██║    \n" \
"   ██║   ╚██████╔╝╚██████╔╝██║  ██║    ╚██████╔╝███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝███████║    ██║  ██║███████║███████║██║███████║   ██║   ██║  ██║██║ ╚████║   ██║    \n" \
"   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    \n" \
"\n" \
"\n" \
"\n" \
"\n"
)
    # Hold script for 1 second.
    time.sleep(1)
    # Tron 500 introduces itself.
    text_to_speech("My name is Tron Five Thousand. I will be your guide.")
    # Hold script for 2 seconds.
    time.sleep(2)
    # Tron hopes the player is ready for the ride of their life.
    text_to_speech("I hope you're ready for the ride of your life...")
    # Hold script for 0.5 seconds
    time.sleep(0.5)
    # Clear screen
    cls()
    # Obtain player name
    take_player_name()
    # Clear screen
    cls()
    # Tron tells player to buckle up
    text_to_speech("Buckle up, " + player_name + ". because:")
    # ASCII art of "This"
    print(
"\n" \
"\n" \
" ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  \n" \
"▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ \n" \
" ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  \n" \
"     ▐░▌     ▐░▌       ▐░▌     ▐░▌     ▐░▌           \n" \
"     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄  \n" \
"     ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌ \n" \
"     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌ \n" \
"     ▐░▌     ▐░▌       ▐░▌     ▐░▌               ▐░▌ \n" \
"     ▐░▌     ▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌ \n" \
"     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ \n" \
"      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  \n" \
"\n"
)
    # Tron says "this"
    text_to_speech("This")
    # Create a little room below
    print("\n" * 5)
    # Hold the script for 0.5 seconds.
    time.sleep(0.5)
    # ASCII art of "Is"
    print(
"\n" \
"\n" \
" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  \n" \
"▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ \n" \
" ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  \n" \
"     ▐░▌     ▐░▌           \n" \
"     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄  \n" \
"     ▐░▌     ▐░░░░░░░░░░░▌ \n" \
"     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌ \n" \
"     ▐░▌               ▐░▌ \n" \
" ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌ \n" \
"▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ \n" \
" ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  \n" \
"\n"
)
    # Tron says "is"
    text_to_speech("Iz")
    # Clear screen
    cls()
    # Hold the script for 0.5 seconds
    time.sleep(0.5)
    # Print Tea Boy ASCII art
    print(
"\n" \
"\n" \
"\n" \
"\n" \
"\n" \
" .----------------.  .----------------.  .----------------.           .----------------.  .----------------.  .----------------.  \n" \
"| .--------------. || .--------------. || .--------------. |         | .--------------. || .--------------. || .--------------. | \n" \
"| |  _________   | || |  _________   | || |      __      | |         | |   ______     | || |     ____     | || |  ____  ____  | | \n" \
"| | |  _   _  |  | || | |_   ___  |  | || |     /  \     | |         | |  |_   _ \    | || |   .'    `.   | || | |_  _||_  _| | | \n" \
"| | |_/ | | \_|  | || |   | |_  \_|  | || |    / /\ \    | |         | |    | |_) |   | || |  /  .--.  \  | || |   \ \  / /   | | \n" \
"| |     | |      | || |   |  _|  _   | || |   / ____ \   | |         | |    |  __'.   | || |  | |    | |  | || |    \ \/ /    | | \n" \
"| |    _| |_     | || |  _| |___/ |  | || | _/ /    \ \_ | |         | |   _| |__) |  | || |  \  `--'  /  | || |    _|  |_    | | \n" \
"| |   |_____|    | || | |_________|  | || ||____|  |____|| |         | |  |_______/   | || |   `.____.'   | || |   |______|   | | \n" \
"| |              | || |              | || |              | |         | |              | || |              | || |              | | \n" \
"| '--------------' || '--------------' || '--------------' |         | '--------------' || '--------------' || '--------------' | \n" \
" '----------------'  '----------------'  '----------------'           '----------------'  '----------------'  '----------------'  \n" \
"\n" \
"\n" \
"\n" \
"\n" \
"\n"
)
    # Tron says "Tea Boy"
    text_to_speech("Tea Boy")
    # Hold the script for 2 seconds
    time.sleep(2)
    # Clear screen
    cls()
    # Reprint Tea Boy ASCII art
    print(
"\n" \
"\n" \
"\n" \
"\n" \
"\n" \
" .----------------.  .----------------.  .----------------.           .----------------.  .----------------.  .----------------.  \n" \
"| .--------------. || .--------------. || .--------------. |         | .--------------. || .--------------. || .--------------. | \n" \
"| |  _________   | || |  _________   | || |      __      | |         | |   ______     | || |     ____     | || |  ____  ____  | | \n" \
"| | |  _   _  |  | || | |_   ___  |  | || |     /  \     | |         | |  |_   _ \    | || |   .'    `.   | || | |_  _||_  _| | | \n" \
"| | |_/ | | \_|  | || |   | |_  \_|  | || |    / /\ \    | |         | |    | |_) |   | || |  /  .--.  \  | || |   \ \  / /   | | \n" \
"| |     | |      | || |   |  _|  _   | || |   / ____ \   | |         | |    |  __'.   | || |  | |    | |  | || |    \ \/ /    | | \n" \
"| |    _| |_     | || |  _| |___/ |  | || | _/ /    \ \_ | |         | |   _| |__) |  | || |  \  `--'  /  | || |    _|  |_    | | \n" \
"| |   |_____|    | || | |_________|  | || ||____|  |____|| |         | |  |_______/   | || |   `.____.'   | || |   |______|   | | \n" \
"| |              | || |              | || |              | |         | |              | || |              | || |              | | \n" \
"| '--------------' || '--------------' || '--------------' |         | '--------------' || '--------------' || '--------------' | \n" \
" '----------------'  '----------------'  '----------------'           '----------------'  '----------------'  '----------------'  \n" \
"\n" \
"\n" \
"\n" \
"\n" \
"\n"
)
    # Supplement the above with a Loading Game art whilst Tron talks.
    print(
"\n" \
"\n" \
"\n" \
" ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄           \n" \
"▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌          \n" \
"▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀           \n" \
"▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌    ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌               ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌                    \n" \
"▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌    ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌ ▄▄▄▄▄▄▄▄      ▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄           \n" \
"▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌    ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░▌▐░░░░░░░░▌     ▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌          \n" \
"▐░▌          ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌    ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌ ▀▀▀▀▀▀█░▌     ▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀           \n" \
"▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌    ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌                    \n" \
"▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄  ▄  ▄  \n" \
"▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌▐░▌▐░▌ \n" \
" ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀  ▀  ▀  \n" \
"\n" \
"\n" \
"\n"
)
    # Hold the script for 1 second
    time.sleep(1)
    # Tron warns this ain't no game
    text_to_speech("This ain't no game. This is reality for apprentices... up and down the country... You're lucky you came to University.")
    # Hold script for 2 seconds
    time.sleep(2)
    # Tron details the first quest
    text_to_speech("Its time for your very first quest... It's called... " + str(quest_numbers[player.current_quest]["name"]) + "... To complete this quest you must... " + str(quest_numbers[player.current_quest]["description"]) + "... ")
    # Hold the script for 1 second
    time.sleep(1)
    # Give name and description of current room
    text_to_speech("You're entering " + player.current_room["name"] + ". " + player.current_room["description"].replace("\n"," "))
    # Hold the script for 1 second
    time.sleep(1)
    # Tron tells apprentice to get going
    text_to_speech("Now off you go, apprentice.")
    # Clear screen
    cls()
    # Register that we have now visited Outside
    player.current_room["visited"] = True

    return

def take_player_name():
    """This function is used in the opening and is how we capture the
    name of the player. It is used in various points of tts utterance."""
    global player_name
    text_to_speech("What is your name, apprentice?")
    print("What is your name, Apprentice?")
    player_name = input("> ")
    player_name = str(normalise_input(player_name)[0])
    # Return in title case
    player_name = player_name.title()
    text_to_speech("Nice one, " + player_name + "! I'm sure we'll get along just fine.")
    return player_name

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    holding_array = []
    number_of_items = len(holding_array)

    for thing in items:
        holding_array.append(thing["name"])

    return ", ".join([str(name) for name in holding_array])


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if len(room["items"]) > 0:
        print("There is " + list_of_items(room["items"]) + " here." + "\n")
        return
    else:
        # Do nothing.
        pass

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    if len(player.inventory) > 0:
        print("You have " + list_of_items(player.inventory) + "." + "\n")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(player.current_room["menu_art"])
    print()
    print("You're in " + room["name"].upper())
    print()
    # Display room descriptions; if quest is 4 or more, print alt description, else regular one.
    if player.current_quest >= 4:
        print(room["description_alt"])
    else:
        print(room["description"])
    print()
    # Print the items in the room
    print_room_items(room)
    return

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items, room_props, room_consumables):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item_to_take in room_items:
        mass_str = ""
        if item_to_take["mass"] > 0:
            mass_str = " (" + str(item_to_take["mass"]) + " KG)"
        print("TAKE " + item_to_take["id"].upper() + " to take " + item_to_take["name"].lower() + mass_str)

    if len(room_items) > 1:
        print("TAKE ALL to take everything you can take.")

    dropable_items = 0
    for item_to_drop in inv_items:
        if item_to_drop["can_drop"]:
            dropable_items += 1
            mass_str = ""
            if item_to_drop["mass"] > 0:
                mass_str = " (" + str(item_to_drop["mass"]) + " KG)"
            print("DROP " + item_to_drop["id"].upper() + " to drop your " + item_to_drop["name"].lower() + mass_str)

    if dropable_items > 1:
        print("DROP ALL to drop everything you can drop.")

    for prop in room_props:
        print("USE " + prop["id"].upper() + " to use the " + prop["name"].lower())

    for consumable in room_consumables:
        print("CONSUME " + consumable["id"].upper() + " to consume the " + consumable["name"].lower())

    print("EXIT to quit the game.")

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    if chosen_exit in exits:
        return True
    else:
        return False


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    # Advise that player_name is global
    global player_name
    # Check if player has entered a valid exit
    if is_valid_exit(player.current_room["exits"], direction) == True:
        # If player entered a valid exit, ascertain where they are going
        destination_room = move(player.current_room["exits"], direction)
        # Check if player is on a late enough quest to access room
        if player.current_quest >= destination_room["required_current_quest_min"]:
            # Check through all items required to enter room
            for required_item in destination_room["required_items"]:
                # Check if a required item isn't in player inventory
                if required_item not in inventory:
                    print("You need to bring something else to enter " + destination_room["name"] + ", " + player_name + "!")
                    text_to_speech("You're not carrying the right thing to access " + destination_room["name"] + ". Go get it, " + player_name + "!")
                    return
            # If its a valid exit and quest and items requirements are met, migrate rooms
            player.current_room = destination_room
            # Clear the screen prior to the animation
            cls()
            if not skip_long_parts:
                # Play door opening sound effect
                set_song("door.mp3", False)
                # Display opening door animation
                print_animation(anim_door.anim, True)
                # Clear the screen following the animation
                cls()

            # Display entry art for the current room
            print(player.current_room["entry_art"])
            # Set current song playing according to room, alt song if quest is more than 4
            # TTS announce where we're going, using alt description if quest is 4 or more.
            if player.current_quest < 4:
                set_song(player.current_room["song"])
                # If they have not visited this room before and wouldn't have heard this variant of description, introduce them.
                if player.current_room["visited"] == False:
                    text_to_speech("Get excited " + player_name + ". You're entering " + player.current_room["name"] + ". " + player.current_room["description"].replace("\n"," "))
                # If they have visited this room before and would have heard this variant of description, just give name only.
                else:
                    text_to_speech("Returning to " + player.current_room["name"] + ".")
            # If quest is less than 4, just use the default room songs.
            # If quest is less than 4, just use regular description.
            else:
                set_song(player.current_room["song_alt"])
                # If they have not visited this room before and wouldn't have heard this variant of description, introduce them.
                if player.current_room["visited"] == False:
                    text_to_speech("You're back at " + player.current_room["name"] + " again, " + player_name + ". " + player.current_room["description_alt"].replace("\n"," "))
                # If they have visited this room before and would have heard this variant of description, just give name only.
                else:
                    text_to_speech("Returning to " + player.current_room["name"] + ".")
            # Register that the player has now visited this room as to prevent repeated tts descriptions should they revist.
            player.current_room["visited"] = True
            # Clear the screen after entry procedure and tts intro completed
            cls()
        # Handle if player is on too early of a quest to go into room
        else:
            print("Pay attention, " + player_name + "! You need to complete a quest to enter " + destination_room["name"] + ".")
            text_to_speech("Let's not get ahead of ourselves here " + player_name + "! You need to complete a quest to access " + destination_room["name"] + ".")
    # Handle if player enters an invalid exit
    else:
        print("You cannot go there, " + player_name + ".")
        text_to_speech("Sorry " + player_name + ", but you can't go there.")

def total_weight_carried():
    """This function returns the total weight held by the player
    based on the items currently in the inventory and their
    corresponding mass values. This can then be used to add
    and remove item masses so that the player can be prevented
    from picking up too much after taking / allowed to pick up
    more after a drop."""
    player.weight_carried = 0
    for item in player.inventory:
        player.weight_carried += item["mass"]
    return

def execute_take(item_ref):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints "You cannot take that."
    Furthermore, it will also enforce a rule such that the player cannot carry more
    than max_weight_allowed KG in their inventory at any given time.
    The max_weight_allowed variable can be altered in player.py.
    """

    global player_name

    # Obtain the initial weight being carried, based on whats in inventory.
    total_weight_carried()

    # Check if we want to take everything
    take_all = (item_ref == "all")

    missed_some = False

    # Temporary list to avoid concurrent list modification
    remove_from_room = []

    # If the item is indeed in the current room, make the move.
    for c in player.current_room["items"]:
        if take_all or (item_ref == c["id"]):
            # Checking that what the player is already carrying plus what they're about to pick
            # up would not lead to them holding more than the maximum allowed mass, max_weight_allowed.

            if weight_carried + c["mass"] <= player.max_weight_allowed:
                player.inventory.append(c)
                remove_from_room.append(c)

                # Add in the additional weight that the player is now carrying.
                player.weight_carried += c["mass"]
                if not take_all:
                    print("You've picked up " + c["name"] + ".")
                    text_to_speech("You've picked up " + c["name"] + ". " + c["description"])
                    player.current_room["items"].remove(c)
                    cls()
                    return

            # If the player will be carrying too much after they pick up their chosen item, advise.
            else:
                print ("You're carrying too much stuff, " + player_name + "! You've got to drop something or consume some stuff to get stronger...")
                text_to_speech("Sorry " + player_name + "! you're not quite strong enough to lift that... You need to drop something, or go and consume something from one of the rooms so you're strong enough.")
                cls()
                missed_some = True

                if not take_all:
                    return



    # If we were trying to take everything, output an appropriate message now.
    if take_all:
        for remove in remove_from_room:
            player.current_room["items"].remove(remove)

        if missed_some:
            print("You've taken what you can, but some things were too heavy.")
            text_to_speech("You've taken what you can, but some things were too heavy.")
            cls()
        else:
            print("You've just taken everything that you can take.")
            text_to_speech("You've just taken everything that you can take.")
            cls()
        return

    # If that item actually is not in the current room, advise player.
    print("Sorry " + player_name + ". You cannot take that.")
    text_to_speech("Sorry " + player_name + ". You cannot take that.")


def execute_drop(item_ref):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    # Obtain the initial weight being carried, based on whats in inventory.
    total_weight_carried()

    # Check if we want to drop everything
    drop_all = (item_ref == "all")

    # If the item is indeed in the inventory, make the drop.

    # Temporary list to avoid concurrent list modification
    remove_from_inventory = []

    for i in inventory:
        if i["can_drop"] and (drop_all or (item_ref == i["id"])):
            player.current_room["items"].append(i)
            remove_from_inventory.append(i)

            # Take off the additional weight that the player just dropped.
            player.weight_carried -= i["mass"]

            # If we're not trying to drop everything, say what we dropped and stop.
            if not drop_all:
                # Narrate what just happened
                print("You've just dropped " + i["name"] + ".")
                text_to_speech("You've just dropped " + i["name"] + ".")
                player.inventory.remove(i)
                cls()
                return

    # If we were trying to drop everything, output an appropriate message now.
    if drop_all:
        for remove in remove_from_inventory:
            inventory.remove(remove)
        print("You've just dropped everything that you can drop.")
        text_to_speech("You've just dropped everything that you can drop.")
        cls()
        return

    # If that item actually is not in the inventory, advise player.
    print("Sorry " + player_name + ". You cannot drop that.")
    text_to_speech("Sorry " + player_name + ". You cannot drop that.")

def execute_use(prop_ref):
    """This function takes an prop id as an argument and executes the prop's
    use_action function. However, if there is no such prop in the room, this
    function prints "You cannot use that."
    """

    # If the prop is indeed in the room and the player has met the requirement to use the item, use it.

    for prop in player.current_room["props"]:
        if (prop_ref == prop["id"]):
            if eval(prop["use_condition"]):

                # execute the use function of the prop
                exec(prop["use_action"])

                # Narrate and show what just happened
                print("You've just used the " + prop["name"] + ".")
                text_to_speech("You've just used the " + prop["name"] + ". " + prop["use_comment"] + ".")
                cls()

            else:

                # If the use condition is not met, advise player.
                print("You cannot use that right now, " + player_name + ". Check you're carrying the right things?")
                text_to_speech("You cannot use that right now, " + player_name + ". make sure you're carrying what you need?")
                cls()

            return

    # If that prop actually is not in the room, advise player.

    print("Sorry " + player_name + ". You cannot use that.")
    text_to_speech("Sorry " + player_name + ". You cannot use that.")

def execute_consume(consumable_ref):
    """This function takes an consumable id as an argument and executes the
    consumable's consume_action function. However, if there is no such
    consumable in the room, this function prints "You cannot consume that."
    """
    # If the consumable is indeed in the room, consume it.

    for consumable in player.current_room["consumables"]:
        if (consumable_ref == consumable["id"]):
            # eval the use function of the prop
            eval(consumable["consume_action"])

            # Narrate and show what just happened
            print("You've just consumed the " + consumable["name"] + ".")
            text_to_speech("You've just consumed the " + consumable["name"] + ". " + consumable["consume_comment"] + ".")
            cls()

            # Remove it from the room
            player.current_room["consumables"].remove(consumable)

            return

    # If that prop actually is not in the room, advise player.
    print("Sorry " + player_name + ". You cannot consume that.")
    text_to_speech("Sorry " + player_name + ". You cannot consume that. It doesn't exist.")

def add_strength(kg):
    """This function is used for rooms which contain consumables.
    Consumables are set to increment the max_weight_allowed stat
    in player.py, for ease of execution, this function takes an
    argument denoting how many KG we want to increase the player
    strength by. It is referenced unnder consume_action in map.py
    and subsequently evaluated here."""
    player.max_weight_allowed += kg

def execute_exit():
    """This function asks the player if they really want to exit the game.
    If they answer yes, exit. Otherwise, continue the game."""

    print("Are you sure you want to quit the game? Your progress will NOT be saved!")
    text_to_speech("You're quitting early?")
    choice = normalise_input(input("If you're sure, type YES: "))
    if choice == ["yes"]:
        stop_and_exit()
    else:
        text_to_speech("I didn't think so!")

def execute_command(command):
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
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("Use what?")

    elif command[0] == "consume":
        if len(command) > 1:
            execute_consume(command[1])
        else:
            print("Consume what?")

    elif command[0] == "exit":
        execute_exit()

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items, room_props, room_consumables):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items, room_props, room_consumables)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return map.rooms[exits[direction]]

def text_to_speech(msg):
    """This function takes an argument, msg, and speaks what it says"""
    global tts_engine
    global audio_supported

    if skip_long_parts:
        return

    if not audio_supported:
        return

    try:
        # Reduce volume of music
        pygame.mixer.music.set_volume(0.33)
        tts_engine = pyttsx3.init()
        tts_engine.setProperty('rate',180)  #180 words per minute
        tts_engine.setProperty('volume',0.9)
        tts_engine.say(str(msg))
        tts_engine.runAndWait()
        # Return volume of music to default
        pygame.mixer.music.set_volume(1)
    # Exit by Ctrl+C
    except KeyboardInterrupt:
        stop_and_exit()
    except:
        audio_supported = False
        no_audio_message()

def set_song(file, loop=True):
    global audio_supported
    if not audio_supported:
        return
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("music/" + file)
        pygame.mixer.music.set_volume(1)
        if loop:
            # Argument of -1 repeats music indefinetly.
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play()
    # Exit by Ctrl+C
    except KeyboardInterrupt:
        stop_and_exit()
    except:
        audio_supported = False
        no_audio_message()

def quest_completed(quest):
    """ This function will take the quest the player is on, obtain its
    criteria and check to see whether the player has met it. If they have,
    it will return a value to tell main game loop to move to the next quest
    """
    global player_name
    # Checking to see whether its time to trigger endgame function (ie coming to the end of final quest?)
    if player.current_quest + 1 == 6 and player.current_room == map.rooms["Pandora"]:
        game_won()
        time.sleep(1)
    # Checking if the criteria of the current quest has been met
    if eval(quest_numbers[quest]["criteria"]):
        if not skip_long_parts:
            print("""
   ___                         _        ____                               _          _                _   _
  / _ \   _   _    ___   ___  | |_     / ___|   ___    _ __ ___    _ __   | |   ___  | |_    ___    __| | | |
 | | | | | | | |  / _ \ / __| | __|   | |      / _ \  | '_ ` _ \  | '_ \  | |  / _ \ | __|  / _ \  / _` | | |
 | |_| | | |_| | |  __/ \__ \ | |_    | |___  | (_) | | | | | | | | |_) | | | |  __/ | |_  |  __/ | (_| | |_|
  \__\_\  \__,_|  \___| |___/  \__|    \____|  \___/  |_| |_| |_| | .__/  |_|  \___|  \__|  \___|  \__,_| (_)
                                                                  |_|
"""
            )
            print()
            print("Well Done, " + player_name + "! You've completed " + str(quest_numbers[quest]["name"]) + "! \n")
            text_to_speech("Well Done, " + player_name + "! You've completed " + str(quest_numbers[quest]["name"]) + "!")
            time.sleep(3)
        cls()
        # Increment the current quest by one
        player.current_quest += 1
        # Checking if we have now reached quest 6 (ie: final quest + 1), launching credits before loop crashes.
        if player.current_quest == 6:
            end_credits()
            # Don't try to introduce the next quest in the main loop!
            return False
        # Resetting all visited values for all rooms to False if just gone to quest 4 as songs and descriptions have changed.
        # Also adding hammer to The Security Suite so the player can go and fetch it.
        if player.current_quest == 4:
            map.rooms["Security"]["items"].append(item_hammer)
            for key in rooms:
                rooms[str(key)]["visited"] = False
        return True
    else:
        return False

def give_sword():
    """This function is executed just as we enter pandora on finale quest."""
    global player_name
    # Read player's input
    text_to_speech("What? Do you want your boss to die on the first day " + player_name + "? Call his name to throw him the sword!")
    print("Say Kirill's name to throw him the sword, quick!")
    shout = input("> ")
    # Normalise the input
    normalised_shout = normalise_input(shout)
    if normalised_shout == ["kirill"]:
        text_to_speech("Nice one " + player_name + ". You throw Kirill the sword with all your might and he terminates the bear. You've saved your boss. Clearly " + player_name + " is looking for a promotion?")
        return
    elif normalised_shout == ["kiril"]:
        text_to_speech("Kirill has got two letter L's in his name! Say it properly " + player_name + "!")
        give_sword()
    elif normalised_shout == ["kirrill"]:
        text_to_speech("That's not how you spell his name! Say it properly " + player_name + "!")
        give_sword()
    elif normalised_shout == ["kirril"]:
        text_to_speech("That's not how you spell his name! Say it properly " + player_name + "!")
        give_sword()
    else:
        give_sword()

def print_quest_info():
    """ This function prints the current quest information, used in main loop """
    print("Your current quest is:")
    print("\n" + str(quest_numbers[player.current_quest]["name_art"]))
    print("Quest Description: " + str(quest_numbers[player.current_quest]["description"]) + "\n")

def print_quest_name_only():
    """ This function prints the name of the current quest, used in main loop """
    print("\n" + str(quest_numbers[player.current_quest]["name_art"]))


def game_won():
    """ This function simply declares what to do when the player does what
    is necessary to win the game ie current_quest = 6"""

    print_animation(anim_bear.anim, True)
    time.sleep(1)
    give_sword()
    cls()
    time.sleep(1)
    return
    # Note, end credits are triggered by quest_completed() when current_quest == 6
    # after this game_won() has been executed by that function too.

def end_credits():
    # End credit scene to go here, similar to opening()
    cls()
    set_song("credits.mp3")
    if not skip_long_parts:
        time.sleep(2)
        for credits_screen in credits.credits:
            print_credits_scroll_left(credits_screen)
        time.sleep(1)
        cls()
    print("Thank you for playing...")
    text_to_speech("Thank you for playing...")
    print(
        "\n" \
        " .----------------.  .----------------.  .----------------.           .----------------.  .----------------.  .----------------.  \n" \
        "| .--------------. || .--------------. || .--------------. |         | .--------------. || .--------------. || .--------------. | \n" \
        "| |  _________   | || |  _________   | || |      __      | |         | |   ______     | || |     ____     | || |  ____  ____  | | \n" \
        "| | |  _   _  |  | || | |_   ___  |  | || |     /  \     | |         | |  |_   _ \    | || |   .'    `.   | || | |_  _||_  _| | | \n" \
        "| | |_/ | | \_|  | || |   | |_  \_|  | || |    / /\ \    | |         | |    | |_) |   | || |  /  .--.  \  | || |   \ \  / /   | | \n" \
        "| |     | |      | || |   |  _|  _   | || |   / ____ \   | |         | |    |  __'.   | || |  | |    | |  | || |    \ \/ /    | | \n" \
        "| |    _| |_     | || |  _| |___/ |  | || | _/ /    \ \_ | |         | |   _| |__) |  | || |  \  `--'  /  | || |    _|  |_    | | \n" \
        "| |   |_____|    | || | |_________|  | || ||____|  |____|| |         | |  |_______/   | || |   `.____.'   | || |   |______|   | | \n" \
        "| |              | || |              | || |              | |         | |              | || |              | || |              | | \n" \
        "| '--------------' || '--------------' || '--------------' |         | '--------------' || '--------------' || '--------------' | \n" \
        " '----------------'  '----------------'  '----------------'           '----------------'  '----------------'  '----------------'  \n" \
        "\n"
    )
    text_to_speech("Tea boy.")
    time.sleep(4)
    print()
    print("Play again? ")
    choice = normalise_input(input("Type YES to play again: "))
    if choice == ["yes"]:
        reset_game()
        return
    else:
        text_to_speech("Play again another time!")
        stop_and_exit()
    # Remember to place an indefinite sleep ie: "Play again? / Exit" at the end to prevent
    # game from returning to loop and crashing on final quest + 1 (which doesn't exist)

def test_unicode_support():
    """This function prints a short test string of unicode characters used
    in this game. If it fails, the terminal doesn't support them."""
    try:
        print("Testing terminal unicode support: ░█║")
    except:
        print()
        print("""This game requires a terminal that supports unicode!
We recommend using cmd (Command Prompt) on Windows.""")
        quit()

def cls():
    """This function will simply clear the screen with 500 linebreaks"""
    print("\n" * 500)

def crash_message(error_msg=""):
    if len(error_msg) > 0:
        print("\n\nAn error ocurred:\n" + error_msg)
    else:
        print("An unknown error ocurred.")
    print("\nThe game encountered an error and was forced to exit. Your progress was not saved.")
    time.sleep(3)
    stop_and_exit()

def no_audio_message():
    print("""WARNING: Your system does not seem to support audio!
This game relies heavily on text-to-speech audio.
The game will continue to run, but you won't get the full experience.""")
    time.sleep(5)

def stop_and_exit():
    """This function performs any necessary cleanup, prints an exit message
    and then quits."""
    print("\nExiting! This may take a few seconds.")
    time.sleep(1)
    os._exit(0)

def reset_game():
    """This function reloads all the files defining the game state in order to
    start the game from scratch."""
    cls()
    set_song("outside.mp3")
    importlib.reload(map)
    importlib.reload(player)


# This is the entry point of our program
def main():
    global skip_long_parts

    # Check for terminal compatibility before doing anything else
    test_unicode_support()

    # Check if we want to skip long parts
    if len(sys.argv) > 1:
        if(str(sys.argv[1]) == "fast"):
            skip_long_parts = True

    try:
        # Before we jump into the main loop, we need to introduce the player.
        opening()

        # Main game loop
        while True:

            print_quest_info()
            print("You're currently strong enough to carry: " + str(player.max_weight_allowed) + " kilograms! \n")

            # Display game status (room description, inventory etc.) and narrate the name and description
            print_room(player.current_room)
            print_inventory_items(inventory)

            # Narration prompt for the user to select a choice
            text_to_speech("What would you like to do next?")

            # Show the menu with possible actions and ask the player
            command = menu(player.current_room["exits"], player.current_room["items"], player.inventory, player.current_room["props"], player.current_room["consumables"])

            # Clearing contents of screen
            cls()

            # Execute the player's command
            execute_command(command)

            # Check to see if player has done all requisite things to complete current quest, incrementing the quest number automatically if so.
            if quest_completed(player.current_quest) == True:
                print("Your upcoming quest is...")
                print_quest_name_only()
                text_to_speech("Now its time for your next quest. It's called... " + str(quest_numbers[player.current_quest]["name"]) + "... To complete this quest you must... " + str(quest_numbers[player.current_quest]["description"]) + "... ")
                cls()

            # If there is more to do, just continue with the loop

    # Exit by Ctrl+C
    except KeyboardInterrupt:
        stop_and_exit()

    # Any other exception
    except Exception as e:
        err_string = type(e).__name__
        if len(str(e)) > 0:
            err_string += ": " + str(e)
        crash_message(err_string)

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
