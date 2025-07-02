# Quick Sort

## Description

Quick Sort is a highly efficient, comparison-based sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. This can be done in-place, requiring small additional amounts of memory to perform the sorting.

---

## Time Complexity

- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n^2)

---

## Implementation

```python
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
```

```php
<?php
function quick_sort($arr) {
    if (count($arr) < 2) {
        return $arr;
    }
    $pivot = $arr[0];
    $less = [];
    $greater = [];
    for ($i = 1; $i < count($arr); $i++) {
        if ($arr[$i] <= $pivot) {
            $less[] = $arr[$i];
        } else {
            $greater[] = $arr[$i];
        }
    }
    return array_merge(quick_sort($less), [$pivot], quick_sort($greater));
}
?>
```

```javascript
function quickSort(arr) {
  if (arr.length < 2) {
    return arr;
  }
  const pivot = arr[0];
  const less = arr.slice(1).filter(item => item <= pivot);
  const greater = arr.slice(1).filter(item => item > pivot);
  return [...quickSort(less), pivot, ...quickSort(greater)];
}
```

---

## When to use

- When average-case performance is critical.
- When space complexity is a concern (it's an in-place sort).
- Generally faster than other O(n log n) algorithms in practice due to better cache performance and fewer swaps.

---
