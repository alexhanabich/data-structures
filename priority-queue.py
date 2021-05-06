# Using Binary Heap
# Binary Heaps have exactly 2 children (including null)
# In a complete binary tree, every level before the last is completely filled,
# and the last layer is filled from the left
def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]


def get_smaller_child(heap, idx):
    child_idx = idx * 2 + 1
    if child_idx + 1 >= len(heap):
        return child_idx + 1
    if heap[child_idx] > heap[child_idx + 1]:
        child_idx += 1
    return child_idx

def bubble_up(heap, idx):
    parent_idx = (idx - 1)//2
    while idx > 0 and heap[idx] < heap[parent_idx]:
        swap(heap, idx, parent_idx)
        idx = parent_idx
        parent_idx = (idx - 1)//2


def bubble_down(heap, idx):
    # defaults to left
    # left: idx * 2 + 1, right: idx * 2 + 2
    child_idx = get_smaller_child(heap, idx)
    print('smaller child: ', child_idx)
    while child_idx < len(heap) - 1 and heap[idx] > heap[child_idx]:
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
        swap(self.heap, 0, len(self.heap) - 1)
        val = self.heap.pop()
        bubble_down(self.heap, 0)
        return val

    def decrease_key(self):
        pass
    

pq = HeapPQ()
pq.insert(5)
pq.insert(3)
pq.insert(6)
pq.insert(7)
pq.insert(0)
pq.insert(1)
pq.insert(4)
pq.insert(9)
pq.insert(10)
pq.insert(11)
pq.insert(13)
pq.insert(15)
pq.insert(14)
pq.insert(2)
pq.insert(12)
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)
print(pq.poll())
print(pq.heap)




