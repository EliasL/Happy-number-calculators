import sys


def square(x):
    return int(x) * int(x)


def happy(number):

    return sum(map(square, list(str(number))))


def is_happy(number):

    sad_numbers =(4, 16, 37, 58, 89, 145, 42, 20)
    x = 0
    while number > 1 and (number not in sad_numbers):
        number = happy(number)
        x += 1
    return number == 1, x



c = 0
n = 1
lhn = []

maxn = 1000000# 1 000 000

done = 0

for i in range(maxn):
    H, c = is_happy(n)
    if H:
        lhn.append((c, n))
    n += 1
    if i % (maxn/100) == 0:
        done += 1
        print(str(done) + "%")

lhnPath = "Order of happy numbers with the actual number.txt"


def writeln(path, numbers):
    document = open(path, "w")
    for i in numbers:
        document.write(str(i))
        document.write("\n")

writeln(lhnPath, lhn)
