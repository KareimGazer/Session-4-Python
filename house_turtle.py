import turtle

def draw_square(t, side_length):
    for _ in range(4):
        t.forward(side_length)
        t.left(90)

def draw_circle(t, radius):
    t.circle(radius)

def draw_rectangle(t, length, width):
    for _ in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)

def draw_star(t):
    for _ in range(5):
        t.forward(50)
        t.right(144)

def draw_house(body_side_length, circular_window_radius, rectangular_door_length, rectangular_door_width):
    """
    Draws a house with a square body, two circular windows, and a rectangular door,
    surrounded by stars above the square representing the house, using the previously defined functions.
    
    Args:
        body_side_length (float): Side length of the square body of the house.
        circular_window_radius (float): Radius of the circular windows.
        rectangular_door_length (float): Length of the rectangular door.
        rectangular_door_width (float): Width of the rectangular door.
    """

    # Create the turtle screen
    screen = turtle.Screen()
    screen.title("House with Stars")
    
    # Create a turtle object
    t = turtle.Turtle()
    t.speed(3)  # Set drawing speed

    # Draw the house body
    t.penup()
    t.goto(-body_side_length / 2, -body_side_length / 2)
    t.pendown()
    draw_square(t, body_side_length)

    # Draw the first circular window (left)
    t.penup()
    t.goto(-body_side_length / 4, body_side_length / 4 - circular_window_radius)
    t.pendown()
    draw_circle(t, circular_window_radius)

    # Draw the second circular window (right)
    t.penup()
    t.goto(body_side_length / 4, body_side_length / 4 - circular_window_radius)
    t.pendown()
    draw_circle(t, circular_window_radius)

    # Draw the rectangular door
    t.penup()
    t.goto(-rectangular_door_length / 2, -body_side_length / 2)
    t.pendown()
    draw_rectangle(t, rectangular_door_length, rectangular_door_width)

    # Draw stars above the house
    star_positions = [(-150, 150), (-50, 180), (50, 180), (150, 150), (0, 220)]
    for x, y in star_positions:
        t.penup()
        t.goto(x, y)
        t.pendown()
        draw_star(t)

    # Wait for the user to close the window
    screen.mainloop()

# Example usage
draw_house(200, 30, 50, 80)
