# Quick Sort Algorithm

Widely used Quick sort algorithm based on the `Divide-and-Conquer` strategy. This is a `Recursive` algorithm, meaning that during the running of this algorithm, it calls the same function for different inputs.

A list is divided into sub-lists by selecting a pivot element. While dividing the array, elements less than pivot are moved to the left side and elements greater than pivot are moved to the right side of the pivot. The left and right sub-lists are also divided using the same approach. This process continues until each subarray contains a single element. At this point, elements are already sorted. Finally, the sub-lists are combined to form the sorted list.

## Working of Quick Sort

Iteration steps -
1. Select a pivot-element randomly from the active unsorted list.
2. Rearrange the list:
    + The pivot-element is compared with the elements starting from first index.
    + Starting from first index position with a pos-pointer, when an element smaller than pivot is found, swap that element with the element at pos-pointer and increment the pos-pointer.
    + This process is repeated until end-of-list is reached.
    + Place the pivot element after the pos-pointer index.

Repeat the iteration steps, for each of the sub-lists created from the previous iteration. This goes on until the sub-lists contain only a single element, at which point the lists are sorted.

```
partition(arr, start_index, end_index)
   set last element as pivot-element
   target <- start_index - 1
   for i <- start_index to end_index
      if arr[i] < pivot-element
         target++
         swap arr[i] and arr[target]
      swap pivot-element and arr[target+1]
   return target + 1

quick_sort(arr, start_index, end_index)
   if (leftmostIndex < rightmostIndex)
      return
   
   pivotIndex <- partition(arr, start_index, end_index)
   quick_sort(arr, start_index, pivot_index - 1)
   quick_sort(arr, pivot_index, end_index)
```

## Python Implementation

```python
def partition(arr: list, start_index: int = 0, end_index: int = None) -> int:
    pivot_i = random.randint(start_index, end_index)
    pivot_el = arr[pivot_i]
    i = start_index - 1
    for j in range(start_index, end_index):
        if arr[j] <= pivot_el:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[pivot_i] = arr[pivot_i], arr[i + 1]
    pivot_i = i + 1
    return pivot_i

def quick_sort(arr: list, start_index: int = 0, end_index: int = None) -> list | None:
    if not end_index:
        end_index = len(arr) - 1

    if start_index >= end_index:
        return

    pivot_index = partition(arr=arr, reverse=reverse, start_index=start_index, end_index=end_index)
    quick_sort(arr=arr, reverse=reverse, start_index=start_index, end_index=pivot_index - 1)
    quick_sort(arr=arr, reverse=reverse, start_index=pivot_index + 1, end_index=end_index)
    return arr
```

## Quick Sort Complexity

1. Time Complexity:
   - Worst Case Complexity: `O(n<sup>2</sup>)`\
   It occurs when the pivot element picked is either the greatest or the smallest element.
   - Best Case Complexity: `O(n*log n)`\
   It occurs when the pivot element is always the middle element or near to the middle element (in the sorted list).
   - Average Case Complexity: `O(n*log n)`
2. Space Complexity: `O(log n)`

## Comments
