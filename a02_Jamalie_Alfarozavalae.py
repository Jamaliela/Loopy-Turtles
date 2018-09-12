######################################################################
# Author: Elaheh Jamali, Emely Zavala
# Username: Jamalie, Alfarozavalae

# Assignment: A02: Loopy Turtles
# Purpose: To very simply demonstrate the turtle library to demo shapes
######################################################################

import turtle                   # allows us to use the turtle library
wn = turtle.Screen()            # allows us to create graphics window
wn.title("Emely & Ela")         # we named our screen to Emely and Ela
wn.bgcolor("lightblue")         # we gave a color of lightblue to the Screen

Ela = turtle.Turtle()           # create a turtle named Ela
Ela.penup()
Ela.color("purple")
Ela.pensize(10)
Ela.left(180)
Ela.forward(200)
Ela.pendown()
Ela.right(90)
Ela.forward(100)
Ela.right(90)
Ela.forward(50)
Ela.penup()
Ela.left(180)
Ela.forward(50)
Ela.left(90)
Ela.forward(30)
Ela.left(90)
Ela.pendown()
Ela.forward(50)
Ela.penup()
Ela.right(90)
Ela.forward(70)
Ela.left(90)
Ela.forward(15)
Ela.left(75)
Ela.pendown()
Ela.forward(100)
Ela.right(150)
Ela.forward(100)
Ela.penup()
Ela.backward(50)
Ela.pendown()
Ela.right(100)
Ela.forward(20)
Ela.penup()
Ela.right(180)
Ela.forward(60)
Ela.right(90)
Ela.forward(50)
Ela.pendown()
Ela.right(190)
Ela.forward(100)
Ela.right(140)
Ela.forward(44)
Ela.left(110)
Ela.forward(44)
Ela.right(140)
Ela.forward(100)
Ela.penup()
Ela.left(90)
Ela.forward(25)
Ela.pendown()
Ela.left(85)
Ela.forward(100)
Ela.penup()
Ela.right(90)
Ela.forward(40)
Ela.pendown()
Ela.right(90)
Ela.forward(100)
Ela.left(90)
Ela.forward(50)
Ela.penup()
Ela.forward(25)
Ela.left(90)
Ela.pendown()
Ela.forward(55)
Ela.right(30)
Ela.forward(55)
Ela.penup()
Ela.backward(55)
Ela.left(60)
Ela.pendown()
Ela.forward(55)

Emely = turtle.Turtle()         # create a turtle named Emely
Emely.color("red")
Emely.pensize(10)
Emely.shape("circle")

Emely.penup()
Emely.left(90)
Emely.forward(130)
size = 10
for i in range(5):
    Emely.stamp()
    size = size + 1
    Emely.left(40)
    Emely.forward(100)
Emely.left(30)
Emely.forward(320)

Cat = turtle.Turtle()         # create a turtle named Cat
Cat.color("red")
Cat.pensize(10)
Cat.shape("circle")

Cat.penup()
Cat.left(90)
Cat.forward(130)
size = 10
for i in range(5):
    Cat.stamp()
    size = size + 1
    Cat.right(40)
    Cat.forward(100)
Cat.right(30)
Cat.forward(320)

Iza = turtle.Turtle()         # create a turtle named Emely
Iza.color("crimson")
Iza.pensize(7)
Iza.penup()
Iza.left(90)
Iza.forward(130)
Iza.pendown()
for i in range(5):
    Iza.left(40)
    Iza.forward(100)
Iza.left(30)
Iza.forward(320)

Aaron = turtle.Turtle()         # create a turtle named Cat
Aaron.color("crimson")
Aaron.pensize(7)
Aaron.penup()
Aaron.left(90)
Aaron.forward(130)
Aaron.pendown()
for i in range(5):
    Aaron.right(40)
    Aaron.forward(100)
Aaron.right(30)
Aaron.forward(320)


wn.exitonclick()
