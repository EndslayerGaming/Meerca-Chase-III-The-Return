# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import turtle
import time
import random

delay = 0.1

wn = turtle.Screen()
wn.title("Meerca Chase III: The Return")
wn.bgcolor("#1f88c9")
wn.setup(width=600, height=700)
wn.tracer(0) # turns off screen updates

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.directon = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake Body
segments = []

# Functions
def go_up():
    head.directon = "up"

def go_down():
    head.directon = "down"

def go_left():
    head.directon = "left"

def go_right():
    head.directon = "right"

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


def move():
    if head.directon == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.directon == "down":
        y = head.ycor()
        head.sety(y + -20)

    if head.directon == "left":
        x = head.xcor()
        head.setx(x + -20)

    if head.directon == "right":
        x = head.xcor()
        head.setx(x + 20)

# Main game loop
while True:
    wn.update()

    #Check for food collison
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-299, 299)
        y = random.randint(-299, 299)
        food.goto(x, y)

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y - 5)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y - 10)

    move()

    time.sleep(delay)

wn.mainloop()
