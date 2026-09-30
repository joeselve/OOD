l = []

def Combination(input_list, answer = []):
    if answer is None:
        return []
    if not input_list:
        if answer:
            l.append(answer)
        return
    first = input_list[0]
    rest = input_list[1:]
    
    Combination(rest, answer + [first])
    Combination(rest, answer)
    
inp = [int(i) for i in input("Enter Input: ").strip().split()]
Combination(inp)
print(f"Output: {l}")
