from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    while front_is_clear():
      put_beeper_line()
      reset()
      moveup()
    
   
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    


def put_beeper_line():
   put_beeper()
   while front_is_clear():
      move()
      put_beeper()
   
def reset():
   turn_left()
   turn_left()
   while front_is_clear():
      move()

   turn_left()
   turn_left()

def moveup():
   turn_left()
   move()
   if front_is_clear():
    turn_right()
   else:
    turn_left()
    turn_left()
    turn_left()
    while front_is_clear():
          put_beeper()
          move()
    put_beeper()  
 
  



def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()