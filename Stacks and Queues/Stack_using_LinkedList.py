class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def push(self, data):
        item = StackNode(data)
        item.next = self.top
        self.top = item
        print("Item pushed to Stack : ", data)

    def pop(self):
        if self.is_empty():
            return None
        data = self.top
        self.top = self.top.next
        data.next = None
        return data.data


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


