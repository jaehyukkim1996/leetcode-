class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(x)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]

    def empty(self):
        return not self.stack1

    def show(self):
        return self.stack1


obj = MyQueue()
obj.push("a")
obj.push("b")
obj.push("c")
obj.push("d")
print(obj.peek())
