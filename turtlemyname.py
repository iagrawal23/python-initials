import turtle
import random

turtle.shape("turtle")
turtle.pensize(5)

turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.left(180)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(25)
turtle.right(90)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(100)
turtle.left(90)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(25)
turtle.left(180)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.penup()
turtle.forward(30)

turtle.pendown()
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.left(180)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.left(90)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.left(90)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.right(90)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.right(90)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.penup()
turtle.left(180)
turtle.forward(80)

turtle.pendown()
turtle.left(90)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(100)
turtle.left(180)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.left(90)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.left(90)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.left(180)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(100)
turtle.penup()
turtle.left(90)
turtle.forward(30)

turtle.pendown()
turtle.left(75)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(100)
turtle.left(180)
turtle.left(30)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(100)
turtle.left(180)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.left(75)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(25)
turtle.penup()
turtle.left(180)
turtle.forward(55)

turtle.pendown()
turtle.right(90)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(50)
turtle.left(180)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(100)
turtle.left(180)
turtle.left(30)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(100)
turtle.left(180)
turtle.right(30)
turtle.color(random.choice(["red","yellow","blue","green","orange"]))
turtle.forward(100)
turtle.penup()
turtle.forward(30)
turtle.right(17)

turtle.pendown()
for i in range(0,5):
    turtle.color(random.choice(["red","yellow","blue","green","orange"]))
    turtle.forward(100)
    turtle.right(144)
    
turtle.exitonclick()
