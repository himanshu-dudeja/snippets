class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for _ in range(size)]
        self.rear = self.front = -1

    def enqueue(self, data):
        # Case to check if the queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        # Case to check if queue is empty
        elif self.rear == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        # Case to check if queue has some data already present in it.
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        # Case to check if queue is empty
        if self.front == -1:
            print("Queue is empty")
            return
        # Case to check if only 1 element is there in queue
        elif self.front == self.rear:
            self.queue[self.front] = None
            # self.queue.pop(self.front)
            self.rear = self.front = -1
        # Case to check if more elements are there in queue
        else:
            # If we pop the value from here it will be wrong
            # self.queue.pop(self.front)
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size

    def printall(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Printing Queue Values")
            print("~~~~~~~~~~~~~~~~~~~~~")
            tmp_rear = self.rear
            tmp_front = self.front
            while True:
                print(self.queue[tmp_front])
                if tmp_front == tmp_rear:
                    break
                tmp_front = tmp_front + 1
            print("~~~~~~~~~~~~~~~~~~~~~")


c1 = CircularQueue(5)
c1.printall()
c1.enqueue(1)
c1.enqueue(2)
c1.enqueue(3)
c1.printall()
c1.dequeue()
c1.printall()
c1.dequeue()
c1.printall()
c1.dequeue()
c1.printall()
c1.dequeue()
c1.printall()
