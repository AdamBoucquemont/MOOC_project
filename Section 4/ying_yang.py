""" code avec fonction yin_yang dessiné avec turtle """
import turtle

def yin_yang(rayon, color1='black', color2='white'):
    """ dessine un logo yin-yang de rayon rayon """

    def yang (rayon, couleur1, couleur2):
        """ dessin du yang à l'intérieur du yin (ou vice versa) """
        turtle.right(90)
        turtle.up()
        turtle.forward(2 * rayon/3)
        turtle.left(90)
        turtle.down()
        turtle.color(couleur1, couleur2)
        turtle.begin_fill()
        turtle.circle(rayon/6)
        turtle.end_fill()
        turtle.right(90)
        turtle.up()
        turtle.backward(2 * rayon/3)
        turtle.down()
        turtle.left(90)
        
        # turtle.color(couleur1, couleur2)
        # turtle.up()
        # turtle.right(rayon / 200 * 90)
        # turtle.forward(rayon / 200 * 80)
        # turtle.left(rayon / 200 * 90)
        # turtle.down()
        # turtle.begin_fill()
        # turtle.circle(-rayon / 10)
        # turtle.end_fill()
        
        # turtle.left(90)
        # turtle.up()
        # turtle.forward(rayon/3)
        # turtle.right(90)
        # turtle.down()
        # turtle.color(couleur1, couleur2)
        # turtle.begin_fill()
        # turtle.circle(rayon/6)
        # turtle.end_fill()
        # turtle.left(90)
        # turtle.up()
        # turtle.backward(rayon/3)
        # turtle.down()
        # turtle.left(90)

    def yin(rayon, couleur1, couleur2):
        """ dessine la moitié d'un yin-yang
            utilise la fonction yang """
        turtle.color("black", couleur1)
        turtle.begin_fill()
        turtle.circle(- rayon / 2, 180)
        turtle.circle(- rayon, - 180)
        turtle.circle(- rayon / 2, - 180)
        turtle.end_fill()
        yang(rayon, couleur1, couleur2)
        
        # turtle.color("black", couleur1)
        # turtle.begin_fill()
        # turtle.circle(rayon/2, 180)    # demi cercle de rayon / 2
        # turtle.circle(rayon, 180)       # demi cercle de rayon
        # turtle.left(180)
        # turtle.circle(-rayon/2, 180)   # demi cercle intérieur de rayon / 2
        # turtle.end_fill()
        # yang(rayon, couleur1, couleur2)

    #code de yin_yang
    turtle.reset()
    turtle.width(2)
    turtle.speed("fastest")
    yin(rayon, color1, color2)
    turtle.up()
    turtle.goto(0, 0)
    turtle.down()
    yin(rayon, color2, color1)
    turtle.hideturtle()
    turtle.done()
    return

#code principal
yin_yang(300) #réalise le logo de rayon 200