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


def insertion_sort(arr: list = None, reverse: bool = False):
    try:
        # First element (single element) will be sorted
        # Therefore start with second element and start comparing backwards
        for mark_index in range(1, len(arr)):
            # Copy the value of current element into marked
            # This allows the elements to the left to take its place when shifted right
            marked = arr[mark_index]
            step_index = mark_index - 1
            # Compare elements to the left until a smaller element is found
            # Start from step_index reduce by 1 with each iteration until -1 to avoid looping back to end of list
            if reverse:
                # For descending order, check for elements until an element larger than marked is reached
                while step_index >= 0 and marked > arr[step_index]:
                    arr[step_index + 1] = arr[step_index]
                    step_index -= 1
            else:
                # For descending order, check for elements until an element larger than marked is reached
                while step_index >= 0 and marked < arr[step_index]:
                    arr[step_index + 1] = arr[step_index]
                    step_index -= 1
            # Place the marked element after the intended element in reached when moving backwards
            arr[step_index+1] = marked
        return arr
    except:
        # Catch all non-exit errors
        return None

# Acknowledgement:
# Adding the reverse check inside the for loops for iterating over the lists, will result in more comparison checks
# performed, rather than if two entirely separate code blocks are written for ascending and descending sorts
