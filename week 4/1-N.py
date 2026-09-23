str_l = []

def print1ToN(n):
    #code here
    if n == 0:
        return
    print1ToN(n-1)
    str_l.append(str(n))

def printNto1(n):
    if n < 1:
        return
    if n == 0:
        return
    str_l.append(str(n))
    printNto1(n-1)

n = int(input("Enter Input : "))

if n < 1:
    str_l.append("1")
    str_l.append("1")
else:
    print1ToN(n)
    printNto1(n)
string = " ".join(str_l)
print(string)