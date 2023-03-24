def bubble_sort(arr: list = None, reverse: bool = False):
    """
    Uses bubble-sort algorithm to sort the input list in intended order.
    Order can be specified using parameter -reverse-
    Passing bool 'True' to -reverse- parameter returns the list sorted in descending order
    :param arr: list
    :param reverse: bool (True/False)
    :return: list (sorted in intended order), None (for any non-exit errors during execution)
    """
    try:
        # Access each element in list
        for i in range(len(arr)):
            # Compare list elements until last iteration position
            for j in range(0, len(arr) - 2 - i):
                # Check whether ascending or descending order is required
                if reverse:
                    # Compare two adjacent elements
                    if arr[j] < arr[j + 1]:
                        # Swap elements they aren't in intended order
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                else:
                    # comparison for less-than changes to greater-than when sorting for ascending order
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    except:
        # Catch all non-exit errors
        # ToDo: Check for specific errors that occur during execution
        return None
