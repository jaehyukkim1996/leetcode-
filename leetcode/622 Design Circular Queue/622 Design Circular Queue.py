class MyCircularQueue(object):

    def __init__(self, k):
        self.size = 0
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.array = [0]*k

    def enQueue(self, value):
        # add elements to the queue
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.max_size
        self.array[self.rear] = value
        self.size += 1

        return True

    def deQueue(self):
        # delete elements in the queue
        if self.isEmpty():
            return False

        self.front = (self.front+1) % self.max_size
        self.size -= 1

        return True


    def Front(self):
        if not self.isEmpty():
            self.array[self.front]
        else:
            return -1

    def Rear(self):
        if not self.isEmpty():
            self.array[self.rear]
        else:
            return -1

    def isEmpty(self):
        return self.size == 0 #checks if the size is 0

    def isFull(self):
        # variable that checks the current size
        # compare the above variable to the size of the queue
        return self.size == size.max_size

    def show(self):
        return self.array

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(4)
obj.enQueue(3)

