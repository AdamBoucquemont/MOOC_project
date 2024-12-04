def distance_points(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 ) ** (1 / 2)

def longueur(*points):
    distance_total = 0
    for i in range(len(points) - 1):
        distance_total += distance_points(points[i], points[i+1])
    return distance_total

print(longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0)))
print(longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0)))