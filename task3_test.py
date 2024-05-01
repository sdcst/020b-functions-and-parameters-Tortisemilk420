#! python3

import task3

def test1():
  assert task3.perimeter( [5,2,6]) == 13

def test2():
  assert task3.perimeter( [9,8,6,5.5] ) == 28.5

  
if __name__ == "__main__":
  test1()
  test2()

