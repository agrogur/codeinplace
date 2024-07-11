from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def modify_shapes(canvas):
    # Delete existing shapes
    canvas.clear()

    # Create modified shapes
    rect = canvas.create_rectangle(50, 50, 150, 150, color='yellow')
    oval = canvas.create_oval(100, 100, 300, 300, color='purple')
    line = canvas.create_line(50, 200, 200, 350, color='orange')
    text = canvas.create_text(200, 50, text='Hello again!', font='Arial', font_size=25, color='black')

    # Create an image with size
    image = canvas.create_image_with_size(100, 200, 200, 200, "ladybird.jpg")


    # Display the modified shapes
    canvas.wait_for_click()

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # Create initial shapes
    rect = canvas.create_rectangle(100, 100, 200, 200, color='orange')
    oval = canvas.create_oval(50, 50, 150, 150, color='green')
    line = canvas.create_line(50, 200, 150, 300, color='black')
    text = canvas.create_text(50, 350, text='Hello!', font='Arial', font_size=20, color='black')

    # Create a new rectangle
    rect = canvas.create_rectangle(250, 100, 350, 200, color='blue')

    # Create a new image
    image = canvas.create_image(200, 250, "ladybird.jpg")

    
    # Get the leftmost x coordinate of the rectangle
    left_x = canvas.get_left_x(rect)
    print("Leftmost x coordinate:", left_x)

    # Wait for a click to trigger shape modification
    canvas.wait_for_click()

    # Modify the shapes
    modify_shapes(canvas)

if __name__ == '__main__':
    main()
