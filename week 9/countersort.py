def countersort(my_list):
    num_list = []
    for num in my_list:
        r = check(num_list, num)
        if r is False:
            num_list.append([num, 1])
        else:
            num_list[r][1] += 1
            
    for i in range(len(num_list)):
        for j in range(len(num_list) - i - 1):
            if num_list[j][1] < num_list[j + 1][1]:
                num_list[j + 1], num_list[j] = num_list[j], num_list[j + 1]
    return num_list

def check(num_list, num):
    i = 0
    for f_num in num_list:
        if num == f_num[0]:
            return i
        i += 1
    return False
                

inp = [int(i) for i in input("Enter list  of numbers: ").split()]

for k in countersort(inp):
    print(f"number {k[0]}, total: {k[1]}")