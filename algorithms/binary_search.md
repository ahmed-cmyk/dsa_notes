# Binary Search

A binary search has you start the search from the middle of an array. You then compare the current value with the target value and either search from the upper half 
or the lower half of the array.

**NOTE**: Binary search only works when your list has already been sorted.

---

## Time Complexity

O log (n)

---

## Implementation

```python
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
```

```php
<?php
function binary_search($list, $item) {
    $low = 0;
    $high = count($list) - 1;

    while ($low <= $high) {
        $mid = floor(($low + $high) / 2);
        $guess = $list[$mid];
        if ($guess == $item) {
            return $mid;
        }
        if ($guess > $item) {
            $high = $mid - 1;
        } else {
            $low = $mid + 1;
        }
    }
    return null;
}
?>
```

```javascript
function binarySearch(list, item) {
  let low = 0;
  let high = list.length - 1;

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    const guess = list[mid];

    if (guess === item) {
      return mid;
    }
    if (guess > item) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return null;
}
```

## When to use

**When you have:**
- A sorted array
- A single target

---
