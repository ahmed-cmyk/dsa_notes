# Selection Sort

## Description

Selection Sort is a simple, in-place comparison sorting algorithm. It divides the input list into two parts: a sorted sublist of items built up from left to right at the front (left) of the list and an unsorted sublist of items remaining to be sorted. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

---

## Time Complexity

- **Best Case**: O(n^2)
- **Average Case**: O(n^2)
- **Worst Case**: O(n^2)

---

## Implementation

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

```php
<?php
function selection_sort($arr) {
    $n = count($arr);
    for ($i = 0; $i < $n - 1; $i++) {
        $min_idx = $i;
        for ($j = $i + 1; $j < $n; $j++) {
            if ($arr[$j] < $arr[$min_idx]) {
                $min_idx = $j;
            }
        }
        $temp = $arr[$min_idx];
        $arr[$min_idx] = $arr[$i];
        $arr[$i] = $temp;
    }
    return $arr;
}
?>
```

```javascript
function selectionSort(arr) {
  const n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    let minIdx = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[j] < arr[minIdx]) {
        minIdx = j;
      }
    }
    // Swap the found minimum element with the first element
    [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];
  }
  return arr;
}
```

---

## When to use

- When the data set is small.
- When memory write operations are costly, as it performs a minimum number of swaps among all sorting algorithms (O(n) swaps).

---
