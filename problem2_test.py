#! python3


import problem2


def test1():
  # Problem 2 Assertions
  assert round(problem2.distance( (2,4) , (6,3)) , 3) == 4.123

def test2():
  assert round(problem2.distance( (-3,2.2) , (1,2)) , 3) == 4.005


