

from geom.point import *

raw = [ (2,2), (0,5), (8,0), (9,8), (7,14),
              (13,12), (14,13) ]
points = [ Point(p[0], p[1]) for p in raw]

def get_shortest(all_points):
    min_dist = 5000
    for p1 in all_points:
        for p2 in all_points:
            if p1 is not p2:
                d = p2 - p1
                if d < min_dist:
                    min_dist = d
    return min_dist

print(get_shortest(points))
