#!python3
"""
NOTE:
If you complete this extension, call your teacher over to have it assessed


Create a program to determine the solutions for a quadratic equation
in the format ax^2 + bx + c = 0
A key is the discriminant: b^2 - 4 * a * c
If the discriminant is negative, there are no solutions
If the discriminant is zero, there is only 1 solution
If the discriminant is positive, there are 2 solutions

If the discriminant is a perfect square, then the equation can
be factored

If the discriminant is non zero, the solutions are:
x = (-b + sqrt(b^2 - 4 * a * c)) / 2a
x = (-b - sqrt(b^2 - 4 * a * c)) / 2a

Assignment criteria:
Create a program that inputs 3 float values: a, b, c
function numSolutions(a,b,c) returns an integer with the number of solutions
function solutions(a,b,c) returns a tuple with the solutions (note that if 1 solution,
then both solutions will be the same)

If there are no solutions:
output is: "There are no real solutions"

If there is one solution:
output is "There is 1 solution, x=??"

If there are two solutions:
output is: "The solutions are x=?? and x=??"
"""

def numSolutions(a,b,c):
    # inputs:
    # float a
    # float b
    # float c
    # Description:
    #
    # return 0, 1 or 2
    return 

def solutions(a,b,c):
    #inputs:
    # float a
    # float b
    # float c
    # Desription:
    #
    # return tuple of float solution1 and float solution2
    return

def title():
    # inputs none
    # return str of All the title and instructions on one line
    return


def main():
    # Display Title and Instructions
    print( title() )
    # Your code and function calls should go here



main()