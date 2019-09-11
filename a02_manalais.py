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









def main():
    wn = turtle.Screen()
    cone = turtle.Turtle()
    circle = turtle.Turtle()
    icecream_cone(cone)
    icecream_circle(circle)
    wn.exitonclick()

main()
