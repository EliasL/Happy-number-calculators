import math

def square(x):
    return int(x) * int(x)


def happy(number):

    return sum(map(square, list(str(number))))


def findD(n, number, d):
    m = 0
    if n >= ((d**2)):
        m = math.floor(n/d**2)
        for i in range(m):
            number.append(d)
    n = n - ((d**2) * m)
    return n, number


def compacter(number):
    sofar=[]
    for i in number:
        if i != 9:
            sofar.append(i)

    compacting = int(''.join(map(str, sofar)))
    compacting = happy(compacting)
    new = 81+compacting
    for j in range(9):
        for k in range(9):
            if j**2+k**2 == new:
                number.remove(9)
                for i in sofar:
                    number.remove(i)
                number.insert(0, k)
                number.insert(0, j)
                return number
    return number


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
    number = number[::-1]
    if 9 in number and number[0] != 9:
        number = compacter(number)
    return int(''.join(map(str, number)))



while True:
    n = int(input("Enter number: "))
    n = reverse(n)
    print(n)
