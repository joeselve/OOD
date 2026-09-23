i = 0

def staircase(n):
    #code here
    global i, str_p_l
    if n > 0:
        i += 1
        j = (n - 1) * "_"
        k = i * "#"
        row = j + k
        print(row)
        staircase(n - 1)
    elif n < 0:
        n = abs(n)
        j = n * "#"
        k = i * "_"
        i += 1
        row = k + j
        print(row)
        staircase(-(n - 1))

inp = int(input("Enter Input : "))

if inp == 0:
    print("Not Draw!")
else:
    staircase(inp)

