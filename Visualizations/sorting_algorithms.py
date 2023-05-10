import random


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
        if all(arr[i] <= arr[i + 1] for i in range(size - 1)):
            list_sorted = True
        yield arr, [i], [j], []


def exchange_sort(arr: list):
    size = len(arr)
    for i in range(size-1):
        for j in range(i+1, size):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                yield arr, [i], [j], list(range(i))


def brick_sort(arr: list):
    size = len(arr)
    list_sorted = False
    while not list_sorted:
        list_sorted = True
        for i in range(0, size-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                list_sorted = False
                yield arr, [i+1], [], []
        for j in range(1, size-1, 2):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                list_sorted = False
                yield arr, [], [j+1], []


SORTS = {
    "Bubble Sort": bubble_sort,
    "Bogo Sort": bogo_sort,
    "Exchange Sort": exchange_sort,
    "Brick Sort": brick_sort
}
