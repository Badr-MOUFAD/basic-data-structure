from basic.LinkedList import LinkedList


class Queues(LinkedList):
    def __init__(self):
        super().__init__()
        return

    def enqueue(self, element):
        self.pushBack(element)
        return

    def dequeue(self):
        return self.popFront()