import random
import math
from turtle import *

def number(x,y):
	global i
	global step
	random_number = random.randint(x,y)
	i.append(random_number)
	if len(i) == step:
		move(i)
def all_steps(num):
	for k in range(num):
		number(1,4)
def move(c):
	speed(0)
	for a in c:
		if (a == 1):
			setheading(0)
			forward(1)
		elif (a == 2):
			setheading(270)
			forward(1)
		elif (a == 3):
			setheading(180)
			forward(1)
		elif (a == 4):
			setheading(90)
			forward(1)
	setheading(0)
def growing_numbers(N):
	initial_position = position()
	print(initial_position)
	all_steps(N)
	final_position = position()
	print(final_position)
	total_distance_taken = math.sqrt((final_position[0]-initial_position[0])**2 + (final_position[1]-initial_position[1])**2)
	print(total_distance_taken, "When step goes to infinity distance approaches to square-root of step")
i = []
step = int(input("Please give me a step number for me to move that much: "))
shape("turtle")
bgcolor("turquoise")
color("green")
growing_numbers(step)
exitonclick()
