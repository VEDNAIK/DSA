class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        print("Element pushed : ", self.tail.data)

    def pop(self):
        if self.head is None:
            return "Queue is Empty"
        if self.head.next is None:
            self.tail = None
        data = self.head
        self.head = self.head.next
        data.next = None
        return data.data

    def peek(self):
        if self.head is None:
            return "Queue is Empty"
        return self.head.data


x = Queue()
print(x.peek())
print(x.push(5))
print(x.push(6))
print(x.peek())
print(x.pop())
print(x.pop())
print(x.pop())

