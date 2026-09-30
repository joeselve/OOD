print("*** Fun with Drawing ***")

inp = int(input("Enter input : "))

ran = 0
for row in range(1, inp + 1):
    f_point = inp
    l_point = inp * 3 - 2
    point = []
    my_list = []
    for col in range(1, inp * 4 - 2):
        if (col == f_point - ran) or (col == f_point + ran):
                point.append(col)
                my_list.append("*")
        elif (col == l_point - ran) or (col == l_point + ran):
            point.append(col)
            my_list.append("*")
        elif (f_point - ran < col < f_point + ran):
             my_list.append("+")
        elif (l_point - ran < col < l_point + ran):
             my_list.append("+")
        else:
            my_list.append(".")
    line = "".join(my_list)
    print(line)
    ran += 1

ran = 2
for row in range(2, inp * 2):
    f_point = ran
    l_point = inp * 4 - 2 - ran
    my_list = []
    for col in range(1, inp * 4 - 2):
        if col == f_point:
            my_list.append("*")
        elif col == l_point:
             my_list.append("*")
        elif f_point < col < l_point:
            my_list.append("+")
        else:
            my_list.append(".")
    line = "".join(my_list)
    print(line)
    ran += 1
    