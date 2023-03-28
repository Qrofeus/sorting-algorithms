import random


def bubble_sort(arr: list = None, reverse: bool = False):
    """
    Uses bubble-sort algorithm to sort the input list in intended order.
    Order can be specified using parameter -reverse-
    Passing boolean True to -reverse- parameter returns the list sorted in descending order
    :param arr: list - unsorted list
    :param reverse: bool - True if descending order is intended, otherwise False
    :return: list - Sorted in intended order, None (for any non-exit errors during execution)
    """
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


def selection_sort(arr: list = None, reverse: bool = False):
    """
    Uses selection-sort algorithm to sort the input list in intended order.
    Order can be specified using parameter -reverse-
    Passing boolean True to -reverse- parameter returns the list sorted in descending order
    :param arr: list - unsorted list
    :param reverse: bool - True if descending order is intended, otherwise False
    :return: list - Sorted in intended order, None (for any non-exit errors during execution)
    """
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


def insertion_sort(arr: list = None, reverse: bool = False):
    """
        Uses insertion-sort algorithm to sort the input list in intended order.
        Order can be specified using parameter -reverse-
        Passing boolean True to -reverse- parameter returns the list sorted in descending order
        :param arr: list - unsorted list
        :param reverse: bool - True if descending order is intended, otherwise False
        :return: list - Sorted in intended order, None (for any non-exit errors during execution)
    """
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
        arr[step_index + 1] = marked
    return arr


def merge_sort(arr: list = None, reverse: bool = False):
    # Merge Sort like other recursive functions, has a possibility to cause an error with memory usage
    # But that should not be problem with relatively smaller sized lists
    # As the function has a merge action, that takes two lists and combines them into a third, using list slices is
    # preferred, even though it will add to the temporary memory requirement during execution.
    """
    Uses merge-sort algorithm to sort the input list in intended order.
    Order can be specified using parameter -reverse-
    Passing boolean True to -reverse- parameter returns the list sorted in descending order
    :param arr: list - unsorted list
    :param reverse: bool - True if descending order is intended, otherwise False
    :return: list - Sorted in intended order, None (for any non-exit errors during execution)
    """
    if len(arr) <= 1:
        return

    new_end = len(arr) // 2

    # Separate and sort the two halves formed with new_end
    left_list = arr[:new_end]
    right_list = arr[new_end:]
    merge_sort(arr=left_list, reverse=reverse)
    merge_sort(arr=right_list, reverse=reverse)

    # Merging the two halves
    # Merging functionality can be separated into a separate function
    i = j = k = 0
    # k index will be used for merging into original list
    while i < len(left_list) and j < len(right_list):
        # While merging the two lists, check if intended order if descending
        # change the comparisons performed accordingly
        if reverse:
            if left_list[i] >= right_list[j]:
                # Using "greater than or equal" preserves original sequence in-case of matching values
                arr[k] = left_list[i]
                i += 1
            else:
                arr[k] = right_list[j]
                j += 1
        else:
            if left_list[i] <= right_list[j]:
                # Using "less than or equal" preserves original sequence in-case of matching values
                arr[k] = left_list[i]
                i += 1
            else:
                arr[k] = right_list[j]
                j += 1
        k += 1
    # Add the remaining elements in left_list or right_list to original after either one runs-out
    while i < len(left_list):
        arr[k] = left_list[i]
        i += 1
        k += 1
    while j < len(right_list):
        arr[k] = right_list[j]
        j += 1
        k += 1

    return arr


def partition(arr: list = None, reverse: bool = False, start_index: int = 0, end_index: int = None):
    """
    This function will select a random element as pivot in the given range for the list, and rearrange the list having
    all elements smaller than the pivot to it's left and all elements larger to it's right.
    :param arr: list
    :param reverse: bool - True if descending order is intended, else False
    :param start_index: starting index of the range
    :param end_index: last index of the range
    :return: int - index of pivot element
    """
    # partition the list into two sections, with the last element in the list as the pivot point
    pivot_i = random.randint(start_index, end_index)
    pivot_el = arr[pivot_i]
    # To avoid worst case scenarios, this pivot_element may be selected randomly, rather than choosing the last element

    # Pointer for greater(ascending)/smaller(descending) element
    i = start_index - 1

    # Traverse through all element in the list section, and compare each element with pivot
    for j in range(start_index, end_index):
        # Check whether intended order is ascending/descending
        if not reverse:
            if arr[j] <= pivot_el:
                # If element smaller than pivot_element is found swap it with greater element pointed to by 'i'
                # Increment 'i' before swap
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        else:
            if arr[j] >= pivot_el:
                # If element greater than pivot_element is found swap it with greater element pointed to by 'i'
                # Increment 'i' before swap
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
    # Swap pivot element with greater/smaller element pointed by 'i'
    arr[i + 1], arr[pivot_i] = arr[pivot_i], arr[i + 1]
    pivot_i = i + 1
    return pivot_i


def quick_sort(arr: list = None, reverse: bool = False, start_index: int = 0, end_index: int = None):
    # Quick Sort like other recursive functions, has a possibility to cause an error with memory usage
    # But that should not be problem with relatively smaller sized lists
    """
    Uses merge-sort algorithm to sort the input list in intended order.
    Order can be specified using parameter -reverse-
    Passing boolean True to -reverse- parameter returns the list sorted in descending order.
    :param arr: list - unsorted list.
    :param reverse: bool - True if descending order is intended, otherwise False.
    :param start_index: int - first index of list.
    :param end_index: int - last index of list.
    :return: list - sorted in intended order, None (for any non-exit errors during execution)
    """
    # This Quick sort implementation does not have a merge functionality that merges two sections into a third
    # Therefore using start_index and end_index to sort the list in-place is used

    # For first function call, last index of the list will be the last element of the list
    # When calling the function recursively, the start and end index will change according to the partitions
    if not end_index:
        end_index = len(arr) - 1

    if start_index >= end_index:
        return

    # The partition functionality is declared in a separate function, to avoid "maximum recursion depth"
    pivot_index = partition(arr=arr, reverse=reverse, start_index=start_index, end_index=end_index)

    # Recursively call the sorting function on the left and right section of the pivot_index
    quick_sort(arr=arr, reverse=reverse, start_index=start_index, end_index=pivot_index - 1)
    quick_sort(arr=arr, reverse=reverse, start_index=pivot_index + 1, end_index=end_index)

    return arr

# Acknowledgement:
# Adding the reverse check inside the for loops for iterating over the lists, will result in more comparison checks
# performed, rather than if two entirely separate code blocks are written for ascending and descending sorts
