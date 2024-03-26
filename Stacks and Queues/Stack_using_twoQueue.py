from queue import Queue


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.put(x)
        for i in range(self.q1.qsize()):
            self.q2.put(self.q1.get())
        x = self.q1
        self.q1 = self.q2
        self.q2 = x

    def pop(self) -> int:
        return self.q1.get()

    def top(self) -> int:
        return self.q1.queue[0]

    def empty(self) -> bool:
        return self.q1.empty()