# Trees

A tree is a non-linear data structure that simulates a hierarchical tree structure, with a root value and subtrees of children with a parent node, represented as a set of linked nodes.

## Key Characteristics:
- **Hierarchical:** Data is organized in a parent-child relationship.
- **Root Node:** The topmost node in the tree.
- **Edges:** Connections between nodes.
- **Leaves:** Nodes with no children.
- **Subtree:** A tree formed by a node and its descendants.

## Common Tree Types:
- **Binary Tree:** Each node has at most two children (left and right).
- **Binary Search Tree (BST):** A binary tree where the left child contains values less than the parent, and the right child contains values greater than the parent. This allows for efficient searching.
- **AVL Tree:** A self-balancing binary search tree.
- **Red-Black Tree:** Another self-balancing binary search tree.
- **Trie (Prefix Tree):** A tree-like data structure used to store a dynamic set or associative array where the keys are usually strings.

## Implementations (Binary Search Tree Example):

### Python
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if node is None:
            return TreeNode(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        return node

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)

    def inorder_traversal(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements

    def _inorder_recursive(self, node, elements):
        if node:
            self._inorder_recursive(node.left, elements)
            elements.append(node.data)
            self._inorder_recursive(node.right, elements)

# Example Usage:
# bst = BinarySearchTree()
# bst.insert(50)
# bst.insert(30)
# bst.insert(70)
# bst.insert(20)
# bst.insert(40)
# print(bst.inorder_traversal()) # Output: [20, 30, 40, 50, 70]
# print(bst.search(40).data) if bst.search(40) else "Not Found" # Output: 40
```

### PHP
```php
<?php

class TreeNode {
    public $data;
    public $left;
    public $right;

    public function __construct($data) {
        $this->data = $data;
        $this->left = null;
        $this->right = null;
    }
}

class BinarySearchTree {
    public $root;

    public function __construct() {
        $this->root = null;
    }

    public function insert($data) {
        $this->root = $this->_insertRecursive($this->root, $data);
    }

    private function _insertRecursive($node, $data) {
        if ($node === null) {
            return new TreeNode($data);
        }
        if ($data < $node->data) {
            $node->left = $this->_insertRecursive($node->left, $data);
        } elseif ($data > $node->data) {
            $node->right = $this->_insertRecursive($node->right, $data);
        }
        return $node;
    }

    public function search($data) {
        return $this->_searchRecursive($this->root, $data);
    }

    private function _searchRecursive($node, $data) {
        if ($node === null || $node->data === $data) {
            return $node;
        }
        if ($data < $node->data) {
            return $this->_searchRecursive($node->left, $data);
        }
        return $this->_searchRecursive($node->right, $data);
    }

    public function inorderTraversal() {
        $elements = [];
        $this->_inorderRecursive($this->root, $elements);
        return $elements;
    }

    private function _inorderRecursive($node, &$elements) {
        if ($node) {
            $this->_inorderRecursive($node->left, $elements);
            $elements[] = $node->data;
            $this->_inorderRecursive($node->right, $elements);
        }
    }
}

// Example Usage:
// $bst = new BinarySearchTree();
// $bst->insert(50);
// $bst->insert(30);
// $bst->insert(70);
// $bst->insert(20);
// $bst->insert(40);
// print_r($bst->inorderTraversal()); // Output: Array ( [0] => 20 [1] => 30 [2] => 40 [3] => 50 [4] => 70 )
// $foundNode = $bst->search(40);
// echo ($foundNode ? $foundNode->data : "Not Found") . "\n"; // Output: 40

?>
```

### JavaScript
```javascript
class TreeNode {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(data) {
        this.root = this._insertRecursive(this.root, data);
    }

    _insertRecursive(node, data) {
        if (node === null) {
            return new TreeNode(data);
        }
        if (data < node.data) {
            node.left = this._insertRecursive(node.left, data);
        } else if (data > node.data) {
            node.right = this._insertRecursive(node.right, data);
        }
        return node;
    }

    search(data) {
        return this._searchRecursive(this.root, data);
    }

    _searchRecursive(node, data) {
        if (node === null || node.data === data) {
            return node;
        }
        if (data < node.data) {
            return this._searchRecursive(node.left, data);
        }
        return this._searchRecursive(node.right, data);
    }

    inorderTraversal() {
        const elements = [];
        this._inorderRecursive(this.root, elements);
        return elements;
    }

    _inorderRecursive(node, elements) {
        if (node) {
            this._inorderRecursive(node.left, elements);
            elements.push(node.data);
            this._inorderRecursive(node.right, elements);
        }
    }
}

// Example Usage:
// const bst = new BinarySearchTree();
// bst.insert(50);
// bst.insert(30);
// bst.insert(70);
// bst.insert(20);
// bst.insert(40);
// console.log(bst.inorderTraversal()); // Output: [20, 30, 40, 50, 70]
// console.log(bst.search(40) ? bst.search(40).data : "Not Found"); // Output: 40
```

## Tips for LeetCode Amateurs:
- **Recursion is Key:** Many tree problems are elegantly solved using recursion. Understand pre-order, in-order, and post-order traversals.
- **Binary Search Trees (BSTs):** A fundamental tree type. Understand its properties for efficient searching, insertion, and deletion.
- **Balancing:** For large datasets, unbalanced trees can degrade performance to O(n). Self-balancing trees (AVL, Red-Black) maintain O(log n) performance.
- **Tree vs. Graph:** While trees are a type of graph, they have specific properties (no cycles, single root) that simplify many algorithms.
- **Common LeetCode Problems:** Tree traversals, finding min/max, checking if a tree is a BST, finding the lowest common ancestor, and constructing trees from traversals.
