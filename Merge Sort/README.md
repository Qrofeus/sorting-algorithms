# Merge Sort Algorithm

One of the most popular sorting algorithm that is based on the `Divide-and-Conquer` strategy. The provided unsorted list is repeatedly broken down into two halves, until a single element remains in a half. While merging back, the elements are placed in the intended order.

This is a `Recursive` algorithm, meaning that during the running of this algorithm, it calls the same function for different inputs. Therefore, this recursively called function will need to end its execution before the original function can end. 

## Working of Merge Sort

**merge_sort()** ->
- Base case:
  - Size of list is equal to 1.
  - Return (End function execution).

1. Find the middle index of the list, store the index in `mid`.
2. Recursive call `merge_sort()` for the sub-list -> start-of-list to left-of-mid.
3. Recursive call `merge_sort()` for the sub-list -> mid to end-of-list.
4. Combine the left sub-list and right sub-lists, in the intended order using the `merge()` function

**merge()** ->
1. Iterate through both the sub-lists consecutively.
2. Add the smallest of the current elements from both lists.
3. Repeat until either of the list is exhausted.
4. Add the remaining elements from the other list to the merged list.
```
merge_sort(array, start, end)
    if start > end 
        return
    mid = (start + end)/2
    merge_sort(array, start, mid)
    merge_sort(array, mid, end)
    merge(array, start, mid, end)
end merge_sort
    
merge(array, left-sublist, right-sublist)
    Have we reached the end of any of the arrays?
    No:
        Compare current elements of both arrays 
        Copy smaller element into sorted array
        Move pointer forward of element containing smaller element
    Yes:
        Copy all remaining elements of non-empty array
```

## Python Implementation

```python
def merge_sort(arr: list) -> list | None:
    if len(arr) <= 1:
        return
    mid_index = len(arr) // 2
    
    left_list = arr[:mid_index]
    right_list = arr[mid_index:]
    
    merge_sort(arr=left_list, reverse=reverse)
    merge_sort(arr=right_list, reverse=reverse)
    
    # Merge the left_list and right_list in the intended order
    i = j = k = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            arr[k] = left_list[i]
            i += 1
        else:
            arr[k] = right_list[j]
            j += 1
        k += 1
    while i < len(left_list):
        arr[k] = left_list[i]
        i += 1
        k += 1
    while j < len(right_list):
        arr[k] = right_list[j]
        j += 1
        k += 1
    return arr
```

## Merge Sort Complexity

1. **Time Complexity**:
   - Worst Case Complexity: `O(n*log n)`
   - Best Case Complexity: `O(n*log n)`
   - Average Case Complexity: `O(n*log n)`
2. **Space Complexity**: O(n)

## Comments

- The merge functionality used in the Merge sort algorithm is encouraged to be implemented in a separate function `merge()`, which makes for clean and readable code.
- Being a recursive function, for larger lists, there will be a chance of reaching maximum-recursion-depth(in Python) if proper base case is not defined. The maximum-recursion-depth for python may be altered (not-recommended) using `sys.setrecursionlimit(__limit=n)`.
- A variation of Merge sort is also sometimes used, where the list is recursively broken down into three sections instead of two.
