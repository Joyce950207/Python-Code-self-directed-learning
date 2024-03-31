"""
File: MoveToTheEnd.py
Name: Joyce
------------------------
This file shows how to use while loop
to walk to the end of a certain 
row in Karel world
"""

from karel.stanfordkarel import *

def main():
     """
    Karel will move to the end of the first Street in any world
    """
    while front_is_clear():
        move()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
