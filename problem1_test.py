#! python3
import problem1


def test1():
  # Problem 1 Assertions
  assert problem1.hypotenuse(3,4,True) == 5

def test2():
  assert problem1.hypotenuse(13,5,False) == 12
  
if __name__ == "__main__":  
  test1()
  test2()
