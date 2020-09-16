

class HeapBinaryTree:
    def __init__(self, arr=None, priority="max"):
        self.arr = [] if arr is None else arr

        # for solving the problem
        self.nbSwaps = 0
        self.arrSwaps = []

        self.__priority = "max"
        self.priority = priority
        return

    def __getitem__(self, index):
        return self.arr[index]

    def __setitem__(self, index, value):
        self.arr[index] = value
        return

    def __len__(self):
        return len(self.arr)

    def getHeight(self):
        leftChild = self.getLeftChild(0)
        height = 0

        while leftChild[1] is not None:
            height += 1
            leftChild = self.getLeftChild(leftChild[0])

        return height

    def getParent(self, i):
        if i == 0:
            return i, None

        parentIndex = int((i - 1) / 2)
        return parentIndex, self[parentIndex]

    def getLeftChild(self, i):
        try:
            childIndex = 2 * i + 1
            return childIndex, self[childIndex]
        except:
            return i, None

    def getRightChild(self, i):
        try:
            childIndex = 2 * i + 2
            return childIndex, self[2 * i + 2]
        except:
            return i, None

    def getMax(self):
        return self[0]

    def extractMax(self):
        self.swap(0, len(self) - 1)
        maxElement = self.arr.pop()
        self.shiftDown(0)

        return maxElement

    def insert(self, element):
        self.arr.append(element)
        self.shiftUp(len(self) - 1)
        return

    def changePriority(self, i, newValue):
        if self.priority == "max":
            if newValue > self[i]:
                self[i] = newValue
                self.shiftUp(i)
            else:
                self[i] = newValue
                self.shiftDown(i)
        else:
            if newValue > self[i]:
                self[i] = newValue
                self.shiftDown(i)
            else:
                self[i] = newValue
                self.shiftUp(i)
        return

    def deleteElement(self, i):
        self[i] = self.getMax() + 1
        self.shiftUp(i)
        self.extractMax()
        return

    def shiftDown(self, i, boundary=None):
        boundary = len(self) if boundary is None else boundary

        if i >= boundary:
            return

        leftChild = self.getLeftChild(i)
        rightChild = self.getRightChild(i)

        arr = [item for item in [rightChild, leftChild] if item[1] is not None and item[0] < boundary]

        if len(arr) == 0:
            return

        arr.sort(key=lambda x: x[1])
        if self.priority == "max":
            if arr[-1][1] < self[i]:
                return

            self.swap(i, arr[-1][0])
            self.shiftDown(arr[-1][0], boundary)
        else:
            if self[i] < arr[0][1]:
                return

            self.swap(i, arr[0][0])
            self.shiftDown(arr[0][0], boundary)
        return

    def shiftUp(self, i):
        parent = self.getParent(i)

        if parent[1] is None:
            return

        if self.priority == "max":
            if parent[1] < self[i]:
                self.swap(i, parent[0])
                self.shiftUp(parent[0])
        else:
            if self[i] < parent[1]:
                self.swap(i, parent[0])
                self.shiftUp(parent[0])
        return

    def swap(self, i, j):
        # for solving the problem
        self.nbSwaps += 1
        self.arrSwaps.append(("{0} {1}".format(i, j)))

        swapElement = self[i]
        self[i] = self[j]
        self[j] = swapElement
        return

    def buildHeap(self):
        if len(self) == 0:
            return

        for i in range(self.getParent(len(self) - 1)[0], -1, -1):
            self.shiftDown(i)
        return

    def inPlaceHeapSort(self):
        boundary = len(self) - 1

        while boundary > 0:
            self.swap(0, boundary)
            self.shiftDown(0, boundary)
            boundary -= 1

        return

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, value):
        if value not in ["max", "min"]:
            raise Exception("Property priority can be either max or min")

        self.__priority = value
        self.buildHeap()
        return

    @staticmethod
    def heapSort(arr, reverse=False):
        priority = "min" if reverse else "max"

        h = HeapBinaryTree(arr, priority=priority)
        h.inPlaceHeapSort()

        return h.arr

    # not very efficient (over use of memory)
    @staticmethod
    def deprecatedHeapSort(arr, reverse=False):
        H = HeapBinaryTree()
        result = []

        for element in arr:
            H.insert(element)

        while len(H) != 0:
            result.append(H.extractMax())

        if reverse:
            return result

        return result[-1:0:-1] + [result[0]]


n = int(input(""))
arr = [int(c) for c in input("").split(" ")]

h = HeapBinaryTree(arr=arr, priority="min")

print(h.nbSwaps)
for swap in h.arrSwaps:
    print(swap)
