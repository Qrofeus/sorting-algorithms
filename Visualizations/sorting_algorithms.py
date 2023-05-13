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
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
                yield arr, [i+1], list(range(start)), list(range(end+1, size))
        if not swapped:
            break
        end -= 1
        # Backward pass
        swapped = False
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
                yield arr, [i], list(range(start)), list(range(end+1, size))
        start += 1


SORTS = {
    "Bubble Sort": bubble_sort,
    "Bogo Sort": bogo_sort,
    "Exchange Sort": exchange_sort,
    "Brick Sort": brick_sort,
    "Comb Sort": comb_sort,
    "Cocktail Sort": cocktail_sort
}
