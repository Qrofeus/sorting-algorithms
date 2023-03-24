import sorts
import time
import random


def timer_decor(func):
    def wrapper_func(*args, **kwargs):
        # Precision count limited by the float point precision in python, decided by your current system
        # To check your float precision use --> print(sys.float_info.dig)
        # Use time.perf_counter_ns() which uses integer values in nanoseconds if needed
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        execution_time = end_time - start_time
        # Displays the execution time with 8 decimal place precision
        # Increase the precision by change the x value in --> :.xf
        print(f"Execution time: {execution_time:.10f}s")
        return result

    return wrapper_func


@timer_decor
def sorting_function(arr=None):
    # Change the sorts.* function call with your intended sorting algorithm
    if sorts.bubble_sort(arr):
        # The functions will return the sorted list
        print("Sort Complete")
    else:
        # Or -None- if there is any error in processing
        print("Sort Failed")


if __name__ == '__main__':
    array = [range(1_000_000_000)]
    repeat = 1_000
    for _ in range(repeat):
        random.shuffle(array)
        sorting_function(arr=array)
