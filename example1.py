#!python3

"""
A function is created by defining using the def command.
The commands will not be executed unless the function is
"called"

 def : tells us that a function is being defined
     : it is followed by the function name and input parameters
     : the name must meet the same criteria as naming variables
 all the commands within the function are indented to indicate
 the function block of commands
 the input parameter is required, and is a variable that can be
 used inside the function
 the return value is sent back to the main block of code
 notice the use of comments to indicate what the input parameters are
 as well as what the output is

 NOTE: You can think of each function as being its down distinct unit.  Any variables that you create inside a function only exist inside that function, and any variables that were created outside the function do not exist inside the function

 Notice that the function does not contain any output or print statements.  The goal of using a function is to create reusable code that can be placed in many different programs.  We can put print statements in to test how the function is working, but it is a good idea to remove them/comment them out so that they don't intefere with the program's output later on.
"""

def double(number):
    """
     input:
       a float number
     output:
       a float number
     purpose: to generate the value of the input number when doubled
    """

    answer = number * 2
    #print(answer)
    return answer


# note: The function must be "called", which means using the name
# to execute the code.  The function can be used "inline" or assigned
# to a variable.

print("==This is an inline use of a function")
print(f"The number 4, when doubled is { double(4) }" )
print("\n\n")


print("==This is how the value of the function can be assigned")
x = double(4)
print(f"The number 4, when doubled is {x}" )
print("\n\n")

print("==Functions can receive inputs that are variable:")
num = float(input("Enter a number:"))
print(f"The number { num } when doubled is { double(num) }")
print("or")
answer = double(num)
print("The answer is "  + str(answer))
