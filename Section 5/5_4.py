def distance_points(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 ) ** (1 / 2)

print(distance_points((1.0, 1.0), (2.0, 1.0)))
print(distance_points((-1.0, 0.5), (2.0, 1.0)))