import random


class NegativeValuesPresent(Exception):
    pass


def bubble_sort(arr: list, reverse: bool = False) -> list:
    """
    Uses bubble-sort algorithm to sort the input list in intended order.
    Order can be specified using parameter -reverse-
    Passing boolean True to -reverse- parameter returns the list sorted in descending order
    :param arr: list - unsorted list
    :param reverse: bool - True if descending order is intended, otherwise False
    :return: list - Sorted in intended order
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


def selection_sort(arr: list, reverse: bool = False) -> list:
    """
    Uses selection-sort algorithm to sort the input list in intended order.
    Order can be specified using parameter -reverse-
    Passing boolean True to -reverse- parameter returns the list sorted in descending order
    :param arr: list - unsorted list
    :param reverse: bool - True if descending order is intended, otherwise False
    :return: list - Sorted in intended order
    """
    for i in range(len(arr) - 1):
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


def insertion_sort(arr: list, reverse: bool = False) -> list:
    """
        Uses insertion-sort algorithm to sort the input list in intended order.
        Order can be specified using parameter -reverse-
        Passing boolean True to -reverse- parameter returns the list sorted in descending order
        :param arr: list - unsorted list
        :param reverse: bool - True if descending order is intended, otherwise False
        :return: list - Sorted in intended order
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


def merge_sort(arr: list, reverse: bool = False) -> list | None:
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
    :return: list - Sorted in intended order
    """
    if len(arr) <= 1:
        return

    mid_index = len(arr) // 2

    # Separate and sort the two halves formed with new_end
    left_list = arr[:mid_index]
    right_list = arr[mid_index:]
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


def partition(arr: list, reverse: bool = False, start_index: int = 0, end_index: int = None) -> int:
    """
    This function will select a random element as pivot in the given range for the list, and rearrange the list having
    all elements smaller than the pivot to it's left and all elements larger to it's right.
    :param arr: list
    :param reverse: bool - True if descending order is intended, else False
    :param start_index: starting index of the range
    :param end_index: last index of the range
    :return: int - index of pivot element
    """
    # Choose a random element from the list as pivot_el and swap it with the last element in the list
    pivot_i = random.randint(start_index, end_index)
    arr[pivot_i], arr[end_index] = arr[end_index], arr[pivot_i]

    # partition the list into two sections, with the last element in the list as the pivot point
    pivot_el = arr[end_index]

    # Pointer for greater(descending)/smaller(ascending) element
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
    arr[i + 1], arr[end_index] = arr[end_index], arr[i + 1]
    return i + 1


def quick_sort(arr: list, reverse: bool = False, start_index: int = 0, end_index: int = None) -> list | None:
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
    :return: list - sorted in intended order
    """
    # This Quick sort implementation does not have a merge functionality that merges two sections into a third
    # Therefore using start_index and end_index to sort the list in-place is used

    # For first function call, last index of the list will be the last element of the list
    # When calling the function recursively, the start and end index will change according to the partitions
    if not end_index:
        end_index = len(arr) - 1

    if end_index <= start_index:
        return

    # The partition functionality is declared in a separate function, to avoid "maximum recursion depth"
    pivot_index = partition(arr=arr, reverse=reverse, start_index=start_index, end_index=end_index)

    # Recursively call the sorting function on the left and right section of the pivot_index
    quick_sort(arr=arr, reverse=reverse, start_index=start_index, end_index=pivot_index - 1)
    quick_sort(arr=arr, reverse=reverse, start_index=pivot_index + 1, end_index=end_index)

    return arr


def counting_sort(arr: list[int], reverse: bool = False) -> list:
    """
    Uses counting-sort algorithm to sort the input list in intended order. Used for lists with numerical elements.
    Order can be specified using parameter -reverse-. Passing boolean True to -reverse- parameter returns the list
    sorted in descending order
    :param arr: list - unsorted list
    :param reverse: bool - True if descending order is intended, otherwise False
    :return: list - Sorted in intended order
    """
    # Find minimum and maximum values in the list
    # Find range of values using the minimum and maximum values
    offset, max_value = min(arr), max(arr)
    list_range = max_value - offset + 1

    # This step of finding minimum and maximum values is important when the list does not start with zero
    # Saving memory of unused indices in counting-list and a few iterations when generating the sorted list

    # Create a count_list of zeros with length equal to the list_range
    # This list will store the number of times each element appeared in the unsorted list
    count_list = [0] * list_range

    # Storing the values in count_list will be with respect to min_value
    for element in arr:
        # Increment the counter for everytime the element appears
        count_list[element - offset] += 1

    # Reset the list 'arr'
    arr = []
    # Check for the intended order
    # For ascending order sorting, iterate through the count_list from left to right
    # For descending order sorting, iterate through the count_list from right to left
    list_iterator = reversed(list(enumerate(count_list))) if reverse else enumerate(count_list)
    for index, value in list_iterator:
        # Add the elements corresponding to the index values in count_list to the list 'arr'
        # Repeatedly add the index value for the count associated with that index
        arr += [(index + offset)] * value
    return arr


def bucket_sort(arr: list[int], reverse: bool = False) -> list:
    """
    Uses bucket-sort algorithm to sort the input list in intended order. Used for lists with numerical elements.
    Order can be specified using parameter -reverse-. Passing boolean True to -reverse- parameter returns the list
    sorted in descending order
    :param arr: list - unsorted list
    :param reverse: bool - True if descending order is intended, otherwise False
    :return: list - Sorted in intended order
    """
    bucket_count = 10
    # Find maximum value in the list, using that find range of values for each bucket
    bucket_range = max(arr) / bucket_count

    # Create list of lists to simulate buckets in which the elements of the unsorted list
    # are stored according to the bucket range calculated above
    buckets = [[] for _ in range(bucket_count)]

    # Iterate through the unsorted list, placing each element in the appropriate bucket, using the bucket_range
    for element in arr:
        bucket_index = int(element // bucket_range)
        buckets[bucket_index].append(element)

    # Sort the individual buckets using any stable sorting algorithm
    # Will be using counting_sort for this implementation
    for i, bucket in enumerate(buckets):
        buckets[i] = counting_sort(arr=bucket, reverse=reverse)

    # Merge all the buckets and return the sorted list
    # There are 4 methods to achieve this -
    # Using nested for loop, Using List comprehension, Using sum() function, Using NumPy module
    return sum(buckets, [])


def radix_counting(arr: list[str], unit_place: int, reverse: bool = False) -> list:
    """
    Separates the elements in to sub-list based on the current unit-place passed through the 'unit_place' parameter.
    Merges the sub-lists back together in the intended order and returns the list sorted for that unit-place
    :param arr: list[str] - unsorted list mapped from int to str with leading zeroes
    :param unit_place: int - current unit-place to be considered from right
    :param reverse: bool - True if descending order is intended, otherwise False
    :return: list[str] - sorted for up-till the current unit-place
    """
    # Create 10 sub-lists for each of the possible numerical values (0-9)
    unit_counts = [[] for _ in range(10)]

    # For each element in the list, add that element to the corresponding sub-list
    # based on the value at the current unit-place
    for num in arr:
        unit_counts[int(num[-unit_place])].append(num)

    # When merging the sub-lists check for the intended order, reverse the buckets if intended order is descending order
    if reverse:
        unit_counts = unit_counts[::-1]

    # Merge the sub-lists together to get the list sorted for current unit_place
    arr = [num for bucket in unit_counts for num in bucket]
    return arr


def radix_sort(arr: list[int], reverse: bool = False) -> list:
    """
    Uses radix-sort algorithm to sort the input list in intended order. Used for lists with numerical elements.
    Order can be specified using parameter -reverse-. Passing boolean True to -reverse- parameter returns the list
    sorted in descending order
    :param arr: list - unsorted list
    :param reverse: bool - True if descending order is intended, otherwise False
    :return: list - Sorted in intended order
    """
    # To make sure this algorithm works as intended, the elements inside the list should be positive integers
    # Integer assertion is done when passing the list as a parameter, and to check for any negative integers,
    # following check is implemented
    if any(val < 0 for val in arr):
        raise NegativeValuesPresent

    # Find the highest unit place of the maximum value in the list
    units = len(str(max(arr)))

    # Convert all elements in the list to string for ease of operation. Working with int, while possible
    # will require dividing element in the list with (10^current-unit) each time it is to be used
    arr = [str(num).zfill(units) for num in arr]
    # Starting from right rearrange the elements in 10 sub-lists (0-9)
    for unit in range(1, units+1):
        arr = radix_counting(arr=arr, unit_place=unit, reverse=reverse)

    # Convert the list back to int values
    arr = list(map(int, arr))
    return arr

# Acknowledgement:
# Adding the reverse check inside the for loops for iterating over the lists, will result in more comparison checks
# performed, rather than if two entirely separate code blocks are written for ascending and descending sorts
