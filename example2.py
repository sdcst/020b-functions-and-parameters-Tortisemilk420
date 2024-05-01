#!python3

"""
A function can return more than 1 value, if it is returned as a tuple or list.
The return value can be assigned to a variable or assigned to as many variables
as are in the tuple/list, and each value can be assigned separately, in order.
Alternatively, the output can be retained as a tuple/list
"""

def plus(x,y,z):
    # inputs: 
    # x: any number
    # y: any number
    # z: any number
    # returns: a tuple of 3 numbers
    # function adds one to each of the input parameters and returns them
    return ( x+1, y+1, z+1 )


a,b,c = plus(3,4,5)
print(a)

x = plus(5,6,7)
print(x)

y = plus(a,b,10)
# note that variables can be used as input parameters
print(y)
pass