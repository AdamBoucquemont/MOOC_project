import turtle
from math import pi, sin, cos
import random
import time

def pave(abscisse_centre, ordonnee_centre, longueur_arete, color1, color2, color3):
    """ Dessine avec turtle un pave hexagonal
        en position ( abscisse_centre, ordonnee_centre)
        paramètres :
        - (abscisse_centre, ordonnee_centre) : point centre du pavé
        -  longueur_arete : longueur de chaque arête du pavé
        - color1, color2, color3 : les couleurs des 3 hexagones"""
    turtle.up()
    turtle.goto(abscisse_centre, ordonnee_centre)
    turtle.down()
    for color in [color1, color2, color3]:
        turtle.color('black', color)
        turtle.begin_fill()
        angle = 120
        for _ in range(4):
            turtle.forward(longueur_arete)
            turtle.left(angle)
            angle = 180 - angle
        turtle.right(120)
        turtle.hideturtle()
        turtle.end_fill()

turtle.hideturtle()
turtle.speed(0)
turtle.reset()
time.sleep(5)

while True:
    pave(random.randint(-300,300),  random.randint(-300,300),
        random.randint(10,50), 'black', 'red', 'blue')
    pave(random.randint(-300,300),  random.randint(-300,300),
        random.randint(10,50), 'white', 'grey', 'black')