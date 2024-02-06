# Requires at least Python 3.11

"""
Question:

11. Investigate the dynamic programming technique. Give two real life problems that they can address. Implement
the two solutions. Use both theoretical and experimental approaches to assess the performance of the algorithms.
"""
from random import randrange
from time import time
from typing import Callable, TypeVar
import sys

T = TypeVar("T")


def generate_random_list(size: int = 100, start=1, stop=100) -> list[int]:
    return [randrange(start, stop + 1) for _ in range(size)]


def profile(task_title: str, task: Callable[[], T]) -> T:
    start_time = time()
    result = task()
    runtime = time() - start_time
    print(f"{task_title}: {runtime} s ")
    return result


def fibonacci_bruteforce(number: int) -> int:
    """
    Finds the fibonnacci series at the `number`, O(2^n)
    """
    if number <= 1:
        return number
    return fibonacci_bruteforce(number - 1) + fibonacci_bruteforce(number - 2)


def fibonacci_memoised(number: int, memo: dict[int, int] = {}) -> int:
    """
    Same as `fibonacci_bruteforce` but O(n)
    """
    result = memo.get(number, None)
    if result is not None:
        return result
    if number <= 1:
        return number
    new_value = fibonacci_memoised(number - 1, memo) + fibonacci_memoised(
        number - 2, memo
    )
    memo[number] = new_value
    return new_value


def coin_change_bruteforce(target_change: int, coins: list[int]) -> int:
    """
    Finds the minimum number of coins needed to construct the target change
    O(n^m) where m is the `target_change` and n is the coin count
    """
    if target_change < 0:
        return -1
    if target_change == 0:
        return 0
    potential_changes = [
        coin_change_bruteforce(target_change - c, coins) for c in coins
    ]
    changes = [pc for pc in potential_changes if pc != -1]
    if not changes:
        return -1
    new_value = min(changes) + 1
    return new_value


def coin_change_memoised(
    target_change: int, coins: list[int], memo: dict[int, int] = {}
) -> int:
    """
    Same as `coin_change_bruteforce` but O(n)
    """
    result = memo.get(target_change, None)
    if result is not None:
        return result
    if target_change < 0:
        return -1
    if target_change == 0:
        return 0
    potential_changes = [
        coin_change_memoised(target_change - c, coins, memo) for c in coins
    ]
    changes = [pc for pc in potential_changes if pc != -1]
    if not changes:
        memo[target_change] = -1
        return -1
    new_value = min(changes) + 1
    memo[target_change] = new_value
    return new_value


def coin_row_bruteforce(coins: list[int]) -> int:
    """
    Finds maximum amount of non-alternating coins that can be picked, O(2^n)
    """
    n = len(coins)
    if n == 0:
        return 0
    if n == 1:
        return coins[0]
    if n == 2:
        return max(coins[0], coins[1])
    max_if_first_is_picked = coins[0] + coin_row_bruteforce(coins[2:])
    max_if_second_is_picked = coins[1] + coin_row_bruteforce(coins[3:])
    return max(max_if_first_is_picked, max_if_second_is_picked)


def coin_row_table(coins: list[int]) -> int:
    """
    Same as `coin_row_bruteforce` but O(n)
    """
    n = len(coins)
    if n == 0:
        return 0
    if n == 1:
        return coins[0]
    table = [0] * n
    table[0] = coins[0]
    table[1] = coins[1]
    for idx in range(2, n):
        table[idx] = max(table[idx - 1], coins[idx] + table[idx - 2])
    return table[n - 1]


def benchmark_coin_change() -> None:
    coins = generate_random_list(50)
    target_change = 50
    profile("Coin change memoised", lambda: coin_change_memoised(target_change, coins))
    profile(
        "Coin change bruteforce", lambda: coin_change_bruteforce(target_change, coins)
    )


def benchmark_coin_row() -> None:
    coins = generate_random_list(60)
    profile("Coin row tabulation", lambda: coin_row_table(coins))
    profile("Coin row brute force", lambda: coin_row_bruteforce(coins))


def benchmark_fibonacci() -> None:
    profile("Fibonacci memoised", lambda: fibonacci_memoised(40))
    profile("Fibonacci brute force", lambda: fibonacci_bruteforce(40))


def main() -> None:
    if sys.version_info[0] < 3 or sys.version_info[1] < 11:
        return print("You need at least Python 3.11 to run this file.\nYou can get it at: https://www.python.org/downloads/release/python-3111/")
    benchmark_coin_change()
    benchmark_coin_row()
    benchmark_fibonacci()

if __name__ == "__main__":
    main()

