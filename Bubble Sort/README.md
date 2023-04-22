# Bubble Sort Algorithm

A sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order. With each iteration the largest element in the active list bubbles to the end of the list.

## Working of Bubble Sort:

Iteration steps -

1. Starting form first index compare the first and second element.
2. If the first element is greater(smaller for descending order) than the second, swap the position of the elements.
3. Now, compare the elements in second and third position, swap them if they are not in the intended order.
4. Repeat the steps until the last position in the list.

These iteration steps are repeated 'n' number of times, 'n' being the size of the list.

```
bubble_sort(array)
  for 0 to sizeof(array)-1
    if left_element > right_element
      swap(left_element, right_element)
end bubble_sort
```

## Python Implementation

```python
def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(0, len(arr) - 2 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

## Bubble Sort Complexity

1. **Time Complexity**:
   - Worst Case Complexity: `O(n<sup>2</sup>)`\
   If we want to sort in ascending order and the array is in descending order then the worst case occurs.
   - Best Case Complexity: `O(n)`\
   If the array is already sorted, then there is no need for sorting.
   - Average Case Complexity: `O(n<sup>2</sup>)`\
   It occurs when the elements of the array are in jumbled order (neither ascending nor descending).
2. **Space Complexity**: `O(1)`

## Comments

- Optimizing Bubble Sort:
    - We can introduce an extra variable `swapped`. The value of `swapped` is set true if there occurs swapping of
      elements. Otherwise, it is set false.
    - After an iteration, if there is no swapping, the value of `swapped` will be false. This means elements are already
      sorted and there is no need to perform further iterations.
