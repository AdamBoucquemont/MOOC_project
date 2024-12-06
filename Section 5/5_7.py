def plus_grand_bord(w):
    plus_grand_bord = ''
    i = len(w) - 1
    while i != 0 and plus_grand_bord == '':
        if w[:i] == w[-i:]:
            plus_grand_bord = w[:i]
        i -= 1
    return plus_grand_bord
    
print(plus_grand_bord('abdabda'))
print(plus_grand_bord('abcabd'))
print(plus_grand_bord('abcba'))
print(plus_grand_bord('aaaaa'))