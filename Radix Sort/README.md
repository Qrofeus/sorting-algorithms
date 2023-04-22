# Radix Sort

Radix sort algorithm, sorts the elements by first grouping the individual digits of the same place value, going from smallest to largest place value. When grouping the elements, it sorts them for the digits of the same place value. This process is repeated for all the unit-places, at the end of which the list will be sorted.

The sorting of element for the same place value can be achieved by using any stable sorting algorithm. This implementation uses Counting sort algorithm.

## Working of Radix Sort

1. Find the largest element in the list. The number of digits in the largest element is stored in `max_units`.
2. Modify the list with leading zeros, so that all the elements in the list have `max_units` number of digits.
3. For each unit-place, going from right to left follow the iteration steps-
   - Iterate through the list, add each element to the sub-list corresponding to the digit (0-9) at the current unit-place
   - Combine all the sub-lists to get the sorted list for current unit-place

```
radix_counting(array, unit-place)
    unit_counts <- 10 sub-lists for digits (0-9)
    for each element in array
        add element to unit_counts sub-list matching digit at unit-place
    combine the sub-lists and return the sorted list
    
radix_sort(array)
    max-unit-places <- number of digits in maximum element in list
    for current-unit <- 1 to max-unit-places
        sort the array for each of the current-unit values
    return the sorted array
```

## Python Implementation

```python
def radix_counting(arr: list[str], unit_place: int) -> list:
    unit_counts = [[] for _ in range(10)]

    for num in arr:
        unit_counts[int(num[-unit_place])].append(num)

    arr = [num for bucket in unit_counts for num in bucket]
    return arr


def radix_sort(arr: list[int]) -> list:
    max_units = len(str(max(arr)))

    arr = [str(num).zfill(max_units) for num in arr]
    for unit in range(1, max_units + 1):
        arr = radix_counting(arr=arr, unit_place=unit)
    arr = list(map(int, arr))
    return arr
```

## Radix Sort Complexity

1. Time Complexity:
   - Worst case complexity: `O(n+k)`
   - Best case complexity: `O(n+k)`
   - Average case complexity: `O(n+k)`\
   Since the radix sort uses counting sort as an intermediate stable sort, the time complexity is `O(d(n+k))`. Here, d is the number cycles (unit-places of maximum element in list) and O(n+k) is the time complexity of counting sort.
2. Space Complexity: `O(n)`\
    For each iteration of the intermediate counting sort a list of 10 sub-lists is created where all the elements in the unsorted-list are stored. For this implementation, negligible additional storage may be required for the list when it is converted from int to str. 

## Comments

- Working with floating point and negative numbers can be achieved by converting all the values to positive integers -
     + For floating point numbers, multiplying each element by 10<sup>n</sup> where n is the maximum places after the decimal.
     + For negative number, adding the lowest value to all elements in the list, making zero as the lowest element after conversion.

In both cases after the sorting is complexity, reverse the conversion by dividing or subtracting those values for all elements accordingly.

- In this implementation, the list is converted to string values with leading zeros. While working with integer values is possible, the numbers will need to be divided by 10<sup>current-unit</sup> each time that number is to used in the counting sort portion of this algorithm.