# Stacks

A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle. Think of it like a stack of plates: the last plate you put on is the first one you take off.

## Key Characteristics:
- **LIFO:** Last element added is the first one to be removed.
- **Operations:** Primarily supports `push` (add an element) and `pop` (remove the top element).
- **Limited Access:** Elements can only be added or removed from one end (the "top" of the stack).

## Common Operations:
- `push(item)`: Adds an item to the top of the stack.
- `pop()`: Removes and returns the item at the top of the stack.
- `peek()` or `top()`: Returns the top item without removing it.
- `isEmpty()`: Checks if the stack is empty.
- `size()`: Returns the number of items in the stack.

## Implementations:

### Python
```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None # Or raise an error for empty stack

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example Usage:
# my_stack = Stack()
# my_stack.push(10)
# my_stack.push(20)
# print(my_stack.peek()) # Output: 20
# print(my_stack.pop())  # Output: 20
# print(my_stack.is_empty()) # Output: False
```

### PHP
```php
<?php

class Stack {
    private $items = [];

    public function push($item) {
        array_push($this->items, $item);
    }

    public function pop() {
        if (!$this->isEmpty()) {
            return array_pop($this->items);
        }
        return null; // Or throw an exception
    }

    public function peek() {
        if (!$this->isEmpty()) {
            return end($this->items);
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
// $myStack = new Stack();
// $myStack->push(10);
// $myStack->push(20);
// echo $myStack->peek() . "\n"; // Output: 20
// echo $myStack->pop() . "\n";  // Output: 20
// echo ($myStack->isEmpty() ? 'True' : 'False') . "\n"; // Output: False

?>
```

### JavaScript
```javascript
class Stack {
    constructor() {
        this.items = [];
    }

    push(item) {
        this.items.push(item);
    }

    pop() {
        if (this.isEmpty()) {
            return null; // Or throw an error
        }
        return this.items.pop();
    }

    peek() {
        if (this.isEmpty()) {
            return null;
        }
        return this.items[this.items.length - 1];
    }

    isEmpty() {
        return this.items.length === 0;
    }

    size() {
        return this.items.length;
    }
}

// Example Usage:
// const myStack = new Stack();
// myStack.push(10);
// myStack.push(20);
// console.log(myStack.peek()); // Output: 20
// console.log(myStack.pop());  // Output: 20
// console.log(myStack.isEmpty()); // Output: false
```

## Tips for LeetCode Amateurs:
- **When to Use:** Stacks are great for problems involving backtracking, parsing expressions (e.g., parentheses matching), and managing function calls (recursion).
- **Browser History:** A classic real-world example is the back button in a web browser, which uses a stack to keep track of visited pages.
- **Recursion to Iteration:** Many recursive algorithms can be converted to iterative ones using a stack.
