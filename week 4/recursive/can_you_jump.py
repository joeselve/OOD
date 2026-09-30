def jump(input_list, index = 0, furthest = 0):
    n = len(input_list)
    
    if index < furthest:
        return False
    
    furthest = max(furthest, index + input_list[index])
    
    if furthest >= n - 1:
        return True
    
    return jump(input_list, index + 1, furthest)

inp = [int(i) for i in input("level data : ").split()]

print(jump(inp))