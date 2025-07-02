# Hash Tables (Hash Maps/Dictionaries)

A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

## Key Characteristics:
- **Key-Value Pairs:** Stores data as collections of key-value pairs.
- **Fast Lookups:** Provides average O(1) time complexity for insertion, deletion, and retrieval operations.
- **Hash Function:** Uses a hash function to convert keys into array indices.
- **Collision Handling:** Requires mechanisms to handle collisions (when two different keys hash to the same index).

## Common Collision Resolution Techniques:
- **Separate Chaining:** Each bucket is a linked list, storing all elements that hash to that bucket.
- **Open Addressing:** When a collision occurs, the algorithm probes for another empty slot in the array (e.g., linear probing, quadratic probing, double hashing).

## Implementations:

### Python
Python's `dict` type is implemented as a hash table.
```python
# Python's built-in dictionary is a hash table implementation
my_hash_table = {}

# Insertion
my_hash_table["apple"] = 10
my_hash_table["banana"] = 20
my_hash_table["cherry"] = 30

# Retrieval
print(my_hash_table["banana"]) # Output: 20

# Check if key exists
print("apple" in my_hash_table) # Output: True

# Deletion
del my_hash_table["cherry"]
print(my_hash_table) # Output: {'apple': 10, 'banana': 20}

# Iteration
for key, value in my_hash_table.items():
    print(f"{key}: {value}")
```

### PHP
PHP's arrays can function as hash tables (associative arrays).
```php
<?php

// PHP arrays can be used as hash tables (associative arrays)
$myHashTable = [];

// Insertion
$myHashTable["apple"] = 10;
$myHashTable["banana"] = 20;
$myHashTable["cherry"] = 30;

// Retrieval
echo $myHashTable["banana"] . "\n"; // Output: 20

// Check if key exists
echo (array_key_exists("apple", $myHashTable) ? 'True' : 'False') . "\n"; // Output: True

// Deletion
unset($myHashTable["cherry"]);
print_r($myHashTable);
/* Output:
Array
(
    [apple] => 10
    [banana] => 20
)
*/

// Iteration
foreach ($myHashTable as $key => $value) {
    echo "{$key}: {$value}\n";
}

?>
```

### JavaScript
JavaScript's `Object` and `Map` types can function as hash tables.
```javascript
// Using a plain JavaScript Object as a hash table
const myHashTableObject = {};

// Insertion
myHashTableObject["apple"] = 10;
myHashTableObject["banana"] = 20;
myHashTableObject["cherry"] = 30;

// Retrieval
console.log(myHashTableObject["banana"]); // Output: 20

// Check if key exists
console.log("apple" in myHashTableObject); // Output: true

// Deletion
delete myHashTableObject["cherry"];
console.log(myHashTableObject); // Output: { apple: 10, banana: 20 }

// Iteration
for (const key in myHashTableObject) {
    console.log(`${key}: ${myHashTableObject[key]}`);
}

console.log("\n-- Using JavaScript Map --\n");

// Using JavaScript Map (preferred for general hash table use)
const myHashTableMap = new Map();

// Insertion
myHashTableMap.set("apple", 10);
myHashTableMap.set("banana", 20);
myHashTableMap.set("cherry", 30);

// Retrieval
console.log(myHashTableMap.get("banana")); // Output: 20

// Check if key exists
console.log(myHashTableMap.has("apple")); // Output: true

// Deletion
myHashTableMap.delete("cherry");
console.log(myHashTableMap); // Output: Map(2) { 'apple' => 10, 'banana' => 20 }

// Iteration
myHashTableMap.forEach((value, key) => {
    console.log(`${key}: ${value}`);
});
```

## Tips for LeetCode Amateurs:
- **When to Use:** Hash tables are incredibly useful for problems requiring fast lookups, counting frequencies of elements, checking for duplicates, and implementing caches.
- **Trade-offs:** While average time complexity is O(1), worst-case can be O(n) if there are many collisions and a poor hash function. However, well-implemented hash tables rarely hit worst-case scenarios.
- **Space Complexity:** Hash tables can consume more space than other data structures due to the need for buckets and potential empty slots.
- **Common LeetCode Patterns:
    - **Two Sum:** Often solved efficiently using a hash table to store numbers and their indices.
    - **Counting Frequencies:** Use a hash table to store counts of elements in an array or string.
    - **Grouping Anagrams:** Group words by their sorted character representation (which acts as a key in a hash table).
