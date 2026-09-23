print("*** Odd Even ***")

def odd_even(type, data, mode):
    if type == "S":
        result = ""
        for cha in range(len(data)):
            if mode == "Odd":
                if cha%2 == 0:
                    result += data[cha]
            elif mode == "Even":
                if cha%2 != 0:
                    result += data[cha]

    if type == "L":
        result = []
        new_list = data.split()
        for cha in range(len(new_list)):
            if mode == "Odd":
                if cha%2 == 0:
                    result.append(new_list[cha])
            elif mode == "Even":
                if cha%2 != 0:
                    result.append(new_list[cha])
    
    return result
                
inp = input("Enter Input : ").split(",")

t = inp[0]
d = inp[1]
m = inp[2]

print(odd_even(t, d, m))
