#! python3
import task4

def test1():
  assert task4.isInteger( 9.5 ) == False

def test2():
  assert task4.isInteger( -2 ) == True
