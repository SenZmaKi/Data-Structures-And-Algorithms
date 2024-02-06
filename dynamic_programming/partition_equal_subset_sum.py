from ..utils import profile, generate_random_list


def partition_equal_subset_sum_bruteforce(sub_array: list[int], curr_sum=0) -> bool:
    if not sub_array:
        return False
    if sum(sub_array) == curr_sum:
        return True
    for idx, elem in enumerate(sub_array):
        new_sub_array = sub_array[:]
        new_sub_array.pop(idx)
        if partition_equal_subset_sum_bruteforce(new_sub_array, curr_sum + elem):
            return True
    return False


def partition_equal_subset_sum(
    sub_array: list[int],
    sub_tuple: tuple[int, ...] = (),
    curr_sum=0,
    memo: dict[tuple[int, ...], bool] = {},
) -> bool:
    if not sub_array:
        return False
    if not sub_tuple:
        sub_tuple = tuple(sub_array)
    if (result := memo.get(sub_tuple, None)) is not None:
        return result
    if sum(sub_array) == curr_sum:
        return True
    for idx, elem in enumerate(sub_array):
        new_sub_array = sub_array[:]
        new_sub_array.pop(idx)
        to_add = partition_equal_subset_sum(new_sub_array, tuple(new_sub_array), curr_sum + elem)
        if to_add:
            return True
    memo[sub_tuple] = False
    return False




