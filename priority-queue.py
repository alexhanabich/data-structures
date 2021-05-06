# Using Binary Heap
# Binary Heaps have exactly 2 children (including null)
# In a complete binary tree, every level before the last is completely filled,
# and the last layer is filled from the left
def swap(lst, a, b):
    lst[a], lst[b] = lst[a], lst[b]


def bubble_up(heap, idx):
    parent_idx = (idx - 1)/2
    while idx > 0 and heap[idx] < heap[parent_idx]:
        swap(heap, idx, parent_idx)
        idx = parent_idx
        parent_idx = (idx - 1)/2


def bubble_down(heap, idx):
    # defaults to left(first element) - see min() documentation
    # left: idx * 2 + 1, right: idx * 2 + 2
    child_idx = min(idx * 2 + 1, idx * 2 + 2)
    swap(heap, 0, len(heap) - 1)
    heap.pop()
    while child_idx < len(heap) - 1 and heap[child_idx] > heap[idx]:
        swap(heap, idx, child_idx)
        idx = child_idx
        child_idx = idx * 2 + 1


class HeapPQ:
    def __init__(self):
        self.heap = []


    def insert(self, element):
        self.heap.append(element)
        idx = len(self.heap) - 1
        bubble_up(self.heap, idx)


    def peek_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def poll_min(self):
        idx = len(self.heap) - 1
        swap(self.heap, 0, idx)
        self.heap.pop
        bubble_down(self.heap, 0)


    def decrease_key(self):
        
