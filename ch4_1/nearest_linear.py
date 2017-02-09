from math import sqrt

def sq_dist(p, q):
    return((p[0] - q[0])**2 + (p[1] - q[1])**2)

def linear_search(points, query):
    sqd = float("inf")
    for point in points:
        d = sq_dist(point, query)
        if d < sqd:
            nearest = point
            sqd = d
    return(nearest, sqd)

point_list = [(2, 5), (5, 7), (10, 2), (3, 3), (8, 9), (1, 1)]
n = linear_search(point_list, (9, 6))
print('nearest:', n[0], 'dist:', sqrt(n[1]))

