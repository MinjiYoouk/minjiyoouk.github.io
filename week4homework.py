# import required modules
from tkinter import *
from PIL import Image, ImageDraw, ImageTk
import random
import math

# Create a new Tkinter window
app = Tk()
app.title("Heptagon with Pentagon and Hexagon")
app.geometry("400x400")

# Create a canvas widget inside the window
canvas = Canvas(app, bg="white")
canvas.pack(fill=BOTH, expand=1)

# Create a blank image of size 400x400 pixels and fill it with a white background
myImage = Image.new("RGB", (400, 400), (255, 255, 255))

# Create a drawing context for the image
drawingContext = ImageDraw.Draw(myImage)

# Define the number of sides for the heptagon (7 sides)
num_sides = 7

# Calculate the coordinates for the center of the image
center_x = myImage.width // 2
center_y = myImage.height // 2

# Calculate the radius of the heptagon
radius = min(myImage.width, myImage.height) // 2 - 10

# Calculate the angle step for each side of the heptagon
angle_step = 2 * math.pi / num_sides

# Create a list of random colors for the heptagon edges
heptagon_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(num_sides)]

# Set the line width for the heptagon edges
heptagon_line_width = 6

# Draw the heptagon by connecting its vertices with thicker edges
for i in range(num_sides):
    start_x = center_x + int(radius * math.cos(i * angle_step))
    start_y = center_y + int(radius * math.sin(i * angle_step))
    end_x = center_x + int(radius * math.cos((i + 1) * angle_step))
    end_y = center_y + int(radius * math.sin((i + 1) * angle_step))
    edge_color = heptagon_colors[i]
    drawingContext.line([(start_x, start_y), (end_x, end_y)], fill=edge_color, width=heptagon_line_width)

# Define the number of sides for the pentagon (5 sides)
num_pentagon_sides = 5

# Calculate the radius of the pentagon
pentagon_radius = radius / 3  # 1/3 of the heptagon radius

# Create a list of random colors for the pentagon edges
pentagon_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(num_pentagon_sides)]

# Set the line width for the pentagon edges
pentagon_line_width = 3

# Calculate the angle step for each side of the pentagon
pentagon_angle_step = 2 * math.pi / num_pentagon_sides

# Draw the pentagon inside the heptagon
for i in range(num_pentagon_sides):
    start_x = center_x + int(pentagon_radius * math.cos(i * pentagon_angle_step + angle_step / 2))
    start_y = center_y + int(pentagon_radius * math.sin(i * pentagon_angle_step + angle_step / 2))
    end_x = center_x + int(pentagon_radius * math.cos((i + 1) * pentagon_angle_step + angle_step / 2))
    end_y = center_y + int(pentagon_radius * math.sin((i + 1) * pentagon_angle_step + angle_step / 2))
    edge_color = pentagon_colors[i]
    drawingContext.line([(start_x, start_y), (end_x, end_y)], fill=edge_color, width=pentagon_line_width)

# Define the number of sides for the hexagon (6 sides)
num_hexagon_sides = 6

# Calculate the radius of the hexagon (1/2 of the heptagon radius)
hexagon_radius = radius / 2

# Create a list of random colors for the hexagon edges
hexagon_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(num_hexagon_sides)]

# Set the line width for the hexagon edges
hexagon_line_width = 3

# Calculate the angle step for each side of the hexagon
hexagon_angle_step = 2 * math.pi / num_hexagon_sides

# Draw the hexagon inside the heptagon
for i in range(num_hexagon_sides):
    start_x = center_x + int(hexagon_radius * math.cos(i * hexagon_angle_step + angle_step / 2))
    start_y = center_y + int(hexagon_radius * math.sin(i * hexagon_angle_step + angle_step / 2))
    end_x = center_x + int(hexagon_radius * math.cos((i + 1) * hexagon_angle_step + angle_step / 2))
    end_y = center_y + int(hexagon_radius * math.sin((i + 1) * hexagon_angle_step + angle_step / 2))
    edge_color = hexagon_colors[i]
    drawingContext.line([(start_x, start_y), (end_x, end_y)], fill=edge_color, width=hexagon_line_width)

# Convert the PIL image to a Tkinter PhotoImage
myImage = ImageTk.PhotoImage(myImage)

# Draw the Tkinter PhotoImage on the canvas at position (0, 0)
canvas.create_image(0, 0, image=myImage, anchor="nw")

# Start the Tkinter main loop
app.mainloop()
