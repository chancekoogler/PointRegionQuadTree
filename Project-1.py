# Chance Koogler
# Project (1)
# GEOG 5222
# December 9, 2020

import random
from geom.point import *

class PQuadTree():
    def __init__(self, node, nw, ne, se, sw):
        self.node = node
        self.nw = nw
        self.ne = ne
        self.se = se
        self.sw = sw
        
    def __repr__(self):
        return str(self.node)

    def is_leaf(self):
        return self.nw == None and self.ne == None and self.se == None and self.sw == None

    def insert(self, point):
      # no identical points allowed
        if self.node == point:
            return
      # if it is topright:
        elif point.x > self.node.x and point.y > self.node.y:
          # if node is empty, add it
            if self.ne is None:
                self.ne = PQuadTree(point, None, None, None, None)
          # else, use taken node as root for next level initialization
            else:
                self.ne.insert(point)
# above algorithm is applied for each quadrant.
# last else statement assumes sw position if other 3 have been covered
        elif point.x > self.node.x and point.y < self.node.y:
            if self.se is None:
                self.se = PQuadTree(point, None, None, None, None)
            else:
                self.se.insert(point)

        elif point.x < self.node.x and point.y > self.node.y:
            if self.nw is None:
                self.nw = PQuadTree(point, None, None, None, None)
            else:
                self.nw.insert(point)

        else: 
            if self.sw is None:
                self.sw = PQuadTree(point, None, None, None, None)
            else:
                self.sw.insert(point)

# function to createQT
def createQT(points):
# set first point from set of points as root
  root = PQuadTree(points[0], None, None, None, None)
# loop through rest of points
  for p in points:
# insert each subsequent point into root
    root.insert(p)
# return root and it's "attributes" AKA the final tree
  return root


def orthogonal_query(t, rect, found):
  # The list must be passed as a function argument, I found declaring the list
  # within this function does not print accurate results (issue with recursive
  # call)
  if rect is None:
    return print("Error. Rectangle must have format [ [x-min, x-max], [y-min, y-max] ]")
  if t is None:
    return
  # if point is greater than x-min and less than x-max
  if  t.node.x >= rect[0][0] and t.node.x <= rect[0][1]:
  # if point is greater than y-min and less than y-max
    # must be in rectangle
    if t.node.y >= rect[1][0] and t.node.y <= rect[1][1]:
      found.append(t.node)
  orthogonal_query(t.nw, rect, found)
  orthogonal_query(t.ne, rect, found)
  orthogonal_query(t.se, rect, found)
  orthogonal_query(t.sw, rect, found)
  return found

def test1():
    # Test1 sample data taken from GISalgs github
    found = []
    raw = [ (2,2), (0,5), (8,0), (9,8), (7,14),
              (13,12), (14,13) ]
    points = [ Point(p[0], p[1]) for p in raw]
    rect = [ [0,5], [0,5] ]
    t = createQT(points)
    print(orthogonal_query(t,rect, found))
    print()

def test2():
    found = []
    # 10 random points. Points coordinates are Random Floats of value: 0 <= x < 100
    points = [Point(random.uniform(0, 100), random.uniform(0, 100))
          for i in range(10)]
    rect = [ [0,50], [0,50] ]
    t = createQT(points)
    print(orthogonal_query(t,rect, found))
    print()

test1()
test2()

