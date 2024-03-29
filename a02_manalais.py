######################################################################
# Author: Sama Manalai
# Username: manalais
#

# Assignment: A02: Loopy Language
# Purpose: Draws an Ice cream and a square
######################################################################
import turtle

def icecream_cone(cone):
    cone.penup()
    cone.pensize(3)
    cone.setpos(25, 25)
    cone.color('tan')
    cone.pendown()
    cone.fillcolor('tan')
    cone.begin_fill()
    cone.right(70)
    cone.forward(102)
    cone.left(70)
    cone.forward(40)
    cone.right(-75)
    cone.forward(100)
    cone.left(105)
    cone.forward(100)
    cone.end_fill()
def icecream_circle(circle):
    circle.penup()
    circle.setpos(75, 100)
    circle.pensize(3)
    circle.color('pink')
    circle.pendown()
    circle.fillcolor('pink')
    circle.begin_fill()
    circle.circle(-52)
    circle.end_fill()
def random0(random):
    random.penup()
    random.setpos(-45,40)
    random.pensize(6)
    random.color('blue')
    random.pendown()
    random.fillcolor('blue')
    random.begin_fill()
    for side in range(2):
        random.forward(60)
        random.right(90)
        random.forward(60)
        random.right(90)
    random.end_fill()


def main():
    wn = turtle.Screen()
    cone = turtle.Turtle()
    circle = turtle.Turtle()
    random = turtle.Turtle()
    icecream_cone(cone)
    icecream_circle(circle)
    random0(random)
    wn.exitonclick()

main()
