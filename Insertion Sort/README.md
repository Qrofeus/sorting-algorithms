# Insertion Sort Algorithm

Considering each element in the unsorted list, it is compared to the elements to the left of itself. That element is
then placed when the element to the left is smaller than it. The sorted list therefore, grows from left to right.

## Working of Insertion Sort

Starting from the second element, iteration steps -

1. Store the value of current-element in `key`.
2. Start comparing the `key` with the values of element to it's left from right side.
3. When an element with value less than `key` is found or start of list is reached, store that index in `target`.
4. Shift the elements right of `target` up-to the position of current-element, one to the right.
5. Place the value held in `key` at `target` index in the list.

Repeat until all the elements in the list are traversed. When end-of-list is reached all the elements will be in the
intended sorted order.

```
insertion_sort(array)
    mark first element as sorted
    for element-X <- unsorted array
        key <- element-X
        for j <- IndexOfelement-X down to 0
        if j > key
            move sorted element to the right by 1
        break loop and insert element-X here
end insertion_sort
```

## Python Implementation

```python
def insertion_sort(arr: list) -> list:
    for mark_index in range(1, len(arr)):
        marked = arr[mark_index]
        step_index = mark_index - 1
        for step_index in range(mark_index-1, -1, -1):
            if marked < arr[step_index]:
                arr[step_index + 1] = arr[step_index]
        arr[step_index + 1] = marked
    return arr
```

## Insertion Sort Complexity

1. **Time Complexity**:
    - Worst Case Complexity: `O(n<sup>2</sup>)`\
    Suppose, an array is in ascending order, and you want to sort it in descending order. In this case, worst case complexity occurs. Each element has to be compared with each of the other elements so, for every nth element, (n-1) number of comparisons are made.
    - Best Case Complexity: `O(n)`\
    When the array is already sorted, the outer loop runs for n number of times whereas the inner loop does not run at all. So, there are only n number of comparisons. Thus, complexity is linear.
    - Average Case Complexity: `O(n<sup>2</sup>)`\
    It occurs when the elements of an array are in jumbled order (neither ascending nor descending).
2. **Space Complexity**: `O(1)`

## Comments

- Better than Selection sort as it does not try to find the minimum from the entire unsorted list. It works only one the current element comparing only with the sorted elements.
