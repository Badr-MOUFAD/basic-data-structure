from basic.Node import Node


class Tree(Node):
    def __init__(self, data):
        super().__init__(data)
        return

    def getHeight(self):
        if self.left is None and self.right is None:
            return 0

        if self.left is None:
            return 1 + self.right.getHeight()

        if self.right is None:
            return 1 + self.left.getHeight()

        return 1 + max(self.left.getHeight(), self.right.getHeight())

    def __str__(self):
        left = ""
        right = ""

        if self.left is not None:
            left = str(self.left) + " "

        if self.right is not None:
            right = " " + str(self.right)

        return left + str(self.data) + right