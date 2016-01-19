import math

# Note, this calculator does not compact

def square(x):
    return int(x) * int(x)


def happy(number):

    return sum(map(square, list(str(number))))


def findD(n, number, d):
    m = 0
    if n >= (d**2):
        m = math.floor(n/d**2)
        print("There are/is "+str(m)+" \""+str(d)+"\"s")
    n = n - (d**2 * m)
    return n, number


def reverse(n):
    i = 0
    number = []
    n, number = findD(n, number, 9)
    n, number = findD(n, number, 8)
    n, number = findD(n, number, 7)
    n, number = findD(n, number, 6)
    n, number = findD(n, number, 5)
    n, number = findD(n, number, 4)
    n, number = findD(n, number, 3)
    n, number = findD(n, number, 2)
    n, number = findD(n, number, 1)


while True:
    n = int(input("Enter number: "))
    reverse(n)
