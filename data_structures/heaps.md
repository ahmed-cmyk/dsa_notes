# Heaps

A heap is a specialized tree-based data structure that satisfies the heap property. In a max-heap, for any given node C, if P is a parent node of C, then the value of P is greater than or equal to the value of C. In a min-heap, the value of P is less than or equal to the value of C.

## Key Characteristics:
- **Complete Binary Tree:** All levels are completely filled except possibly the last level, which is filled from left to right.
- **Heap Property:** Defines the relationship between parent and child nodes (max-heap or min-heap).
- **Efficient Operations:** Insertion and deletion of the root (min or max element) are O(log n).

## Common Types:
- **Max-Heap:** The root node has the maximum value among all nodes.
- **Min-Heap:** The root node has the minimum value among all nodes.

## Implementations:

### Python
Python's `heapq` module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. It implements a min-heap.
```python
import heapq

# Min-Heap Example
min_heap = []

# Insertion (heappush maintains the heap property)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 5)

print(min_heap) # Output: [5, 10, 20, 30] (internal representation, not necessarily sorted)

# Deletion (heappop removes and returns the smallest element)
print(heapq.heappop(min_heap)) # Output: 5
print(min_heap) # Output: [10, 30, 20]

print(heapq.heappop(min_heap)) # Output: 10
print(min_heap) # Output: [20, 30]

# Accessing the smallest element without removing
print(min_heap[0]) # Output: 20

# Building a heap from a list
list_to_heap = [4, 1, 7, 3, 8, 2]
heapq.heapify(list_to_heap)
print(list_to_heap) # Output: [1, 3, 2, 4, 8, 7]
```

### PHP
PHP does not have a built-in heap data structure, but it can be implemented using `SplPriorityQueue` or by manually managing an array.
```php
<?php

// Using SplPriorityQueue (implements a Max-Heap by default)
$maxHeap = new SplPriorityQueue();
$maxHeap->setExtractFlags(SplPriorityQueue::EXTR_DATA);

// Insert elements with their priorities (higher priority means higher value for max-heap)
$maxHeap->insert(10, 10);
$maxHeap->insert(30, 30);
$maxHeap->insert(20, 20);
$maxHeap->insert(5, 5);

echo "Max-Heap (SplPriorityQueue):\n";
while (!$maxHeap->isEmpty()) {
    echo $maxHeap->extract() . "\n";
}
/* Output:
Max-Heap (SplPriorityQueue):
30
20
10
5
*/

// Manual Min-Heap implementation using an array (simplified for illustration)
class MinHeap {
    private $heap = [];

    public function insert($item) {
        $this->heap[] = $item;
        $this->bubbleUp(count($this->heap) - 1);
    }

    public function extractMin() {
        if (empty($this->heap)) {
            return null;
        }
        if (count($this->heap) === 1) {
            return array_pop($this->heap);
        }
        $min = $this->heap[0];
        $this->heap[0] = array_pop($this->heap);
        $this->bubbleDown(0);
        return $min;
    }

    private function bubbleUp($index) {
        $parentIndex = floor(($index - 1) / 2);
        while ($index > 0 && $this->heap[$parentIndex] > $this->heap[$index]) {
            list($this->heap[$index], $this->heap[$parentIndex]) = array($this->heap[$parentIndex], $this->heap[$index]);
            $index = $parentIndex;
            $parentIndex = floor(($index - 1) / 2);
        }
    }

    private function bubbleDown($index) {
        $leftChildIndex = 2 * $index + 1;
        $rightChildIndex = 2 * $index + 2;
        $smallest = $index;

        if ($leftChildIndex < count($this->heap) && $this->heap[$leftChildIndex] < $this->heap[$smallest]) {
            $smallest = $leftChildIndex;
        }
        if ($rightChildIndex < count($this->heap) && $this->heap[$rightChildIndex] < $this->heap[$smallest]) {
            $smallest = $rightChildIndex;
        }

        if ($smallest !== $index) {
            list($this->heap[$index], $this->heap[$smallest]) = array($this->heap[$smallest], $this->heap[$index]);
            $this->bubbleDown($smallest);
        }
    }

    public function peek() {
        return empty($this->heap) ? null : $this->heap[0];
    }

    public function isEmpty() {
        return empty($this->heap);
    }
}

echo "\nMin-Heap (Manual Implementation):\n";
$minHeap = new MinHeap();
$minHeap->insert(10);
$minHeap->insert(30);
$minHeap->insert(20);
$minHeap->insert(5);

echo $minHeap->extractMin() . "\n"; // Output: 5
echo $minHeap->extractMin() . "\n"; // Output: 10

?>
```

### JavaScript
JavaScript does not have a built-in heap. It can be implemented using an array and simulating the heap operations.
```javascript
class MinHeap {
    constructor() {
        this.heap = [];
    }

    getParentIndex(i) { return Math.floor((i - 1) / 2); }
    getLeftChildIndex(i) { return 2 * i + 1; }
    getRightChildIndex(i) { return 2 * i + 2; }

    hasParent(i) { return this.getParentIndex(i) >= 0; }
    hasLeftChild(i) { return this.getLeftChildIndex(i) < this.heap.length; }
    hasRightChild(i) { return this.getRightChildIndex(i) < this.heap.length; }

    parent(i) { return this.heap[this.getParentIndex(i)]; }
    leftChild(i) { return this.heap[this.getLeftChildIndex(i)]; }
    rightChild(i) { return this.heap[this.getRightChildIndex(i)]; }

    swap(i, j) {
        [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
    }

    peek() {
        if (this.heap.length === 0) return null;
        return this.heap[0];
    }

    insert(item) {
        this.heap.push(item);
        this.heapifyUp();
    }

    extractMin() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        const item = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown();
        return item;
    }

    heapifyUp() {
        let index = this.heap.length - 1;
        while (this.hasParent(index) && this.parent(index) > this.heap[index]) {
            this.swap(this.getParentIndex(index), index);
            index = this.getParentIndex(index);
        }
    }

    heapifyDown() {
        let index = 0;
        while (this.hasLeftChild(index)) {
            let smallerChildIndex = this.getLeftChildIndex(index);
            if (this.hasRightChild(index) && this.rightChild(index) < this.leftChild(index)) {
                smallerChildIndex = this.getRightChildIndex(index);
            }

            if (this.heap[index] < this.heap[smallerChildIndex]) {
                break;
            } else {
                this.swap(index, smallerChildIndex);
            }
            index = smallerChildIndex;
        }
    }

    size() {
        return this.heap.length;
    }

    isEmpty() {
        return this.heap.length === 0;
    }
}

// Example Usage:
// const minHeap = new MinHeap();
// minHeap.insert(10);
// minHeap.insert(30);
// minHeap.insert(20);
// minHeap.insert(5);

// console.log(minHeap.peek()); // Output: 5
// console.log(minHeap.extractMin()); // Output: 5
// console.log(minHeap.peek()); // Output: 10
```

## Tips for LeetCode Amateurs:
- **Priority Queues:** Heaps are commonly used to implement priority queues, where elements are retrieved based on their priority (e.g., smallest or largest).
- **Kth Largest/Smallest Element:** Heaps are very efficient for finding the Kth largest or smallest element in a collection.
- **Heap Sort:** Heaps are the basis for the Heap Sort algorithm, which has O(n log n) time complexity.
- **Median Finder:** Heaps can be used to efficiently find the median of a stream of numbers.
- **Understanding Array Representation:** Heaps are often implemented using arrays, where the parent and child indices can be calculated mathematically. This is crucial for understanding their underlying mechanics.
