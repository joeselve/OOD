from collections import deque


class Queue(): #Queue Class
    def __init__(self, dequ = None):
        if dequ == None:
            self.__queue = deque()
        else:
            self.__queue = deque(dequ)

    def enqueue(self, item):
        self.__queue.append(item)
        return item

    def dequeue(self):
        f = self.__queue[0]
        self.__queue.popleft()
        return f

    def peek(self):
        n = len(self.__queue) - 1
        return self.__queue[n]

    def is_empty(self):
        if len(self.__queue) >= 1:
            return False
        else:
            return True
    
    def size(self):
        return len(self.__queue)
    
def radix():
    my_list = input("Enter: ").split()
    max_digit = get_max_digit(my_list)
    digit_queue = [Queue() for i in range(10)]
    num_list = []
    for num in my_list:
        num_list.append(int(num))

    for position in range(max_digit):
        for number in num_list:
            digit = get_digit_from_position(number, position)
            digit_queue[digit].enqueue(number)
        numbers = []
        for queue in digit_queue:
            while not queue.is_empty():
                numbers.append(queue.dequeue())
        num_list = numbers
    return num_list

def get_max_digit(number):
    max_digit = 0
    for num in number:
        if len(num) > max_digit:
            max_digit = len(num)
    return max_digit

def get_digit_from_position(number, position):
    return (number // (10 ** position)) % 10


print(radix())