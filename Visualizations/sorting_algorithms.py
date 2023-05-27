import math
import random


def check_sorted(arr: list):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def bubble_sort(arr: list):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr, [j + 1], [], list(range(size - i, size))


def bogo_sort(arr: list):
    size = (len(arr))
    list_sorted = False
    while not list_sorted:
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]
        list_sorted = check_sorted(arr)
        yield arr, [i], [j], []


def exchange_sort(arr: list):
    size = len(arr)
    for i in range(size - 1):
        for j in range(i + 1, size):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                yield arr, [i], [j], list(range(i))


def brick_sort(arr: list):
    size = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, size - 1, 2):
            yield arr, [i], [], []
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        for j in range(1, size - 1, 2):
            yield arr, [], [j], []
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True


def comb_sort(arr: list):
    gap = size = len(arr)
    swapped = True
    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False
        for i in range(size - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            yield arr, [i], [i + gap], []


def cocktail_sort(arr: list):
    size = len(arr)
    swapped = True
    start, end = 0, size - 1
    while swapped:
        # Forward pass
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                yield arr, [i + 1], list(range(start)), list(range(end + 1, size))
        if not swapped:
            break
        end -= 1
        # Backward pass
        swapped = False
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                yield arr, [i], list(range(start)), list(range(end + 1, size))
        start += 1


def gnome_sort(arr: list):
    i, size = 0, len(arr)
    while i < size:
        if i == 0 or arr[i] > arr[i - 1]:
            yield arr, [i], [], []
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            yield arr, [], [i - 1], []
            i -= 1


def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i
        while j > 0 and current < arr[j - 1]:
            yield arr, [i], [j], []
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = current
        yield arr, [i], [], [j]


def selection_sort(arr: list):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            yield arr, [min_index], [j], list(range(i))
        arr[i], arr[min_index] = arr[min_index], arr[i]


def find_pos_binary(arr: list, key: int, start: int, end: int):
    if start == end:
        if arr[start] > key:
            return start
        else:
            return start + 1
    elif start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < key:
        return find_pos_binary(arr, key, mid + 1, end)
    elif arr[mid] > key:
        return find_pos_binary(arr, key, start, mid)
    else:
        return mid


def binary_insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = find_pos_binary(arr, key, 0, i - 1)
        yield arr, list(range(i)), [pos], [i]
        arr = arr[:pos] + [key] + arr[pos:i] + arr[i + 1:]


def heapify(arr: list, end: int, curr: int):
    largest = curr
    left = 2 * curr + 1
    right = 2 * curr + 2

    if left < end and arr[curr] < arr[left]:
        largest = left

    if right < end and arr[largest] < arr[right]:
        largest = right

    if largest != curr:
        yield arr, list(range(end)), [curr], [largest]
        arr[curr], arr[largest] = arr[largest], arr[curr]
        yield from heapify(arr, end, largest)


def heap_sort(arr: list):
    size = len(arr)

    for i in range(size // 2, -1, -1):
        yield from heapify(arr, size, i)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        yield from heapify(arr, i, 0)


def knuth_gaps(size: int) -> list[int]:
    i, gaps = 1, []
    current = ((3 ** i) - 1) // 2
    while current < math.ceil(size/3):
        gaps.append(current)
        i += 1
        current = ((3 ** i) - 1) // 2

    return gaps[::-1]


def shell_sort(arr: list):
    size = len(arr)
    gap_sequence = knuth_gaps(size)
    for gap in gap_sequence:
        for i in range(gap, size):
            current = arr[i]
            j = i
            while current < arr[j - gap] and j >= gap:
                yield arr, [i], [], [j - gap]
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = current


SORTS = {
    "Bubble Sort": bubble_sort,
    "Bogo Sort": bogo_sort,
    "Exchange Sort": exchange_sort,
    "Brick Sort": brick_sort,
    "Comb Sort": comb_sort,
    "Cocktail Sort": cocktail_sort,
    "Gnome Sort": gnome_sort,
    "Insertion Sort": insertion_sort,
    "Binary Insertion Sort": binary_insertion_sort,
    "Selection Sort": selection_sort,
    "Heap Sort": heap_sort,
    "Shell Sort": shell_sort
}
