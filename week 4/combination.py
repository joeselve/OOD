num_l = []

def Combination(input_list, answer = []):
    if answer is None:
        answer = []
    if not input_list:
        if answer:
            num_l.append(answer)
        return
    first = input_list[0]
    rest = input_list[1:]
    Combination(rest, answer + [first])
    Combination(rest, answer)

inp = [int(x) for x in input("Enter Input: ").strip().split()]

Combination(inp)

print(f"Output: {num_l}")
