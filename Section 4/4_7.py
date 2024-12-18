from math import sqrt

def rac_eq_2nd_deg(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        r1 = (-b + sqrt(delta)) / 2 * a
        r2 = (-b - sqrt(delta)) / 2 * a
        return (min(r1, r2), max(r1, r2))
    elif delta == 0:
        return (- b / 2 * a,)
    else:
        return ()
    
print(rac_eq_2nd_deg(1.0,-4.0,4.0))
print(rac_eq_2nd_deg(1.0,1.0,-2.0))
print(rac_eq_2nd_deg(1.0,1.0,1.0))