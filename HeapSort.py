
# In-place Heap sort
# an optimized version of heap sort
# that does not require additional memory
# since it manipulates the provided array

from advanced.PriorityQueues import HeapBinaryTree

arr = [int(c) for c in input("").split(" ")]

print(HeapBinaryTree.heapSort(arr))
