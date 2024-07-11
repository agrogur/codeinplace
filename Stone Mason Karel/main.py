from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    build_column()
    build_column()
    build_column()
    build_column()

def build_column():
    turn_left()
    while front_is_clear():
     put_beeper()
     move()
    
    while front_is_blocked(): 
     put_beeper()
     turn_around()

    move()
    move()
    move()
    move()

    turn_left()
    
    if front_is_clear():
     move()
     move()
     move()
     move()
  
      
def turn_around():
      turn_left()
      turn_left()
      
if __name__ == '__main__':
    main()