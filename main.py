import sorts
import time
import random

execution_times = []


def timer_decor(func):
    def wrapper_func(*args, **kwargs):
        # Precision count limited by the float point precision in python, decided by your current system
        # To check your float precision use --> print(sys.float_info.dig)
        # Use time.perf_counter_ns() which uses integer values in nanoseconds if needed
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        execution_time = end_time - start_time
        execution_times.append(execution_time)

        # Displays the execution time with 9 decimal place precision. Effective display of nanoseconds
        # Increase the precision by change the x value in --> :.xf
        print(f"Execution time: {execution_time:.9f}s")
        return result

    return wrapper_func


@timer_decor
def sorting_function(arr: list = None):
    # Change the sorts.* function call with your intended sorting algorithm
    try:
        sorts.counting_sort(arr=arr)
    except RecursionError:
        print(RecursionError)
        exit(1)


def main():
    array = list(range(20))
    repeat = 1_000
    for _ in range(repeat):
        random.shuffle(array)
        sorting_function(arr=array)
    # Displays the execution time with 9 decimal place precision. Effective display of nanoseconds
    # Increase the precision by change the x value in --> :.xf
    print(f"Average execution time: {sum(execution_times) / repeat:.6f}s")


if __name__ == '__main__':
    main()
