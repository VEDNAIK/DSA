# Optimised

class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        if self.output_stack:
            return self.output_stack.pop()
        else:
            for i in range(len(self.input_stack)):
                self.output_stack.append(self.input_stack.pop())
            return self.output_stack.pop()

    def peek(self) -> int:
        if self.output_stack:
            return self.output_stack[-1]
        else:
            for i in range(len(self.input_stack)):
                self.output_stack.append(self.input_stack.pop())
            return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack
    

'''

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1
'''
