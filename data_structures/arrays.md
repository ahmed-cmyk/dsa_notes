# Arrays

An array is a fundamental linear data structure that stores a collection of elements, typically of the same data type, at contiguous memory locations. Each element in an array is identified by an index or a key, usually an integer, representing its position within the array.

## Key Characteristics:
- **Contiguous Memory:** Elements are stored next to each other in memory, allowing for fast access.
- **Fixed or Dynamic Size:**
    - In some languages (like C++, Java), arrays have a fixed size determined at creation.
    - In others (like Python, JavaScript, PHP), arrays (or lists) are dynamic and can grow or shrink.
- **Random Access:** Elements can be accessed directly using their index in O(1) time.
- **Homogeneous (often):** Typically stores elements of the same data type, though some languages allow heterogeneous arrays.

## Common Operations:
- **Access:** `array[index]` to retrieve an element.
- **Insertion:** Adding an element (can be costly if it requires shifting elements).
- **Deletion:** Removing an element (can also be costly).
- **Traversal:** Iterating through all elements.
- **Search:** Finding an element by value.

## Implementations:

### Python
Python lists are dynamic arrays.
```python
# Creating an array (list in Python)
my_array = [1, 2, 3, 4, 5]

# Accessing elements
print(my_array[0]) # Output: 1
print(my_array[2]) # Output: 3

# Modifying elements
my_array[1] = 10
print(my_array) # Output: [1, 10, 3, 4, 5]

# Appending elements
my_array.append(6)
print(my_array) # Output: [1, 10, 3, 4, 5, 6]

# Inserting elements at a specific index (shifts elements)
my_array.insert(2, 99)
print(my_array) # Output: [1, 10, 99, 3, 4, 5, 6]

# Deleting elements
my_array.pop() # Removes last element
print(my_array) # Output: [1, 10, 99, 3, 4, 5]

my_array.pop(1) # Removes element at index 1
print(my_array) # Output: [1, 99, 3, 4, 5]

del my_array[0] # Deletes element at index 0
print(my_array) # Output: [99, 3, 4, 5]

# Slicing
sub_array = my_array[1:3]
print(sub_array) # Output: [3, 4]

# Iteration
for element in my_array:
    print(element)
```

### PHP
PHP arrays are ordered maps, which can be used as both indexed arrays and associative arrays.
```php
<?php

// Creating an array
$myArray = [1, 2, 3, 4, 5];

// Accessing elements
echo $myArray[0] . "\n"; // Output: 1
echo $myArray[2] . "\n"; // Output: 3

// Modifying elements
$myArray[1] = 10;
print_r($myArray);
/* Output:
Array
(
    [0] => 1
    [1] => 10
    [2] => 3
    [3] => 4
    [4] => 5
)
*/

// Appending elements
$myArray[] = 6;
print_r($myArray);

// Inserting elements at a specific index (can be complex, often involves array_splice)
array_splice($myArray, 2, 0, 99);
print_r($myArray);

// Deleting elements
array_pop($myArray); // Removes last element
print_r($myArray);

unset($myArray[1]); // Removes element at index 1, leaves gap in keys
print_r($myArray);

// Re-index array after deletion if needed
$myArray = array_values($myArray);
print_r($myArray);

// Slicing
$subArray = array_slice($myArray, 1, 2);
print_r($subArray);

// Iteration
foreach ($myArray as $element) {
    echo $element . "\n";
}

?>
```

### JavaScript
JavaScript arrays are dynamic and can hold elements of different types.
```javascript
// Creating an array
let myArray = [1, 2, 3, 4, 5];

// Accessing elements
console.log(myArray[0]); // Output: 1
console.log(myArray[2]); // Output: 3

// Modifying elements
myArray[1] = 10;
console.log(myArray); // Output: [1, 10, 3, 4, 5]

// Appending elements
myArray.push(6);
console.log(myArray); // Output: [1, 10, 3, 4, 5, 6]

// Inserting elements at a specific index (shifts elements)
myArray.splice(2, 0, 99);
console.log(myArray); // Output: [1, 10, 99, 3, 4, 5, 6]

// Deleting elements
myArray.pop(); // Removes last element
console.log(myArray); // Output: [1, 10, 99, 3, 4, 5]

myArray.splice(1, 1); // Removes 1 element at index 1
console.log(myArray); // Output: [1, 99, 3, 4, 5]

// Slicing
const subArray = myArray.slice(1, 3);
console.log(subArray); // Output: [99, 3]

// Iteration
for (const element of myArray) {
    console.log(element);
}
```

## Tips for LeetCode Amateurs:
- **Foundation:** Arrays are the most basic and frequently used data structure. A strong understanding is crucial.
- **Two-Pointer Technique:** Many array problems can be solved efficiently using two pointers (e.g., finding pairs, sorting, reversing).
- **Sliding Window:** Useful for problems involving subarrays or substrings of a fixed or variable size.
- **Prefix Sums:** Can optimize problems that require repeated sum calculations over ranges.
- **Sorting:** Often, sorting an array can simplify a problem significantly, even if sorting itself takes O(N log N) time.
- **In-Place Operations:** Be mindful of modifying arrays in-place versus creating new ones, especially for space complexity.
- **Edge Cases:** Always consider empty arrays, single-element arrays, and arrays with duplicate values.
