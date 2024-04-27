import turtle
import keyboard

turt = turtle.Turtle()

while True:
    if keyboard.is_pressed("w"):
        turt.forward(20)
    if keyboard.is_pressed("s"):
        turt.back(20)
    if keyboard.is_pressed("d"):
        turt.right(90)
    if keyboard.is_pressed("a"): 
        turt.left(90)
    if keyboard.is_pressed("esc"):
        break
    if keyboard.is_pressed("f"):
        turt.color("red")
        turt.forward(100)
        turt.right(90)
        turt.forward(100)
        turt.left(90)
        turt.forward(100)
        turt.left(180)
        turt.forward(100)
        turt.right(90)
        turt.forward(50)
        turt.left(90)
        turt.forward(100)
        turt.left(90)
        turt.forward(50)
        turt.left(180)
        turt.forward(50)
        turt.right(90)
        turt.forward(200)
        turt.left(90)
        turt.forward(50)
        turt.right(90)