# Sorting Algorithms

Python implementations for widely known sorting algorithms. 
Open the Table-of-Contents (top-left) for complete list of algorithms implemented.\
I am implementing the sorting algorithms as a part of re-learning and creating a modular source available for future usages.

## Timing the Sorting algorithms

For timing the sorting algorithms, run the `main.py` file with your intended algorithm.\
Replace the function call in the decorated function `sorting_function()` with your intended algorithm.

To calculate average overall execution time, find and un-comment the following lines of code in `main.py`
```python
--> execution_times = []

def timer_decor(func):
    def wrapper_func(*args, **kwargs):
-->     execution_times.append(execution_time)

if __name__ == '__main__':
--> print(f"Average execution time: {sum(execution_times) / repeat:.9f}s")
```
I have added average execution times for my machine below, with following parameters:
```python
arr = list(range(1_000))
repeat = 1_000
```
Before every iteration, the list is shuffled using the `random.shuffle(list)` function available in '**random**' module 
that comes with normal Python3+ installation.\
In case of any errors, check if the imports at the top of the file match the following
```python
import sorts
# for testing the sorting functions defined in 'sorts' module
# sorts.bubble_sort()
import time 
# for time.perf_counter() or time.perf_counter_ns()
import random
# for random.shuffle()
```

## Using the module

If you need a specific type of sort, copy and paste the specific function(s) from the `sorts.py` file to your code.

Or copy the `sorts.py` file to your project directory as a module file to get access to all the implementations.\
In your project file import the `sorts.py` module
```python
import sorts
```
Call the specific function you wish to use

```python
sorts.bubble_sort()
```

## Implementations

Each sorting function will take 2 parameters
1. arr -> the list of numbers, that is to sorted
2. reverse -> boolean value, set to 'True' if desired output is descending order

### Bubble Sort:
```python
bubble_sort(arr: list = None, reverse: bool = False)
```
Loops through the list, pushing the largest value to the end of the list, by comparing it with each element of the list.
With each iteration, the number of comparisons shrinks by one.\
[> Algorithm explanation](/Bubble%20Sort)\
Average Execution Time: 0.083 seconds

### Selection Sort:
```python
selection_sort(arr: list = None, reverse: bool = False)
```
Selecting first element, compare with the rest to find the minimum value in the list and swap the minimum value with 
first element. After each iteration, minimum value is placed in front of the unsorted list, number of comparisons 
shrinking by one each time.\
[> Algorithm explanation](/Selection%20Sort)\
Average Execution Time: 0.036 seconds

### Insertion Sort:
```python
insertion_sort(arr: list = None, reverse: bool = False)
```
We assume that the first element in list is already sorted then, for each following unsorted element, 
we start comparing it with the elements to it's left and place it when the left element is smaller than it. 
With each iteration, the elements to the left of current element will be in sorted order.\
[> Algorithm explanation](/Insertion%20Sort)\
Average Execution Time: 0.030 seconds

### Merge Sort:

```python
merge_sort(arr: list = None, reverse: bool = False)
```
The MergeSort function repeatedly divides the array into two halves until we reach a stage where we try to perform 
MergeSort on a subarray of size 1. After that, the merge function comes into play and combines the sorted arrays into 
larger arrays until the whole array is merged. With this python implementation, all functionalities necessary for this 
algorithm are contained in a single function.\
[> Algorithm Explanation](/Merge%20Sort)\
Average Execution Time: 0.003 seconds

### Quicksort:

### Counting Sort:

### Radix Sort:

### Bucket Sort:

### Heap Sort:

### Shell Sort:
