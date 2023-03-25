# Sorting Algorithms

Python implementations for widely known sorting algorithms. Open the Table of Contents (top-left) for complete list.\
I am implementing the sorting algorithms as a part of re-learning and creating a modular source available for future usages.

For timing the sorting algorithms, run the `main.py` file with your intended algorithm.\
Replace the function call in the decorated function `sorting_function()` with your intended algorithm.

## Using the module

If you need a specific type of sort, copy and paste the specific function(s) from the `sorts.py` file to your code.

Or copy the `sorts.py` file to your project directory as a module file to get access to all the implementations.\
In your project file import the `sorts.py` module
```python
import sorts
```
Call the specific function you wish to use

```python
import sorts
sorts.bubble_sort()
```

## Implementations

Each sorting function will take 2 parameters
1. arr -> the list of numbers, that is to sorted
2. reverse -> boolean value, set to 'True' if desired output is descending order

### Bubble Sort:
```
bubble_sort(arr: list = None, reverse: bool = False)
```
Loops through the list, pushing the largest value to the end of the list, by comparing it with each element of the list.
With each iteration, the number of comparisons shrinks by one.\
[> Algorithm explanation](/Bubble%20Sort)

### Selection Sort:
```
selection_sort(arr: list = None, reverse: bool = False)
```
Selecting first element, compare with the rest to find the minimum value in the list and swap the minimum value with 
first element. After each iteration, minimum value is placed in front of the unsorted list, number of comparisons 
shrinking by one each time.\
[> Algorithm explanation](/Selection%20Sort)

### Insertion Sort:

### Merge Sort:

### Quicksort:

### Counting Sort:

### Radix Sort:

### Bucket Sort:

### Heap Sort:

### Shell Sort:
