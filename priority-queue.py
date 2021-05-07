# Using Binary Heap
# Binary Heaps have exactly 2 children (including null)
# In a complete binary tree, every level before the last is completely filled,
# and the last layer is filled from the left
def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]


def get_smaller_child(heap, idx):
    l = idx * 2 + 1
    r = l + 1
    # default to left
    child_idx = l
    # while right (left inclusive) IS out of bounds
    if r >= len(heap):
        return child_idx
    if heap[l] > heap[r]:
        # select the smaller child
        child_idx = r
    return child_idx

def bubble_up(heap, idx):
    parent_idx = (idx - 1)//2
    while idx > 0 and heap[idx] < heap[parent_idx]:
        swap(heap, idx, parent_idx)
        idx = parent_idx
        parent_idx = (idx - 1)//2


def bubble_down(heap, idx):
    child_idx = get_smaller_child(heap, idx)
    # while left (right inclusive) is NOT out of bounds and parent > child
    while idx * 2 + 1 < len(heap) and heap[idx] > heap[child_idx]:
        swap(heap, idx, child_idx)
        idx = child_idx
        child_idx = get_smaller_child(heap, child_idx)


class HeapPQ:
    def __init__(self):
        self.heap = []


    def insert(self, element):
        self.heap.append(element)
        idx = len(self.heap) - 1
        bubble_up(self.heap, idx)


    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def poll(self):
        if len(self.heap) == 0:
            return None
        # switch the first and last
        swap(self.heap, 0, len(self.heap) - 1)
        # pop the last
        val = self.heap.pop()
        bubble_down(self.heap, 0)
        return val

    def decrease_key(self):
        pass
