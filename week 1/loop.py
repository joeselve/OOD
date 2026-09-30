print(" *** Summation of each digit ***")

inp = input("Enter a positive number : ")
list_inp = list(inp)

result = 0
for number in list_inp:
    temp = int(number)
    result += temp

print(f"Summation of each digit =  {result}")
