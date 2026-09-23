result = False
i = 0
furthest = 0

def canjump(inp):
    global result, i, furthest
    n = len(inp)
    if i > furthest:
        result = False
        return
    furthest = max(furthest, i + inp[i])
    if furthest >= n - 1:
        result = True
        return
    i += 1
    canjump(inp)


inp = [int(x) for x in input("level data : ").strip().split()]

canjump(inp)
print(f"Can Jump: {result}")

