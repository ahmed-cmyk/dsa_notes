# Merge Sort

## Description

Merge Sort is an efficient, comparison-based, divide and conquer sorting algorithm. It divides the unsorted list into n sublists, each containing one element (a list of one element is considered sorted). Then, it repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

---

## Time Complexity

- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)

---

## Implementation

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result
```

```php
<?php
function merge_sort($arr) {
    if (count($arr) <= 1) {
        return $arr;
    }

    $mid = (int)(count($arr) / 2);
    $left_half = array_slice($arr, 0, $mid);
    $right_half = array_slice($arr, $mid);

    $left_half = merge_sort($left_half);
    $right_half = merge_sort($right_half);

    return merge($left_half, $right_half);
}

function merge($left, $right) {
    $result = [];
    $left_idx = 0;
    $right_idx = 0;

    while ($left_idx < count($left) && $right_idx < count($right)) {
        if ($left[$left_idx] < $right[$right_idx]) {
            $result[] = $left[$left_idx];
            $left_idx++;
        } else {
            $result[] = $right[$right_idx];
            $right_idx++;
        }
    }

    while ($left_idx < count($left)) {
        $result[] = $left[$left_idx];
        $left_idx++;
    }

    while ($right_idx < count($right)) {
        $result[] = $right[$right_idx];
        $right_idx++;
    }

    return $result;
}
?>
```

```javascript
function mergeSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const mid = Math.floor(arr.length / 2);
  const leftHalf = arr.slice(0, mid);
  const rightHalf = arr.slice(mid);

  const sortedLeft = mergeSort(leftHalf);
  const sortedRight = mergeSort(rightHalf);

  return merge(sortedLeft, sortedRight);
}

function merge(left, right) {
  let result = [];
  let leftIdx = 0;
  let rightIdx = 0;

  while (leftIdx < left.length && rightIdx < right.length) {
    if (left[leftIdx] < right[rightIdx]) {
      result.push(left[leftIdx]);
      leftIdx++;
    } else {
      result.push(right[rightIdx]);
      rightIdx++;
    }
  }

  return result.concat(left.slice(leftIdx)).concat(right.slice(rightIdx));
}
```

---

## When to use

- When stability is required (maintains the relative order of equal elements).
- When sorting linked lists, as it doesn't require random access.
- When external sorting is needed (data doesn't fit into memory).

---
