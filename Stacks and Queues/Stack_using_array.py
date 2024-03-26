class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def peek(self):
        if self.is_empty():
            return "Empty Stack"
        return self.stack[self.top]

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def push(self, data):
        self.stack.append(data)
        self.top = self.top + 1
        print("Item pushed to Stack : ", data)

    def pop(self):
        if self.is_empty():
            return
        self.top = self.top - 1
        return self.stack.pop()


x = Stack()
print(x.is_empty())
print(x.peek())
print(x.push(5))
print(x.push(6))
print(x.peek())
print(x.pop())
print(x.pop())
print(x.is_empty())
print(x.pop())