from tkinter import *
import math
import random
import time

canvas_width = 800
canvas_height = 600

window = Tk()
canvas = Canvas(window, height=canvas_height, width=canvas_width, background="black")
canvas.pack()

window.update()
time.sleep(0.3)

def Firework():
	# Create a random color
	r = random.randrange(0, 255)
	g = random.randrange(0, 255)
	b = random.randrange(0, 255)
	rgb = "#{:02x}{:02x}{:02x}".format(r, g, b)
	
	# Create a random x, y position for the firework center point
	x = random.randrange(150, canvas_width - 150)
	y = random.randrange(150, int(canvas_height * 2 / 3))
	
	# Create a line every 15° in a circle from this center point
	for degree in range(0, 360, 15):
		hypotenuse = 100
		angle = math.radians(degree)
		opposite = hypotenuse * math.sin(angle)
		adjacent = hypotenuse * math.cos(angle)
		
		x2 = x + adjacent
		y2 = y - opposite
		
		canvas.create_line(x, y, x2, y2, fill=rgb)

for i in range(10):
	Firework()
	time.sleep(0.3)
	window.update()

window.mainloop()
