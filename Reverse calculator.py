import math
import itertools


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


def compacter1(number):
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


def testing(number,list):
    for i in list:
        a = happy(i)


def switch(number, old, new):
    old = list(map(int, str(old)))
    new = map(int, str(new))
    for i in number:
        if i in old:
            number.remove(i)
            old.remove(i)
    for i in new:
        number.append(i)
    number.sort()
    return number


def compacter2(number):
    possible = []
    for L in range(0, len(number)):
      for subset in itertools.combinations(number, L+1):
        a = list(subset)
        a = int(''.join(map(str, a)))
        for i in range(0, 101):
            if happy(a) == happy(i) and a != i and a > i:
                print(str(a) + " is the same as " + str(i))
                #possible.append(switch(number, a, i))
    #print(possible)

    return number


def reverse(n, deep_compressing):
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
    print(number)
    if deep_compressing:
        number = compacter2(number)
    else:
        number = compacter1(number)
    return int(''.join(map(str, number)))



while True:
    n = int(input("Enter number: "))
    n = reverse(n, True)
    print(n)
