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
Ela.penup()                     # put the pen up
Ela.color("purple")             # give ela the color purple
Ela.pensize(10)                 # defining the pen size
Ela.left(180)                   # moving turtle Ela to the left
Ela.forward(200)
Ela.pendown()
Ela.right(90)                    # starting each letter F for the word FAMILY
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
# Starting letter A
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
# Starting letter M
Ela.right(190)
Ela.forward(100)
Ela.right(140)
Ela.forward(44)
Ela.left(110)
Ela.forward(44)
Ela.right(140)
Ela.forward(100)
Ela.penup()   # moving forward
Ela.left(90)
Ela.forward(25)
Ela.pendown()
# Starting letter I
Ela.left(85)
Ela.forward(100)
Ela.penup()
Ela.right(90)
Ela.forward(40)
Ela.pendown()
# Starting letter L
Ela.right(90)
Ela.forward(100)
Ela.left(90)
Ela.forward(50)
Ela.penup()
Ela.forward(25)
Ela.left(90)
Ela.pendown()
# Starting letter Y
Ela.forward(55)
Ela.right(30)
Ela.forward(55)
Ela.penup()
Ela.backward(55)
Ela.left(60)
Ela.pendown()
Ela.forward(55)

Emely = turtle.Turtle()         # create a turtle named Emely
Emely.color("red")              # giving the pen color red
Emely.pensize(10)               # giving the pensize 10
Emely.shape("circle")           # we want our pen to have the shape of a circle
# moving the pen up and above the word
Emely.penup()
Emely.left(90)
Emely.forward(130)
size = 10                # setting the variable size to a value of 10
# we want a continous movement of the pen to shape the top part of the heart
for i in range(5):
    Emely.stamp()      # stamp will leave us the shape circle
    size = size + 1
    Emely.left(40)
    Emely.forward(100)
Emely.left(30)            # now we want to complete the left side of the heart
Emely.forward(320)

Cat = turtle.Turtle()         # create a turtle named Cat
Cat.color("red")              # we gave Cat the color red
Cat.pensize(10)               # assigned the pencil size
Cat.shape("circle")           # assigned the shape for Cat to be a circle

Cat.penup()
# this moves the pen up so we move the turtle above the word
Cat.left(90)
Cat.forward(130)
size = 10                      # setting the size variable to 10
# we want a continuous movement of the pen to shape the top part of the heart
for i in range(5):
    Cat.stamp()                # Leaving a mark as the turtle moves
    size = size + 1            # increasing the mark as the turtle goes in the loop
    Cat.right(40)
    Cat.forward(100)
Cat.right(30)                  # now we want to complete the left side of the heart
Cat.forward(320)

Iza = turtle.Turtle()         # create a turtle named Iza
Iza.color("crimson")          # we gave Iza the color crimson
Iza.pensize(7)                 # assigned the pencil size
Iza.penup()
# we want to move the turtle with the pen up so we can then start to pen down the shape of the heart
Iza.left(90)
Iza.forward(130)
Iza.pendown()
# we want a continuous movement of the pen to shape the top part of the heart with the pen down
for i in range(5):
    Iza.left(40)
    Iza.forward(100)
Iza.left(30)
Iza.forward(320)

Aaron = turtle.Turtle()         # create a turtle named Aaron
Aaron.color("crimson")          # we gave Iza the color crimson
Aaron.pensize(7)                # assigned the pencil size
Aaron.penup()
# we want to move the turtle with the pen up so we can then start to pen down the shape of the heart

Aaron.left(90)
Aaron.forward(130)
Aaron.pendown()
# we want a continuous movement of the pen to shape the top part of the heart with the pen down
for i in range(5):
    Aaron.right(40)
    Aaron.forward(100)
Aaron.right(30)
Aaron.forward(320)


wn.exitonclick()            # we want our program to finish when we click on it
