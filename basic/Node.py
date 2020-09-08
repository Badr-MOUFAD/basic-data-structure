# Node object is the build in block
# for creating all the other data structures


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.__left = None
        self.__right = None

        if isinstance(left, (Node, type(None))) and isinstance(right, (Node, type(None))):
            self.left = left
            self.right = right
            return

        raise Exception("left and right properties must be either Node or NoneType")

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        if not isinstance(value, (Node, type(None))):
            raise Exception("Property left must be a Node object")

        self.__left = value
        return

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        if not isinstance(value, (Node, type(None))):
            raise Exception("Property right must be a Node object")

        self.__right = value
        return