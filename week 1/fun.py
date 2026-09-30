class funString():

    def __init__(self,string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self) :
        n = len(self.string)
        return n
    def changeSize(self):
        new_string = ""
        for cha in self.string:
            temp = 0
            if 65 <= ord(cha) <= 90:
                temp = ord(cha) + 32
                new_string += chr(temp)
            elif 97 <= ord(cha) <= 122:
                temp = ord(cha) - 32
                new_string += chr(temp)
        return new_string

    def reverse(self):
        return self.string[::-1]

    def deleteSame(self):
        my_list = []
        new_string = ""
        for cha in self.string:
            if cha not in my_list:
                my_list.append(cha)
                new_string += cha
        return new_string



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())