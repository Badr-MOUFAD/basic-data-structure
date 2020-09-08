from basic.LinkedList import LinkedList


class Stack(LinkedList):
    def __init__(self):
        super().__init__()
        return

    def push(self, element):
        self.pushBack(element)
        return

    def pop(self):
        return self.popBack()