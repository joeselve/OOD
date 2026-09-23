def sort(my_list):
    new = my_list.copy()
    for i in range(len(new)):
        for j in range(len(new) - i - 1):
            if new[j] > new[j + 1]:
                new[j + 1], new[j] = new[j], new[j + 1]
    return new

def median(my_list):
    if len(my_list) % 2 != 0:
        return my_list[len(my_list)//2]
    else:
        return (my_list[len(my_list)//2 - 1] + my_list[(len(my_list)//2)]) / 2


l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    new = []
    for num in l:
        new.append(int(num))
        print(f"list = {new} : median = {median(sort(new)):.1f}")
