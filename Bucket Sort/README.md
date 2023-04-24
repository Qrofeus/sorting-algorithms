# Bucket Sort Algorithm

Bucket Sort is a sorting algorithm that divides the unsorted list elements into several groups called `buckets`. Each bucket is then sorted by using **any** of the suitable sorting algorithms or recursively applying the same bucket algorithm, like the one used in [Radix sort](../Radix%20Sort).

Finally, the sorted buckets are combined to form a final sorted list. This process of Bucket sort can be understood as a **Scatter-Gather approach**.

## Working of Bucket Sort

1. Define the number of buckets that will be used for dividing the list as `bucket_count`. Create `bucket_count` number of lists, that will hold a range of values from the unsorted list.
2. Separate the elements in the list into corresponding buckets, based on some dividing factor like units-place value or bucket-range (maximum/bucket_count).
3. Apply the selected intermediate sorting algorithm to each of the buckets.
4. Merge all the buckets in the intended order, to get the final sorted list.

```
bucket_sort(list)
  create N empty buckets
  bucket-range <- maximum-value / N
  for all elements in list
    (put element into a bucket matching the range)
    add element to bucket no. -> (element / bucket-range)
  for all the buckets
    sort elements in each bucket
  merge all buckets in order
end bucketSort
```

## Python Implementation

```python
def bucket_sort(arr: list[int]) -> list:
    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]
    
    bucket_range = max(arr) / bucket_count
    for element in arr:
        bucket_index = int(element // bucket_range)
        buckets[bucket_index].append(element)
    for i, bucket in enumerate(buckets):
        buckets[i] = counting_sort(arr=bucket)
    
    return sum(buckets, [])
```

## Bucket Sort Complexity

1. Time Complexity:
   - Worst case complexity: `O(n^2)`\
      When there are elements of close range in the list, they are likely to be placed in the same bucket. This may result in some buckets having more elements than others.
   - Best case complexity: `O(n+k)`\
      It occurs when the elements are uniformly distributed in the buckets with a nearly equal number of elements in each bucket.
   - Average case complexity: `O(n)`\
     It occurs when the elements are distributed randomly in the array. Even if the elements are not distributed uniformly, bucket sort runs in linear time.
   
   Time complexity for this algorithm also heavily depends on the intermediate sorting algorithm used, in-turn inheriting the advantages and limitations of that sorting algorithm.
2. Space Complexity: `O(n+k)`\
   All the buckets will collectively hold all the 'n' number of elements in the list. Space complexity, will again vary for the specific intermediate sorting algorithm used.

## Comments

- Because we are using Counting sort as the intermediate sorting algorithm for individual buckets, the input list needs to consist of only integers. To learn more about this constraint, read the [Counting sort explanation](../Counting%20Sort).\
   Other sorting algorithms may be used to allow for floating point values in the unsorted list, one such algorithm popularly used for the intermediate sorting is [Quick sort](../Quick%20Sort).
- After separating the unsorted list into buckets, parallel programming may be used to speed up the sorting process. In this case the number of buckets may be changed to match the number of processing units available, or a multiple of that number. 
