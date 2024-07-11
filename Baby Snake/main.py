from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    dx = SIZE
    dy = 0

    # Create player
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, "blue")

    # Create the goal rectangle
    goal_x = 360
    goal_y = 360
    goal = canvas.create_rectangle(goal_x, goal_y, goal_x + SIZE, goal_y + SIZE, "red")

    direction = 'Right'
    count = 0

    while True:
        # Handle Key Press
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft' and direction != 'Right':
            direction = 'Left'
        elif key == 'ArrowRight' and direction != 'Left':
            direction = 'Right'
        elif key == 'ArrowUp' and direction != 'Down':
            direction = 'Up'
        elif key == 'ArrowDown' and direction != 'Up':
            direction = 'Down'

        # Update the player's position
        if direction == 'Left':
            dx = -SIZE
            dy = 0
        elif direction == 'Right':
            dx = SIZE
            dy = 0
        elif direction == 'Up':
            dx = 0
            dy = -SIZE
        else:  # direction == 'Down'
            dx = 0
            dy = SIZE

        # Move the player
        canvas.move(player, dx, dy)

        # Check for out of bounds
        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)
        if player_x < 0 or player_x >= CANVAS_WIDTH or player_y < 0 or player_y >= CANVAS_HEIGHT:
            break

        # Detecting collisions
        goal_x = canvas.get_left_x(goal)
        goal_y = canvas.get_top_y(goal)
        goal_right = goal_x + SIZE
        goal_bottom = goal_y + SIZE

        if (
            player_x < goal_right
            and player_x + SIZE > goal_x
            and player_y < goal_bottom
            and player_y + SIZE > goal_y
        ):
            move_goal(canvas, goal)
            count += 1

        # Print points
        text_obj = canvas.create_text(1, CANVAS_HEIGHT - 13, text=f"{count} points", anchor='sw')

        # Sleep
        time.sleep(DELAY)

        # Delete old points text
        canvas.delete(text_obj)

    # Show result
    result = f"Your Score is : {str(count)}"
    canvas.create_text(10, CANVAS_HEIGHT - 50, 'Game Over', color='red', anchor='sw')
    canvas.create_text(10, CANVAS_HEIGHT - 30, result, color='blue', anchor='sw')

# Move the goal to a new location
def move_goal(canvas, goal):
    goal_x = random.randint(0, CANVAS_WIDTH // SIZE - 1) * SIZE
    goal_y = random.randint(0, CANVAS_HEIGHT // SIZE - 1) * SIZE
    canvas.moveto(goal, goal_x, goal_y)

if __name__ == '__main__':
    main()

