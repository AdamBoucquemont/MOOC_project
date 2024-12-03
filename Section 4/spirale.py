import turtle

def spirale(color, largeur):
    rayon = 0
    screen = turtle.Screen()
    turtle.width(largeur)
    turtle.color(color)
    turtle.speed(0)
    for _ in range(100):
        rayon += largeur / 2
        turtle.circle(rayon, 90)
    screen.exitonclick()
    

spirale('red', 10)