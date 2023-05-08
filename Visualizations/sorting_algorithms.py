def bubble_sort(arr: list):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr, [j+1], [], list(range(size-i, size))

