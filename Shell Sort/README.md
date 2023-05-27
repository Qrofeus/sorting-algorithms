# Shell Sort

Shell sort is a variation of the insertion sort algorithm. It first sorts elements that are far apart from each other and successively reduces the interval between the elements to be sorted. By starting with far apart elements, it can move some out-of-place elements into position faster than a simple nearest neighbor exchange.

The interval between the elements is reduced based on the sequence used. This implementation makes use of Knuth gap sequence [(A003462)](https://oeis.org/A003462). The gaps are calculated using the formula - `(3^k - 1)/2`, where k is the position of element in the gap sequence starting from 1. The gaps not exceeding `ceil(n/3)` for n as the size of the unsorted list. When sorting, starting from the largest gap, decreasing with each iteration, perform insertion sort for that gap in the unsorted list.

## Working of Shell Sort

- Knuth Gap Sequence:
  1. With starting position of `i=1`, start with the first element in the gap sequence using the formula - `(3**i - 1)/2`
  2. Keep adding calculated gaps in the sequence, until the gap size passes `n/3`, where n is the size of the unsorted list.
  3. Return the gap sequence, going from largest to smallest.

```
knuth_gaps(size):
    i <- 1
    gap-sequence <- empty-list()
    gap <- (3**i - 1) / 2
    while 'gap' is less than (size/3):
        add gap to gap-sequence, increment position
        caluclate new gap
    return gap-sequence
```

- Shell Sort:
  1. Generate the Knuth gap sequence for the given unsorted list.
  2. Starting from the largest gap size to the smallest:
     - Perform insertion sort on the unsorted list with the current gap size.

```
shell_sort(arr):
    for interval i <- knuth_gaps(size of arr)
    for each interval "i" in array
        mark first element as sorted
        for element-X <- unsorted array
            key <- element-X
            for j <- IndexOfelement-X down to 0
            if j > key
                move sorted element to the right by 1
            break loop and insert element-X here
```

## Python Implementation

```python
def get_knuth_gaps(size: int) -> list[int]:
    i, gaps = 1, []
    current = ((3 ** i) - 1) // 2
    while current < math.ceil(size/3):
        gaps.append(current)
        i += 1
        current = ((3 ** i) - 1) // 2

    return gaps[::-1]

def shell_sort(arr: list) -> list:
    size = len(arr)
    gap_sequence = get_knuth_gaps(size)

    for gap in gap_sequence:
        for mark_index in range(gap, size):
            current = arr[mark_index]
            j = mark_index
            while current < arr[j - gap] and j >= gap:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = current

    return arr
```

## Complexity of Shell Sort

1. Time Complexity:\
   For many practical variants, determining their time complexity remains an open problem.
   - Worst Case Complexity: `O(n^2)`\
      Worst case complexity for shell sort is always less than or equal to `O(n^2)`.\
      According to [Poonen's Theorem](https://math.mit.edu/~poonen/papers/shell.pdf) (not worth the trouble) worst case complexity for shell sort is `Θ(Nlog N)2/(log log N)2)` or `Θ(Nlog N)2/log log N)` or `Θ(N(log N)2)` or something in between.
   - Best Case Complexity: `O(nlog n)`
   - Average Case Complexity: `O(nlog n)`
2. Space Complexity: `O(1)`

## Comments

- There are several different gap sequences available, that can be used when iterating over the unsorted-list. Among them sequences discovered by the authors Tokuda, Sedgewick and Knuth are one of the more popular sequences used in Shell sort. The Wikipedia [article](https://en.wikipedia.org/wiki/Shellsort#Gap_sequences) lists all the sequences and their formulae used in Shell sort.
- Reference: [Programiz - Shell Sort](https://www.programiz.com/dsa/shell-sort)
