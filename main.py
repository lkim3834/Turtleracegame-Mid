
# Turtle Racing Game

# have to know forward() : --->  , backward() : <---
# what if we want to go to the different way? left() and right(). Inside the parameters, you're going to put how many degrees you're going to turn
from turtle import * 
from random import randint 

# Track Construction
# create a turtle
track = Turtle()
# hide the turtle
track.penup()
track.hideturtle()
# fastest speed is 0 
track.speed(0)

# the Outer Track 
track.goto(0, -260)
track.pendown()

track.color("black", "pink")
track.begin_fill()
# draw circle of radius 
# 270 pixel
track.circle(270)
track.end_fill()

# inner grass
track.penup()
track.goto(0, -100)
track.pendown()
track.color("black", "green")
track.begin_fill()
track.circle(110)
track.end_fill()

#finish Line
track.right(90)
track.forward(160)
track.penup()

# t1 (lane1 racer)
t1 = Turtle()
t1.color("purple")
t1.shape("turtle")
# penup because we want to place the turtle 
t1.penup()
t1.goto(0,-120)
t1.pendown()

# t2 (lane2 racer)
t2 = Turtle()
t2.color("green")
t2.shape("turtle")
# penup because we want to place the turtle 
t2.penup()
t2.goto(0,-160)
t2.pendown()

# t3 (lane3 racer)
t3 = Turtle()
t3.color("black")
t3.shape("turtle")
# penup because we want to place the turtle 
t3.penup()
t3.goto(0,-200)
t3.pendown()


# t4 (lane3 racer)
t4 = Turtle()
t4.color("red")
t4.shape("turtle")
# penup because we want to place the turtle 
t4.penup()
t4.goto(0,-240)
t4.pendown()

# Race Time
for i in range(118):
  # randint integer will be the speed
  t1.circle(130, randint(1,5))
  t2.circle(170, randint(1,5))
  t3.circle(210, randint(1,5))
  t4.circle(250, randint(1,5))

