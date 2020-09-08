from basic.Node import Node


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.nbNode = 0
        return

    def isEmpty(self):
        if self.nbNode == 0:
            return True

        return False

    def pushFront(self, data):
        if self.isEmpty():
            node = Node(data, left=self.head, right=self.tail)

            self.head.right = node
            self.tail.left = node
        else:
            node = Node(data, left=self.head, right=self.head.right)
            self.head.right.left = node
            self.head.right = node

        self.nbNode += 1
        return

    def popFront(self):
        if self.isEmpty():
            raise Exception("List already empty")

        if self.nbNode == 1:
            popedValue = self.head.right.data

            self.head.right = None
            self.tail.left = None
            self.nbNode = 0

            return popedValue

        popedValue = self.head.right.data
        mostRightNode = self.head.right.right

        mostRightNode.left = self.head
        self.head.right = mostRightNode
        self.nbNode -= 1

        return popedValue

    def pushBack(self, data):
        if self.isEmpty():
            self.pushFront(data)
        else:
            node = Node(data, left=self.tail.left, right=self.tail)
            self.tail.left.right = node
            self.tail.left = node
            self.nbNode += 1

        return

    def popBack(self):
        if self.nbNode < 2:
            return self.popFront()

        popedValue = self.tail.left.data
        mostLeftNode = self.tail.left.left

        mostLeftNode.right = self.tail
        self.tail.left = mostLeftNode
        self.nbNode -= 1

        return popedValue

    def findElement(self, data):
        node = self.head.right

        while node.data is not None and node.right is not None:
            if node.data == data:
                return True

            node = node.right

        return False

    def __str__(self):
        result = []

        node = self.head.right

        while node.data is not None and node.right is not None:
            result.append(node.data)

            node = node.right

        return str(result)