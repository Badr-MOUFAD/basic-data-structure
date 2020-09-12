
class HeapBinaryTree:
    def __init__(self, arr=None):
        self.arr = [] if arr is None else arr
        self.buildHeap()
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
        self.__swap(0, len(self) - 1)
        maxElement = self.arr.pop()
        self.__shiftDown(0)

        return maxElement

    def insert(self, element):
        self.arr.append(element)
        self.__shiftUp(len(self) - 1)
        return

    def changePriority(self, i, newPriority):
        if newPriority > self[i]:
            self[i] = newPriority
            self.__shiftUp(i)
        else:
            self[i] = newPriority
            self.__shiftDown(i)
        return

    def deleteElement(self, i):
        self[i] = self.getMax() + 1
        self.__shiftUp(i)
        self.extractMax()
        return

    def __shiftDown(self, i, boundary=None):
        boundary = len(self) if boundary is None else boundary

        if i >= boundary:
            return

        leftChild = self.getLeftChild(i)
        rightChild = self.getRightChild(i)

        arr = [item for item in [rightChild, leftChild] if item[1] is not None]
        arr.sort(key=lambda x: x[1])

        if len(arr) == 0:
            return

        if arr[-1][1] < self[i]:
            return

        self.__swap(i, arr[-1][0])
        self.__shiftDown(arr[-1][0], boundary)
        return

    def __shiftUp(self, i):
        parent = self.getParent(i)

        if parent[1] is None:
            return

        if parent[1] < self[i]:
            self.__swap(i, parent[0])
            self.__shiftUp(parent[0])

        return

    def __swap(self, i, j):
        swapElement = self[i]
        self[i] = self[j]
        self[j] = swapElement
        return

    def buildHeap(self):
        for i in range(self.getParent(len(self))[0] - 1, -1, -1):
            self.__shiftDown(i)
        return

    def inPlaceHeapSort(self):
        boundary = len(self) - 1

        while boundary >= 0:
            self.__swap(0, boundary)
            self.__shiftDown(0, boundary)
            boundary -= 1
        return

    @staticmethod
    def heapSort(arr):
        H = HeapBinaryTree(arr)
        H.inPlaceHeapSort()
        return H.arr

    # not very efficient
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