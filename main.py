import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)  # Set screen size

user_bet = screen.textinput("Make your bet", "Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = -100
turtles = []

# Create turtles
for color in colors:
    racer = Turtle()
    racer.shape("turtle")
    racer.penup()
    racer.goto(-230, y_position)  # Starting position
    racer.color(color)
    y_position += 50
    turtles.append(racer)

race_on = False
if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 210:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won!")
            else:
                print(f"You lost! The winning turtle is {winning_color}.")
            race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
