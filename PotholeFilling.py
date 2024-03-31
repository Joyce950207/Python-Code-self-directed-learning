"""
File: PotholeFilling.py
Name: Joyce
--------------------------
This program shows karel filling 3
potholes. Learning the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is at the upper left of the pothole, facing East.
    post-condition:Karel is in the pothole, facing South.
    """
    for i in range(3):
        go_in()
        move()
        go_out()
def go_in():
    """
    pre-condition:Karel is at the upper left, facing East.
    post-condition:Karel is in the pothole, facing South.
    """
    move()
    turn_right()
def go_out():
    """
    pre-condition:Karel is in the pothole, facing South.
    post-condition:Karel is at the upper left, facing East.
     """
    put_99_beepers()
    turn_around()
    move()
    turn_right()
    move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
def put_99_beepers():
    for i in range(99):
        put_beeper()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
