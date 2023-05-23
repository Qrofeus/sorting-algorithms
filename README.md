# Sorting Algorithms

Python implementations for widely known sorting algorithms. Open the Table-of-Contents (top-left) for complete list of algorithms implemented.\
I am implementing the sorting algorithms as a part of re-learning and creating a modular source available for future usages.

## Using the module

If you need a specific type of sort, copy and paste the specific function(s) from the `sorts.py` file to your code.\
Some algorithms need more than one function to operate, the necessary functions are listed in code blocks under each algorithm title.

Or copy the `sorts.py` file to your project directory as a module file to get access to all the implementations.\
In your project main file import the `sorts.py` module
```python
import sorts
```
Call the specific function you wish to use
```python
sorts.bubble_sort()
```

## Calculating execution times

For timing the sorting algorithms, run the `main.py` file with your intended algorithm. The execution time required for each list to be sorted using the selected sorting-algorithm, will be printed to the console.\
Replace the function call in the decorated function `sorting_function()` with your intended algorithm.
```python
@timer_decor
def sorting_function(arr: list = None):
    try:
-->     sorts.merge_sort(arr=arr)
```

To calculate average overall execution time, find and un-comment the following lines of code in `main.py`
```python
--> execution_times = []

def timer_decor(func):
    def wrapper_func(*args, **kwargs):
-->     execution_times.append(execution_time)

def main():
--> print(f"Average execution time: {sum(execution_times) / repeat:.9f}s")
```
I have added average execution times for my machine below, with following parameters:
```python
arr = list(range(10_000))
repeat = 1_000
```
Before every iteration, the list is shuffled using the `random.shuffle(list)` function available in '**random**' module that comes with normal Python3+ installation. Python's `random.shuffle(list)` uses the [Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle), which runs in O(n) time and is proven to be a perfect shuffle (assuming a good random number generator).\
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

## Implementations

There are 2 parameters that you will need to provide when calling any sorting function from the `sorts.py` file
1. arr -> (required) the list of numbers, that is to be sorted.
2. reverse -> (optional) boolean value, set to 'True' if desired output is descending order.

Some functions may take parameters other than the 2 mentioned above, but they are optional parameter and need not be passed on when calling any such sorting function. Such parameters, either have default values set in-place or are calculated during execution time.

_Click on the titles for explanation of the sorting algorithm_

#
### [Bubble Sort](/Bubble%20Sort)
```python
bubble_sort(arr: list, reverse: bool = False) -> list
```
Loops through the list, pushing the largest value to the end of the list, by comparing it with each element of the list. With each iteration, the number of comparisons shrinks by one.\
**Average Execution Time**: 8.286862 seconds (repeat=10)

#
### [Selection Sort](/Selection%20Sort)
```python
selection_sort(arr: list, reverse: bool = False) -> list
```
Selecting first element, compare with the rest to find the minimum value in the list and swap the minimum value with first element. After each iteration, minimum value is placed in front of the unsorted list, number of comparisons shrinking by one each time.\
**Average Execution Time**: 3.919520 seconds (repeat=10)

#
### [Insertion Sort](/Insertion%20Sort)
```python
insertion_sort(arr: list, reverse: bool = False) -> list
```
We assume that the first element in list is already sorted then, for each following unsorted element, we start comparing it with the elements to it's left and place it when the left element is smaller than it. With each iteration, the elements to the left of current element will be in sorted order.\
**Average Execution Time**: 2.934712 seconds (repeat=10)

#
### [Merge Sort](/Merge%20Sort)
```python
merge_sort(arr: list, reverse: bool = False) -> list | None
```
The MergeSort function repeatedly divides the array into two halves until we reach a stage where we try to perform MergeSort on a subarray of size 1. After that, the merge function comes into play and combines the sorted arrays into larger arrays until the whole array is merged. With this python implementation, all functionalities necessary for this algorithm are contained in a single function.\
**Average Execution Time**: 0.041366 seconds

#
### [Quick Sort](/Quick%20Sort)
```python
partition(arr: list, reverse: bool = False, start_index: int = 0, end_index: int = None) -> int
quick_sort(arr: list, reverse: bool = False, start_index: int = 0, end_index: int = None) -> list | None
```
The list is divided into two sections by selecting a pivot element from the list. While dividing the list, the pivot element is positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot. The left and right sections are also divided using the same approach. This process continues until each subarray contains a single element. At this point the list is sorted. Combine all sections to get sorted list back.\
**Average Execution Time**: 0.089487 seconds

#
### [Counting Sort](/Counting%20Sort)
```python
counting_sort(arr: list[int], reverse: bool = False) -> list
```
After finding the range of values present in the list, create a new counting-list of zeroes with length of list equal to the range of values. Iterating through the unsorted list, increment the value of index in the counting-list, where the index corresponds to the value in unsorted list. To get the sorted list, loop through the counting-list and add the values corresponding to the index as many times as the value for that index in counting-list.\
**Average Execution Time**: 0.003476 seconds

#
### [Bucket Sort](/Bucket%20Sort)
```python
counting_sort(arr: list[int], reverse: bool = False) -> list
bucket_sort(arr: list[int], reverse: bool = False) -> list
```
The unsorted list elements are divided into different buckets, based on the range of values assigned to each bucket. In this implementation, each bucket stores 1/10th of the maximum value inside the unsorted list, producing multiple lists of reduced length. Each bucket is then individually sorted using **any** stable sorting algorithm (counting_sort). The buckets are then merged together to return the sorted list.\
**Average Execution Time**: 0.008285 seconds

#
### [Radix Sort](/Radix%20Sort)
```python
radix_counting(arr: list[str], unit_place: int, reverse: bool = False) -> list
radix_sort(arr: list[int], reverse: bool = False) -> list
```
The unsorted list elements are repeated grouped together for individual digits with the same place values. When grouping the elements, the list elements are sorted for the current unit-place using **any** stable sorting algorithm. This implementation uses counting sort to sort the elements for each iteration of the unit-place. The grouping of the elements occurs with unit-places going from right to left (least to most significant digits).\
**Average Execution Time**: 0.014188 seconds

#
### [Heap Sort](/Heap%20Sort)
```python
def heapify(arr: list, end: int, root: int) -> None:
def heap_sort(arr: list, reverse: bool = False) -> list:
```
Considering the unsorted list as a [binary tree](https://www.geeksforgeeks.org/binary-tree-data-structure/), we create a [max-heap](https://www.geeksforgeeks.org/introduction-to-max-heap-data-structure/) from that binary tree. The maximum element from the heap gets placed at the start of the list-representation of that max-heap. Swapping that maximum element with the last element in the unsorted list, cements the correct position for the max element. Repeating this process again and again for the unsorted parts of the list, creates a growing sorted list from maximum to minimum value.\
**Average Execution Time**: 0.056756 seconds

```python
def heap_sort_mod(arr: list, reverse: bool = False) -> list:
```

Using the [heapq](https://docs.python.org/3.11/library/heapq.html) module from the [Python Standard Library](https://docs.python.org/3.11/library/), the implementation of the heap_sort algorithm is increased by magnitudes. This is due to the fact that the modules inside the Python Standard Library are written in C programing language which is a much faster language than Python. Similar improvements can be achieved for the other sorting algorithms in this list, by using appropriate modules from the Python Standard Library.\
**Average Execution Time (Heapq Module)**: 0.000005980 seconds

#
### [Shell Sort](/Shell%20Sort)
```python
def get_knuth_gaps(size: int) -> list[int]:
def shell_sort(arr: list, reverse: bool = False) -> list:
```
A variation on [Insertion Sort](/Insertion%20Sort), comparing the elements in the list for the right element to be placed at the current position is achieved using a gap sequence, which starts big, decreasing after each full iteration, eventually reaching a gap size of 1. Several methods may be used to generate such gap sequences, they are available on [Wikipedia](https://en.wikipedia.org/wiki/Shellsort#Gap_sequences) to be referenced. This implementation uses Knuth gap sequence [(A003462)](https://oeis.org/A003462).\
**Average Execution Time**: 0.042352 seconds

#
## Comments:

1. For recursive algorithms, for larger lists there is a chance that during execution, maximum-recursion-depth (in Python) may be reached.
   - Python has a default maximum-recursion-depth of 1000. If a function exceeds this limit `RecursionError` is raised.
   - Although not advised, this limit can be increased using `sys.setrecursionlimit(__limit=n)` function.
2. Python works with references when passing data structures as parameters to a function. Therefore, the implementations of the sorting algorithms work as in-place sorting functions. Despite that, all the sorting functions in this implementation return the sorted list explicitly (to be used if ever needed).
   - If you intend to stop Python from modifying the original list, when passing the list as a parameter to the sorting function use `copy.deepcopy(arr)` function. [Python Documentation](https://docs.python.org/3/library/copy.html)
