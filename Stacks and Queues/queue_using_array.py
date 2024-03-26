class Queue:
    def __init__(self):
        self.head = -1
        self.tail = -1
        self.current_size = 0
        self.maxsize = 5
        self.queue = [0] * self.maxsize

    def push(self, data):
        if self.current_size == self.maxsize:
            return "Queue is full"
        if self.tail == -1:
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.maxsize
        self.queue[self.tail] = data
        print("Element pushed is : ", data)
        self.current_size = self.current_size+1

    def pop(self):
        if self.head == -1:
            return "Queue is Empty"
        item = self.queue[self.head]
        if self.current_size == 1:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head+1) % self.maxsize
        self.current_size = self.current_size - 1
        return item

    def peek(self):
        if self.head == -1:
            return "Queue is Empty"
        else:
            return self.queue[self.head]


x = Queue()
print(x.peek())
print(x.push(5))
print(x.push(6))
print(x.peek())
print(x.pop())
print(x.pop())
print(x.pop())
