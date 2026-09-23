def get_combinations(arr, start=0, current=[]):
    combos = []
    
    if current:
        combos.append(current)
        
    for i in range(start, len(arr)):
        combos.extend(get_combinations(arr, i + 1, current + [arr[i]]))
        
    return combos

def sort(my_list):
    new = my_list.copy()
    for i in range(len(new)):
        for j in range(len(new) - i - 1):
            if new[j] > new[j + 1]:
                new[j + 1], new[j] = new[j], new[j + 1]
    return new

def sort_list(m_list):
    new_list = []
    max_len = max(len(ob) for ob in m_list)
    for i in range(1, max_len + 1):
        for ob in m_list:
            if len(ob) == i:
                new_list.append(ob)
    return new_list

inp = [i for i in input("Enter Input : ").strip().split("/")]

goal, old_my_list = int(inp[0]), [int(i) for i in inp[1].split()]

my_list = sort(old_my_list)

new_list = []
for l in get_combinations(my_list):
    if sum(l) == goal:
        new_list.append(l)
        
if len(new_list) != 0:
    for l in sort_list(new_list):
        print(l)
else:
    print("No Subset")