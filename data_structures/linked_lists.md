# Linked Lists

A linked list is a linear data structure where elements are not stored at contiguous memory locations. Instead, each element (node) points to the next element in the sequence.

## Key Characteristics:
- **Dynamic Size:** Can grow or shrink during runtime.
- **Ease of Insertion/Deletion:** Elements can be added or removed without reorganizing the entire structure.
- **No Random Access:** To access an element, you must traverse the list from the beginning.

## Common Types:
- **Singly Linked List:** Each node points to the next node.
- **Doubly Linked List:** Each node points to both the next and previous nodes.
- **Circular Linked List:** The last node points back to the first node.

## Implementations:

### Python
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# Example Usage:
# my_list = LinkedList()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.display() # Output: 1 -> 2 -> 3
```

### PHP
```php
<?php

class Node {
    public $data;
    public $next;

    public function __construct($data) {
        $this->data = $data;
        $this->next = null;
    }
}

class LinkedList {
    public $head;

    public function __construct() {
        $this->head = null;
    }

    public function append($data) {
        $newNode = new Node($data);
        if ($this->head === null) {
            $this->head = $newNode;
            return;
        }
        $lastNode = $this->head;
        while ($lastNode->next !== null) {
            $lastNode = $lastNode->next;
        }
        $lastNode->next = $newNode;
    }

    public function display() {
        $current = $this->head;
        $elements = [];
        while ($current !== null) {
            $elements[] = $current->data;
            $current = $current->next;
        }
        echo implode(" -> ", $elements) . "\n";
    }
}

// Example Usage:
// $myList = new LinkedList();
// $myList->append(1);
// $myList->append(2);
// $myList->append(3);
// $myList->display(); // Output: 1 -> 2 -> 3

?>
```

### JavaScript
```javascript
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    append(data) {
        const newNode = new Node(data);
        if (!this.head) {
            this.head = newNode;
            return;
        }
        let lastNode = this.head;
        while (lastNode.next) {
            lastNode = lastNode.next;
        }
        lastNode.next = newNode;
    }

    display() {
        let current = this.head;
        const elements = [];
        while (current) {
            elements.push(current.data);
            current = current.next;
        }
        console.log(elements.join(" -> "));
    }
}

// Example Usage:
// const myList = new LinkedList();
// myList.append(1);
// myList.append(2);
// myList.append(3);
// myList.display(); // Output: 1 -> 2 -> 3
```

## Tips for LeetCode Amateurs:
- **Understand Pointers/References:** The core concept of linked lists revolves around how nodes point to each other. Master this.
- **Edge Cases:** Pay special attention to handling empty lists, single-node lists, and operations at the beginning or end of the list.
- **Traversal:** Practice traversing linked lists to find, insert, or delete elements.
- **Two-Pointer Technique:** Many linked list problems can be solved efficiently using two pointers (e.g., fast and slow pointers for finding the middle or detecting cycles).
