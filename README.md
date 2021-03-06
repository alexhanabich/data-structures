# Data Structures

Based on a video playlist by WilliamFiset, implemented in Python instead of Java

## Big-O Notation

ex: O(1), O(log(n), O(n), O(nlog(n)), O(n^2), O(n^3), O(b^n), O(n!)

&nbsp;&nbsp;&nbsp;

## Arrays

### Characteristics

- contiguous
- indexable

### Complexity

|        | Static | Dynamic |
|--------|--------|---------|
| Access | O(1)| O(1)|
| Search | O(n)| O(n)|
| Insert | N/A | O(n)|
| Append | N/A | O(1)|
| Delete | N/A | O(n)|

&nbsp;&nbsp;&nbsp;

## Linked List

- can be used to implement
  - queues
  - stack
  - hash table
  - adjacency list
- use 2 iters to remove elements from singly linked list

### Complexity

|        | Single | Double |
|--------|--------|---------|
| Search | O(n)| O(n)|
| Insert(head) | O(1) | O(1)|
| Insert(tail) | O(1) | O(1)|
| Remove(head) | O(1) | O(1)|
| Remove(tail) | O(n) | O(1)|
| Remove(middle) | O(n) | O(n)|

&nbsp;&nbsp;&nbsp;

## Stack

- LIFO
- can be used in
  - iterative DFS
  - recursion
  - matching brackets
  - undo, redo
  - tower of hanoi

### Complexity

|        | Stack |
|--------|--------|
| Push | O(1)|
| Pop | O(1) |
| Peek | O(1) |
| Search | O(n) |

&nbsp;&nbsp;&nbsp;

## Queue

- FIFO
- enqueue to the queue back
- dequeue to the queue front
- used in BFS

### Complexity

|        | Stack |
|--------|--------|
| Enqueue | O(1)|
| Dequeue | O(1) |
| Peek | O(1) |
| Search | O(n) |

&nbsp;&nbsp;&nbsp;

## Priority Queues

- like a queue but certain elements have priority
- uses heap
- can be used in
  - dijkstra's shortest path
  - dynamically get next best or worst
  - huffman coding
  - A*
  - Prim's MST

### Complexity

| | PQ with Binary Heap|
|--------|--------|
| Binary Heap Construction | O(n)|
| Polling | O(nlog(n))|
| Peeking | O(1) |
| Adding | O(nlog(n)) |
| Remove(HashTable) | O(log(n)) |
| Contains(HashTable) | O(1) |

&nbsp;&nbsp;&nbsp;

## Heap

- tree that satisfies 'heap invariant' meaning, child is always smaller than parent or the other way around
- Max heap - parent >= child
- Min heal - parent <= child

## Union Find

- data structure to keep track of elements in disjoint sets
- find -> find the group of element
- union -> union merges two groups
- can be used in
  - Kruscul's MST
  - grid percolation
  - network connectivity
  - least common ancestor in trees
  - image processing

### Complexity

|        | Union Find |
|--------|--------|
| Enqueue | O(n)|
| Dequeue | ??(n) |
| Peek | ??(n) |
| Search | ??(n) |
| Peek | ??(n) |
| Search | O(1) |