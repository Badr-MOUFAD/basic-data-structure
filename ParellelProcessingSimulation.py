
# modified version of heap (min) binary tree
# it stores objects of the form (thread, job, time)
# object are ranked regarding value

class ModifiedHeapBinaryTree:
    def __init__(self):
        self.arr = []
        return

    def extract(self):
        self.swap(0, len(self) - 1)
        popedElement = self.arr.pop()
        self.shiftDown(0)

        return popedElement

    def insert(self, item):  # item of the form (id, value)
        self.arr.append(item)
        self.shiftUp(len(self) - 1)
        return

    def shiftUp(self, i):
        parent = self.getParent(i)

        if parent[1] is None:
            return

        if self[i][2] < parent[1]:
            self.swap(parent[0], i)
            self.shiftUp(parent[0])
        return

    def shiftDown(self, i):
        leftChild = self.getLeftChild(i)
        rightChild = self.getRightChild(i)

        arr = [child for child in [leftChild, rightChild] if child[1] is not None]
        arr.sort(key=lambda x: x[2])

        if len(arr) == 0:
            return

        if self[i][2] > arr[0][1]:  # smallest element in the array
            self.swap(i, arr[0][0])
            self.shiftDown(arr[0][0])

        return

    def getParent(self, i):
        if i == 0:
            return i, None

        parentIndex = int((i - 1) / 2)
        return parentIndex, self[parentIndex][2]

    def getLeftChild(self, i):
        try:
            childIndex = 2 * i + 1
            return childIndex, self[childIndex][2]
        except:
            return i, None

    def getRightChild(self, i):
        try:
            childIndex = 2 * i + 2
            return childIndex, self[2 * i + 2][2]
        except:
            return i, None

    def swap(self, i, j):
        swapElement = self[i]
        self[i] = self[j]
        self[j] = swapElement
        return

    def __getitem__(self, index):
        return self.arr[index]

    def __setitem__(self, index, value):
        self.arr[index] = value
        return

    def __len__(self):
        return len(self.arr)


def simulateParellelProcessing(nbThreads, arrJobs):
    simualtion = []
    time = 0
    heap = ModifiedHeapBinaryTree()

    for i in range(nbThreads):
        heap.insert((i, i, arrJobs[i]))

    availables = [heap.extract()]

    while heap[0][0] == availables[0]:
        availables.append(heap.extract())

    for actual in availables:
        simualtion.append(actual[0], actual[1], time)

    time += actual[2]
    return