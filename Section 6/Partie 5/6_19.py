import random

def create_map(size, trapsNbr):
    carte = {}
    new_abs = random.randint(1, size)
    new_ord = random.randint(1, size)
    carte[(new_abs, new_ord)] = 1
    while len(carte) <= trapsNbr:
        new_abs = random.randint(1, size)
        new_ord = random.randint(1, size)
        if (new_abs, new_ord) not in carte:
            carte[(new_abs, new_ord)] = -1
    return carte
        
    
def play_game(map_size, treasure_map):
    game_continue = True
    while game_continue:
        new_deplacement = input().split()
        new__abs_deplacement = int(new_deplacement[0])
        new_ord_deplacement = int(new_deplacement[1])
        if type(new__abs_deplacement) == int and type(new_ord_deplacement) == int and new_ord_deplacement <= map_size and new__abs_deplacement <= map_size:
            if (new__abs_deplacement, new_ord_deplacement) in treasure_map:
                game_continue == False
                if treasure_map[(new__abs_deplacement, new_ord_deplacement)] == 1:
                    return True
                else:
                    return False
    
    
print(create_map(4, 5))
print(play_game(5, {(3, 4): -1, (4, 1): 1, (2, 3): -1, (1, 5): -1}))
print(play_game(5, {(3, 4): -1, (4, 1): 1, (2, 3): -1, (1, 5): -1}))