count = 0
i = 0
str_l = []

def length(txt):
    #Code Here
    global count, i    
    try:
        text = txt[i]
        count += 1
        str_l.append(text)
        if i % 2 == 0:
            str_l.append("*")
        else:
            str_l.append("~")
        i += 1
        return length(txt)
    except IndexError:
        return count

    

length(input("Enter Input : "))
print("".join(str_l))
print(count)
#ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้)