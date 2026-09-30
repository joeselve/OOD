def bubblesort(arr):
    n = len(arr)
    if n < 2:
        return "not enough bidder"

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
        first = arr[0]
        second = arr[1]

    if first == second:
        return "error : have more than one highest bid"
    return f"winner bid is {first} need to pay {second}"



inp = input("Enter All Bid : ")

my_list = inp.split()
new_list = []

for number in my_list:
    n = int(number)
    new_list.append(n)

print(bubblesort(new_list))





