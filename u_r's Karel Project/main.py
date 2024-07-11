from karel.stanfordkarel import *

# The problem you need to solve is to get Karel to collect the diamond.
# The diamond, represented by a beeper, is located just inside the store.
# Your task is to guide Karel to pick up the diamond and return to its initial position.

def main():
    for i in range(5):
        move()  # Karel moves 5 steps forward
    turn_right()  # Karel turns right
    for u in range(4):
        move()  # Karel moves 3 steps forward
    turn_right()  # Karel turns right
    
    for j in range(3):
        move()  # Karel moves 3 steps forward
    pick_beeper()  # Karel picks up the beeper
    turn_around()  # Karel turns around
   
    for k in range(3):
        move()  # Karel moves 3 steps forward
    turn_left()  # Karel turns left
    for t in range(4):
        move()  # Karel moves 4 steps forward
    turn_left()  # Karel turns left
    for q in range(5):
        move()  # Karel moves 5 steps forward
    turn_left()  # Karel turns left

def turn_right():
    turn_left()  
    turn_left()  
    turn_left() 
    
def turn_around():
    turn_left()  
    turn_left()
    
# Don't change this code
if __name__ == '__main__':
    main()