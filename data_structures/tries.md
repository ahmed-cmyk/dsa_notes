# Tries (Prefix Trees)

A Trie (pronounced "try"), also known as a prefix tree, is a tree-like data structure used to store a dynamic set or associative array where the keys are usually strings. Unlike a binary search tree, nodes in a trie do not store the key directly. Instead, the position of a node in the tree defines the key with which it is associated.

## Key Characteristics:
- **Efficient Prefix Matching:** Allows for very fast prefix-based searches.
- **Space-Time Tradeoff:** Can be very space-efficient if many keys share common prefixes, but can be space-inefficient for sparse datasets.
- **No Collisions:** Unlike hash tables, tries do not have key collisions.
- **Alphabet Dependent:** The number of children a node can have depends on the size of the alphabet (e.g., 26 for lowercase English letters).

## Common Operations:
- `insert(word)`: Adds a word to the trie.
- `search(word)`: Checks if a word exists in the trie.
- `startsWith(prefix)`: Checks if any word in the trie starts with a given prefix.

## Implementations:

### Python
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example Usage:
# trie = Trie()
# trie.insert("apple")
# print(trie.search("apple"))    # Output: True
# print(trie.search("app"))      # Output: False
# print(trie.startsWith("app"))  # Output: True
# trie.insert("app")
# print(trie.search("app"))      # Output: True
```

### PHP
```php
<?php

class TrieNode {
    public $children = [];
    public $isEndOfWord = false;
}

class Trie {
    private $root;

    public function __construct() {
        $this->root = new TrieNode();
    }

    public function insert(string $word): void {
        $node = $this->root;
        for ($i = 0; $i < strlen($word); $i++) {
            $char = $word[$i];
            if (!isset($node->children[$char])) {
                $node->children[$char] = new TrieNode();
            }
            $node = $node->children[$char];
        }
        $node->isEndOfWord = true;
    }

    public function search(string $word): bool {
        $node = $this->root;
        for ($i = 0; $i < strlen($word); $i++) {
            $char = $word[$i];
            if (!isset($node->children[$char])) {
                return false;
            }
            $node = $node->children[$char];
        }
        return $node->isEndOfWord;
    }

    public function startsWith(string $prefix): bool {
        $node = $this->root;
        for ($i = 0; $i < strlen($prefix); $i++) {
            $char = $prefix[$i];
            if (!isset($node->children[$char])) {
                return false;
            }
            $node = $node->children[$char];
        }
        return true;
    }
}

// Example Usage:
// $trie = new Trie();
// $trie->insert("apple");
// var_dump($trie->search("apple"));    // Output: bool(true)
// var_dump($trie->search("app"));      // Output: bool(false)
// var_dump($trie->startsWith("app"));  // Output: bool(true)
// $trie->insert("app");
// var_dump($trie->search("app"));      // Output: bool(true)

?>
```

### JavaScript
```javascript
class TrieNode {
    constructor() {
        this.children = {};
        this.isEndOfWord = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    insert(word) {
        let node = this.root;
        for (const char of word) {
            if (!node.children[char]) {
                node.children[char] = new TrieNode();
            }
            node = node.children[char];
        }
        node.isEndOfWord = true;
    }

    search(word) {
        let node = this.root;
        for (const char of word) {
            if (!node.children[char]) {
                return false;
            }
            node = node.children[char];
        }
        return node.isEndOfWord;
    }

    startsWith(prefix) {
        let node = this.root;
        for (const char of prefix) {
            if (!node.children[char]) {
                return false;
            }
            node = node.children[char];
        }
        return true;
    }
}

// Example Usage:
// const trie = new Trie();
// trie.insert("apple");
// console.log(trie.search("apple"));    // Output: true
// console.log(trie.search("app"));      // Output: false
// console.log(trie.startsWith("app"));  // Output: true
// trie.insert("app");
// console.log(trie.search("app"));      // Output: true
```

## Tips for LeetCode Amateurs:
- **When to Use:** Tries are ideal for problems involving dictionaries, autocomplete features, spell checkers, and finding words with common prefixes.
- **Space vs. Time:** While tries offer excellent time complexity for prefix-based operations, they can consume a lot of memory if the dataset is very large and the words don't share many prefixes.
- **Node Structure:** Each node typically represents a character, and its children represent the next possible characters in a word.
- **`is_end_of_word` Flag:** This flag is crucial to distinguish between a prefix that is also a valid word and a prefix that is only part of a longer word.