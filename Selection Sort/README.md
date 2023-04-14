# Selection Sort Algorithm

The selection sort algorithm selects the smallest element in the unsorted list and places it at the beginning. This process is repeated for as many times as elements in the list. 

## Working of Selection Sort

Iteration steps -
1. Select the first element as `minimum`.
2. Compare the `minimum` with the rest of the elements, if any element is smaller than `minimum`, assign the value of that element to `minimum`.
3. Place the `minimum` element at the start of the list.

These iteration steps are repeated 'n' number of times, 'n' being the size of the list.

```
selection_sort(array)
    repeat (sizeof(array) - 1) times
        current_min <- first_element
        for each of the unsorted elements
            if element < current_min
                current_min <- element
        swap(first_element, current_min)
end selection_sort
```

## Python Implementation

```python
def selection_sort(arr: list) -> list:
    for i in range(len(arr) - 1):
        target_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[target_index]:
                target_index = j
        arr[i], arr[target_index] = arr[target_index], arr[i]
    return arr
```

## Selection Sort Complexity

1. **Time Complexity:**
   - Worst Case Complexity: `O(n^2)`\
   If we want to sort in ascending order and the array is in descending order then, the worst case occurs.
   - Best Case Complexity: `O(n^2)`\
   It occurs when the array is already sorted
   - Average Case Complexity: `O(n^2)`\
   It occurs when the elements of the array are in jumbled order (neither ascending nor descending).
2. **Space Complexity**: `O(1)`

## Comments

- The time complexity of the selection sort is the same in all cases, because, you have to find the minimum element for each iteration. The minimum element is not known until the end of the array.
- Selection sort saves time as compared to Bubble sort by skipping most of the swapping of elements, as the elements are swapped only once per iteration.
