def bubble_sort(arr: list = None, reverse: bool = False):
    """
    Uses bubble-sort algorithm to sort the input list in intended order.
    Order can be specified using parameter -reverse-
    Passing boolean True to -reverse- parameter returns the list sorted in descending order
    :param arr: unsorted list
    :param reverse: True if descending order is intended, otherwise False
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
    # Check for specific errors that occur during execution
    except:
        # Catch all non-exit errors
        return None


def selection_sort(arr: list = None, reverse: bool = False):
    """
    Uses selection-sort algorithm to sort the input list in intended order.
    Order can be specified using parameter -reverse-
    Passing boolean True to -reverse- parameter returns the list sorted in descending order
    :param arr: unsorted list
    :param reverse: True if descending order is intended, otherwise False
    :return: list (sorted in intended order), None (for any non-exit errors during execution)
    """
    try:
        for i in range(len(arr)):
            # Assign the first element of the unsorted list as minimum
            # Maximum in case of descending order sort
            target_index = i
            for j in range(i + 1, len(arr)):
                if reverse:
                    # Look for the maximum value in the unsorted list
                    if arr[j] > arr[target_index]:
                        # The value at index j is larger than target_index
                        # Therefore, update target_index to j
                        target_index = j
                else:
                    # Look for the minimum value in the unsorted list
                    if arr[j] < arr[target_index]:
                        # The value at index j is smaller than target_index
                        # Therefore, update target_index to j
                        target_index = j
            # Swap the elements at the start of the unsorted list 'i' and 'target_index'
            arr[i], arr[target_index] = arr[target_index], arr[i]
        return arr
    except:
        # Catch all non-exit errors
        return None

# Acknowledgement:
# Adding the reverse check inside the for loops for iterating over the lists, will result in more comparison checks
# performed, rather than if two entirely separate code blocks are written for ascending and descending sorts
