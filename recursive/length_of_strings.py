def length(txt):
    if not txt:
        return 0
    elif not txt[1:]:
        print(txt[0] + '*', end="")
        return 1
    else:
        print(txt[0] + "*" + txt[1] + "~", end="")
        return 2 + length(txt[2:])
    
    
print("\n",length(input("Enter Input : ")),sep="")
#ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้)