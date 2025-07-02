# Queues

A queue is a linear data structure that follows the First-In, First-Out (FIFO) principle. Think of it like a line of people waiting: the first person in line is the first one to be served.

## Key Characteristics:
- **FIFO:** First element added is the first one to be removed.
- **Operations:** Primarily supports `enqueue` (add an element to the rear) and `dequeue` (remove an element from the front).
- **Limited Access:** Elements are added at one end (rear/tail) and removed from the other end (front/head).

## Common Operations:
- `enqueue(item)`: Adds an item to the rear of the queue.
- `dequeue()`: Removes and returns the item from the front of the queue.
- `front()` or `peek()`: Returns the front item without removing it.
- `isEmpty()`: Checks if the queue is empty.
- `size()`: Returns the number of items in the queue.

## Implementations:

### Python
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None # Or raise an error for empty queue

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example Usage:
# my_queue = Queue()
# my_queue.enqueue(10)
# my_queue.enqueue(20)
# print(my_queue.front()) # Output: 10
# print(my_queue.dequeue()) # Output: 10
# print(my_queue.is_empty()) # Output: False
```

### PHP
```php
<?php

class Queue {
    private $items = [];

    public function enqueue($item) {
        array_push($this->items, $item);
    }

    public function dequeue() {
        if (!$this->isEmpty()) {
            return array_shift($this->items);
        }
        return null; // Or throw an exception
    }

    public function front() {
        if (!$this->isEmpty()) {
            return reset($this->items);
        }
        return null;
    }

    public function isEmpty() {
        return empty($this->items);
    }

    public function size() {
        return count($this->items);
    }
}

// Example Usage:
// $myQueue = new Queue();
// $myQueue->enqueue(10);
// $myQueue->enqueue(20);
// echo $myQueue->front() . "\n"; // Output: 10
// echo $myQueue->dequeue() . "\n"; // Output: 10
// echo ($myQueue->isEmpty() ? 'True' : 'False') . "\n"; // Output: False

?>
```

### JavaScript
```javascript
class Queue {
    constructor() {
        this.items = [];
    }

    enqueue(item) {
        this.items.push(item);
    }

    dequeue() {
        if (this.isEmpty()) {
            return null; // Or throw an error
        }
        return this.items.shift();
    }

    front() {
        if (this.isEmpty()) {
            return null;
        }
        return this.items[0];
    }

    isEmpty() {
        return this.items.length === 0;
    }

    size() {
        return this.items.length;
    }
}

// Example Usage:
// const myQueue = new Queue();
// myQueue.enqueue(10);
// myQueue.enqueue(20);
// console.log(myQueue.front()); // Output: 10
// console.log(myQueue.dequeue()); // Output: 10
// console.log(myQueue.isEmpty()); // Output: false
```

## Tips for LeetCode Amateurs:
- **When to Use:** Queues are essential for problems involving breadth-first search (BFS) in graphs and trees, managing tasks in a specific order, and simulating real-world waiting lines.
- **Event Handling:** Many event-driven systems use queues to process events in the order they occur.
- **BFS vs. DFS:** Remember that queues are for BFS (level by level traversal), while stacks (or recursion) are for DFS (depth-first traversal).
