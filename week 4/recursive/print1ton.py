l = []

def print1ToN(n):
    if n < 1:
        n = 1
    if n == 1:
        return l.append(n)
    print1ToN(n - 1)
    l.append(n)

def printNto1(n):
    if n < 1:
        n = 1
    if n == 1:
        return l.append(n)
    l.append(n)
    printNto1(n - 1)

n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)

print(l)