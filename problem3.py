#! python3
"""
Create a function called factors()
Input parameter is a positive integer
Output is a sorted list containing all of the factors of that number.
Note: A Factor is a positive integer that can be evenly divided
into another number.
Example: The factors of 10 are 1, 2, 5, 10
(2 points)
"""

def factors(x):
    l = []
    for i in range(1,x+1):
        if x%i == 0:
            l.append(i)
    return l

if __name__ == "__main__":
    n = factors(10)
    assert sorted(n) == [1, 2, 5, 10]
    n = factors(24)
    assert sorted(n) == [1,2,3,4,6,8,12,24]
    n = factors(3)
    assert sorted(n) == [1,3]
    assert sorted(factors(25)) == [1,5,25]

    n = factors(10)
    print("The factors of 10 are ")
    for i in n:
        print(i,end="")
        if i != n[-1]:
            print(", ", end="")
    else: print()

    
