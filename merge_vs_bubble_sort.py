from random import randint
from time import time as currentime
from typing import Callable

"""
Below are two sorting algorithms, bubble sort and merge sort
Figure out why merge sort runs waaay faster than bubble sort
You can use Chat GPT and the interwebs and whatnot, gambarte
"""


def merge(left_list: list[int], right_list: list[int]) -> list[int]:
    sorted_list: list[int] = []
    picked_left = 0
    picked_right = 0
    size_left = len(left_list)
    while picked_left < size_left and picked_right < len(right_list):
        left_value, right_value = left_list[picked_left], right_list[picked_right]
        if left_value <= right_value:
            sorted_list.append(left_value)
            picked_left += 1
        else:
            sorted_list.append(right_value)
            picked_right += 1

    remaining = (
        left_list[picked_left:]
        if picked_left < size_left
        else right_list[picked_right:]
    )
    sorted_list.extend(remaining)
    return sorted_list


def merge_sort(unsorted_list: list[int]) -> list[int]:  # O(n log n)
    size = len(unsorted_list)
    if size == 1:
        return unsorted_list
    midpoint = size // 2
    left_list = unsorted_list[:midpoint]
    right_list = lambda: unsorted_list[
        midpoint:
    ]  # To save space we only construct the subarray when we actually need it
    # Cause this a DFS the left side will always be evauluated first
    return merge(merge_sort(left_list), merge_sort(right_list()))


def bubble_sort_optimised(list_to_sort: list[int]) -> list[int]:  # O(n^2)
    list_size = len(list_to_sort)
    swapped = False
    sort_range = list_size - 1
    for sorted_idx in range(list_size):
        for idx in range(sort_range - sorted_idx):  # Biggest performance improvement
            if list_to_sort[idx] > list_to_sort[idx + 1]:
                list_to_sort[idx], list_to_sort[idx + 1] = (
                    list_to_sort[idx + 1],
                    list_to_sort[idx],
                ) 
                swapped = True
        if not swapped:
            break  # OP if list gets fully sorted on an before the last
    return list_to_sort


def bubble_sort(list_to_sort: list[int]) -> list[int]:  # O(n^2)
    list_size = len(list_to_sort)
    for _ in range(list_size - 1):
        for idx in range(list_size - 1):
            if list_to_sort[idx] > list_to_sort[idx + 1]:
                buffer = list_to_sort[idx]
                list_to_sort[idx] = list_to_sort[idx + 1]
                list_to_sort[idx + 1] = buffer
    return list_to_sort


def generate_list(size: int) -> list[int]:
    gen_list: list[int] = []
    for _ in range(size):
        gen_list.append(randint(1, 10))
    return gen_list


def print_runtime_later() -> Callable[[], None]:
    start_time = currentime()
    return lambda: print(f"Runtime: {currentime() - start_time} s")


def main():
    # Try adding one more zero bubble sort wont even finish XD
    unsorted_list = generate_list(100000)
    print("Running merge sort")
    p = print_runtime_later()
    m_sorted_list = merge_sort(unsorted_list)
    p()
    unsorted_list_copy = unsorted_list[:]  # Bubble sort sorts Inplace
    print("Running bubble sort optimised")
    p = print_runtime_later()
    bo_sorted_list = bubble_sort_optimised(unsorted_list)
    p()
    print("Running bubble sort")
    p = print_runtime_later()
    b_sorted_list = bubble_sort(unsorted_list_copy)
    p()

    assert m_sorted_list == b_sorted_list == bo_sorted_list
    # print(f"Unsorted List: {unsorted_list}")
    # print(f"Sorted List: {sorted_list}")


if __name__ == "__main__":
    main()

