import math
import itertools
import copy

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
    sofar = []
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
    return makenumber(number)


def testing(number,list):
    for i in list:
        a = happy(i)


def switch(number, old, new):
    test = copy.copy(number)
    old = list(map(int, str(old)))
    new = map(int, str(new))
    for i in old:
        test.remove(i)
    for i in new:
        test.append(i)
    test.sort()
    return test


def makenumber(n):
    return int(''.join(map(str, n)))


def compacter2(number):
    possible = []
    length = len(number)-number.count(9)+2
    for L in range(0, length):
      for subset in itertools.combinations(number, L+1):
        a = list(subset)
        a = int(''.join(map(str, a)))
        for i in range(0, 101):
            if happy(a) == happy(i) and a != i and a > i:
                #print(str(a) + " is the same as " + str(i))
                if switch(number, a, i) not in possible:
                    possible.append(switch(number, a, i))
    #print(possible)
    for i in range(0,len(possible)):
        possible[i] = makenumber(possible[i])
    possible.sort()
    if len(possible) > 0:
        print("compacted")
        return possible[0]
    else:
        return makenumber(number)


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
    return number



while True:
    n = int(input("Enter number: "))
    n = reverse(n, True)
    print(n)
