from typing import  Callable
from .utils import swap, profile, generate_random_list



def bubble_sort(unsorted: list[int]) -> None:
    sorted_count = 0
    to_sort = len(unsorted) - 1
    for _ in range(to_sort):
        swapped = False
        for idx in range(to_sort - sorted_count):
            if unsorted[idx] > unsorted[idx + 1]:
                swap(unsorted, idx, idx + 1)
                swapped = True
        if not swapped:
            return
        sorted_count += 1


def merge_sort_inplace(unsorted: list[int]) -> None:
    # TODO: Implement
    pass


def merge_sort(unsorted: list[int]) -> list[int]:
    def merge(left: list[int], right: list[int]) -> list[int]:
        left_idx = 0
        right_idx = 0
        sorted: list[int] = []
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                sorted.append(left[left_idx])
                left_idx += 1
            else:
                sorted.append(right[right_idx])
                right_idx += 1
        remaining = left[left_idx:] if left_idx < len(left) else right[right_idx:]
        sorted.extend(remaining)
        return sorted

    def actual_merge_sort(unsorted: list[int]) -> list[int]:
        midpoint = len(unsorted) // 2
        if midpoint == 0:
            return unsorted
        return merge(
            actual_merge_sort(unsorted[:midpoint]),
            actual_merge_sort(unsorted[midpoint:]),
        )

    return actual_merge_sort(unsorted)


def insertion_sort(unsorted: list[int]) -> None:
    for curr_idx, curr in enumerate(unsorted[1:], 1):
        new_idx = curr_idx
        for comp_idx, comp in reversed(list(enumerate(unsorted[:curr_idx]))):
            if comp > curr:
                unsorted[comp_idx + 1] = comp
                new_idx -= 1
            else:
                break
        unsorted[new_idx] = curr


def quick_sort(unsorted: list[int]) -> list[int]:
    if len(unsorted) <= 1:
        return unsorted
    pivot_idx = len(unsorted) - 1
    pivot = unsorted[pivot_idx]
    lesser_nums: list[int] = []
    bigger_nums: list[int] = []
    for num in unsorted[:pivot_idx]:
        lesser_nums.append(num) if num < pivot else bigger_nums.append(num)

    return quick_sort(lesser_nums) + [pivot] + quick_sort(bigger_nums)


def quick_sort_inplace(unsorted: list[int]) -> None:
    def actual_quick_sort(unsorted: list[int], start_idx: int, end_idx: int) -> None:
        pivot = unsorted[end_idx]
        last_less_than_idx = start_idx - 1
        if start_idx >= end_idx:
            return
        for idx in range(start_idx, end_idx):
            if unsorted[idx] < pivot:
                last_less_than_idx += 1
                swap(unsorted, last_less_than_idx, idx)
        new_pivot_idx = last_less_than_idx + 1
        swap(unsorted, new_pivot_idx, end_idx)
        actual_quick_sort(unsorted, start_idx, new_pivot_idx - 1)
        actual_quick_sort(unsorted, new_pivot_idx + 1, end_idx)

    return actual_quick_sort(unsorted, 0, len(unsorted) - 1)


# 1 2 3 4
#
def reverse_num(num: int) -> int:
    rev_num = 0
    while num != 0:
        last_digit = num % 10  # 4 3 2 1
        rev_num = rev_num * 10 + last_digit  # 4 43 432 4321
        num = num // 10  # 123 12 1 0
    return rev_num  # 4321


def reverse_num_hacky(num: int) -> int:
    return int(str(num)[::-1])


def reverse_num_hackest(num: int) -> int:
    return int("".join(reversed(str(num))))


def benchmark_reversing_algorithms() -> None:
    nums = generate_random_list(size=100000000, start=100, stop=10000)

    def runner(algo: Callable[[int], int]):
        for num in nums:
            algo(num)

    profile("Reverse number", lambda: runner(reverse_num))
    profile("Reverse number hacky", lambda: runner(reverse_num_hacky))
    profile("Reverse number hackiest", lambda: runner(reverse_num_hackest))


def benchmark_sorting_algorithms():
    unsorted = generate_random_list(size=10000)
    sorted_builtin_inplace = unsorted[:]
    profile("Builtin inplace sort", lambda: sorted_builtin_inplace.sort())
    sorted_builtin = profile("Builtin sort", lambda: sorted(unsorted))
    sorted_merge = profile("Merge sort", lambda: merge_sort(unsorted))
    sorted_quick_inplace = unsorted[:]
    profile("Quick sort inplace", lambda: quick_sort_inplace(sorted_quick_inplace))
    sorted_quick = profile("Quick sort", lambda: quick_sort(unsorted))
    sorted_bubble = unsorted[:]
    profile("Bubble sort", lambda: bubble_sort(sorted_bubble))
    sorted_insertion = unsorted[:]
    profile("Insertion sort", lambda: insertion_sort(sorted_insertion))
    assert (
        sorted_builtin_inplace
        == sorted_builtin
        == sorted_merge
        == sorted_quick_inplace
        == sorted_quick
        == sorted_bubble
    )


def main() -> None:
    benchmark_reversing_algorithms()
    pass


if __name__ == "__main__":
    main()

