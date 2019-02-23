#!/usr/bin/python3
# coding=utf-8

import time
import base64
import sys
import anim_bear
import anim_door

# Border characters - TL, T, TR, R, BR, B, BL, L
anim_border = "╔═╗║╝═╚║"
    
def print_animation_frame(frame, border):
    """This function takes a frame (a list of strings) and prints them in a
    rectangular frame."""

    global anim_border

    # Compute the frame width
    anim_width = 0
    for row in frame:
        if len(row) > anim_width:
            anim_width = len(row)

    # Clear the screen
    frame_text = "\n" * 300

    # Add the top border
    if border:
        frame_text += " " + anim_border[0] + (anim_border[1] * anim_width) + anim_border[2] + "\n"
    
    # Add each row
    for row in frame:
        # Add a small gap
        frame_text += " "

        # Add left border
        if border:
            frame_text += anim_border[7]

        # Add row, padded to correct width
        frame_text += row
        if len(row) < anim_width:
            frame_text += " " * (anim_width - len(row))

        # Add right border
        if border:
            frame_text += anim_border[3]

        # Add a line break
        frame_text += "\n"

    # Add the bottom border
    if border:
        frame_text += " " + anim_border[6] + (anim_border[5] * anim_width) + anim_border[4] + "\n"

    # Print everything at once.
    # Using stdout doesn't add a newline afterwards, preventing jitter.
    sys.stdout.write(frame_text)

def print_animation(anim, border):
    """This function takes an animation object and prints its frames in a
    rectangular frame at a given frame rate (frames per second)"""

    # Predelay of half a second
    time.sleep(0.5)
    
    # Compute delay time
    rate = anim["rate"]
    if rate < 0.2:
       rate = 0.2
    anim_delay = 1.0/rate

    # Print each frame at the specified rate (approximate)
    for loop_number in range(0,anim["repeat"]):
        for frame_number in anim["order"]:
            print_animation_frame(anim["frames"][frame_number], border)
            time.sleep(anim_delay)

def print_credits_scroll_left(lines):
    """This function takes a list of credits strings and prints them to the
    screen, then scrolls them off to the left."""

    margin = 8

    # Compute the width of the whole credits list
    credits_width = 0
    for line in lines:
        if len(line) > credits_width:
            credits_width = len(line)
    
    lines_padded = []
    for line in lines:
        line_offset = (credits_width - len(line)) // 2
        lines_padded.append(" " * line_offset + line)

    time.sleep(1)
    for frame in range(0, len(lines)+1):
        credits_text = "\n" * 300
        for linenum in range(0, len(lines)):
            if linenum >= frame:
                credits_text += "\n"
            else:
                credits_text += " " * margin + lines_padded[linenum] + "\n"
            credits_text += "\n"
        credits_text += "\n\n"
        sys.stdout.write(credits_text)
        time.sleep(0.25)

    time.sleep(3)
    for frame in range(0, credits_width + margin + 1):
        credits_text = "\n" * 300
        for linenum in range(0, len(lines)):
            if len(lines_padded[linenum]) + margin - frame <= 0:
                credits_text += "\n"
            else:
                credits_text += (" " * margin + lines_padded[linenum])[frame:] + "\n"
            credits_text += "\n"
        credits_text += "\n\n"
        sys.stdout.write(credits_text)
        time.sleep(0.05)
    time.sleep(1)