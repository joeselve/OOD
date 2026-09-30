def staircase(n, index = 0, result = ""):
    if n == 0 and index == 0:
            print("Not Draw!")
            return
        
    if n >= 1:
        space = n - 1
        
        result += "_" * space
        result += "#" * (index + 1)
        print(result)
        
        staircase(n - 1, index + 1)
    if n < -1:
        write = abs(n) - 1
        
        result += "_" * index
        result += "#" * write
        
        print(result)
        
        staircase(n + 1, index + 1)

staircase(int(input("Enter Input : ")))