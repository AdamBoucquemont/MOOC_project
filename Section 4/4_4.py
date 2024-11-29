from random import randint, seed

def alea_dice(s):
    seed(s)
    a = randint(1, 6)
    b = randint(1, 6)
    c = randint(1, 6)
    
    return a != b != c and (a == 4 or a == 2 or a == 1) and (b == 4 or b == 2 or b == 1) and (c == 4 or c == 2 or c == 1)