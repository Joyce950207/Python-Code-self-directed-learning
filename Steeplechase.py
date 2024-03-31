"""
File: Steeplechase.py
Name: Joyce
---------------------------------

"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """


    for i in range(95):
        if front_is_clear():
            move()
        else:
            jump()
            cross()
            down()
            turn_left()

def jump():
    turn_left()
    while not right_is_clear():
              move()



def cross():
    turn_right()
    move()

def down():
    turn_right()
    while front_is_clear():
          move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
 execute_karel_task(main)
