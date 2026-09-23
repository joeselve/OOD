def check_dup(my_list):
    check = 0
    new = []
    for num in my_list:
        if num in new:
            check += 1
        else:
            new.append(num)
    if check == len(my_list) - 1:
        return "john"
    else:
        return check
    
def check_sort_from_max(my_list):
    check = False
    for j in range(len(my_list) - 1):
        if my_list[j] >= my_list[j + 1]:
            check = True
        else:
            return False
    return check

def check_sort_from_min(my_list):
    check = False
    for j in range(len(my_list) - 1):
        if my_list[j] <= my_list[j + 1]:
            check = True
        else:
            return False
    return check

    


inp = [i for i in input("Enter Input : ")]
n_inp = [int(i) for i in inp]

if check_dup(n_inp) == "john":
    print("Repdrome")
elif check_sort_from_min(n_inp) == True and check_dup(n_inp) == 0:
    print("Metadrome")
elif check_sort_from_min(n_inp) == True and check_dup(n_inp) >= 1:
    print("Plaindrome")
elif check_sort_from_max(n_inp) == True and check_dup(n_inp) == 0:
    print("Katadrome")
elif check_sort_from_max(n_inp) == True and check_dup(n_inp) >= 1:
    print("Nialpdrome")
else:
    print("Nondrome")