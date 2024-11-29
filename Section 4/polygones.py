import turtle
from math import cos, sin, pi, gcd
from random import randint

def polygone_turtle(n_cotes, centre_x, centre_y, rayon, couleur):
    turtle.penup()
    turtle.pencolor(couleur)
    turtle.fillcolor(couleur)
    turtle.goto(centre_x, centre_y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(1, n_cotes+2):
        turtle.goto(centre_x+rayon*cos(i*2*pi/n_cotes), centre_y+rayon*sin(i*2*pi/n_cotes))
    turtle.end_fill()
    
def etoile_turtle(n_cotes, centre_x, centre_y, rayon, couleur):
    turtle.penup()
    turtle.pencolor(couleur)
    turtle.fillcolor(couleur)
    turtle.goto(centre_x, centre_y)
    turtle.pendown()
    turtle.begin_fill()
        
    est_possible = False 
    while not est_possible:
        inc = (n_cotes-1) // 2
        while gcd(n_cotes, inc) > 1:
            inc = inc - 1
        if inc == 1 :
            n_cotes += 1
        else:
            est_possible = True
            
    angle =  180 - (n_cotes - 2 * inc) * 180 / n_cotes
    for i in range(n_cotes):
        turtle.forward(rayon)
        turtle.left(angle)
        
    turtle.end_fill()
    
colors = ["black", "blue", "red", "green", "yellow"]

for color in colors : 
    polygone_turtle(randint(3, 10), randint(-450, 450), randint(-350, 350), randint(10, 200), color)
    etoile_turtle(randint(3, 10), randint(-450, 450), randint(-350, 350), randint(10, 400), color)
turtle.done()