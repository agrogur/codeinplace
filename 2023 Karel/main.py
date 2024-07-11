from karel.stanfordkarel import *

"""
File: 2021.py
--------------------
When you finish writing this file, Karel should be able to 
place 20 beepers, then 23 beepers, and end facing East to 
the right of the 23 beepers.
"""

def main():
    # Place 20 beepers in a row
    for i in range(20):
     put_beeper()
    move()
    # Place 23 beepers in a row 
    for i in range(23):
     put_beeper()
    move()
    

if __name__ == '__main__':
    main()