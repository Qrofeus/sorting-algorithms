# Counting Sort Algorithm

Counting sort sorts the elements of a list by counting the number of occurrences of each unique element in the list. The count is stored in an auxiliary list and the sorting is done by mapping the count as an index of the auxiliary list.

## Working of Counting Sort

1. Find the maximum and minimum element in the list. Assign minimum value to a variable `offset`
2. Initialize a `counts` list of zeroes, with length equal to the range (maximum - minimum) of values in the list.
3. Traverse the array, incrementing the value at the index corresponding to the current-element.
   + For each element in the list, subtract the `offset` value from it to obtain the corresponding index in the `counts` list.
   + Increment the value in the `counts` list for that index by 1.
4. Start by traversing the `counts` list, start adding the values corresponding with the indexes, to the sorted array.
   + Add the `offset` value to each index in the `counts` list to get the corresponding value.
   + Repeat that index as many times as the value stored at that index in the `counts` list.
   + Some indexes in the `counts` list may be skipped, if unsorted does not have any value corresponding to that index.

```
counting_sort(arr, n)
   max <- find largest element in list
   offset <- min <- find smallest element in list
   initialize counts array with all zeros of size n

   for j <- 0 to n
      increment the value at (j - offset) index in counts list 
   for i <- 0 to n
      for _ <- 0 to counts[i]
         add (i + offset) to the sorted array
```

## Python Implementation

```python
def counting_sort(arr: list[int]) -> list:
    offset, max_value = min(arr), max(arr)
    list_range = max_value - offset + 1
    count_list = [0] * list_range
    
    for element in arr:
        count_list[element - offset] += 1

    arr = []
    for index, value in enumerate(count_list):
        arr += [(index + offset)] * value
    return arr
```

## Counting Sort Complexity

1. Time Complexity:
   - Worst case complexity: `O(n+k)`
   - Best case complexity: `O(n+k)`
   - Average case complexity: `O(n+k)`\
   The unsorted and `counts` list are traversed once for all cases. Creating the `counts` list, reading-writing to and from the counts list require constant time.
2. Space Complexity: `O(n)`\
   When using the `offset` implementation, an auxiliary list of only size 'n' is required. For normal implementation, an auxiliary list of size equal to the maximum element in the unsorted list will be required `O(max)`

## Comments

- Adding the `offset` variable allows for lists containing negative numbers to be sorted as well, as opposed to the popular implementation of only considering the maximum value when creating the `counts` list.
- This implementation of using `offset` also saves on memory when creating the `counts` list if the minimum element in the list is far from the zero.
