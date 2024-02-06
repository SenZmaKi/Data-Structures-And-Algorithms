from ..utils import generate_random_list, profile


def coin_row_bruteforce(coins: list[int], idx=0) -> int:
    n = len(coins) - idx
    if n == 0:
        return 0
    if n == 1:
        return coins[idx]
    if n == 2:
        return max(coins[idx], coins[idx + 1])
    max_if_first_is_picked = coins[idx] + coin_row_bruteforce(coins, idx + 2)
    max_if_second_is_picked = coins[idx + 1] + coin_row_bruteforce(coins, idx + 3)
    return max(max_if_first_is_picked, max_if_second_is_picked)


def coin_row_bruteforce_slicing(coins: list[int]) -> int:
    n = len(coins)
    if n == 0:
        return 0
    if n == 1:
        return coins[0]
    if n == 2:
        return max(coins[0], coins[1])
    max_if_first_is_picked = coins[0] + coin_row_bruteforce_slicing(coins[2:])
    max_if_second_is_picked = coins[1] + coin_row_bruteforce_slicing(coins[3:])
    return max(max_if_first_is_picked, max_if_second_is_picked)


def coin_row_memoised(coins: list[int]) -> int:
    n = len(coins)
    if n == 0:
        return 0
    if n == 1:
        return coins[0]
    memo = [0] * n
    memo[0] = coins[0]
    memo[1] = coins[1]
    for idx in range(2, n):
        memo[idx] = max(memo[idx - 1], coins[idx] + memo[idx - 2])
    return memo[n - 1]


def main():
    coins = generate_random_list(60)
    print(coins)
    dynamic_result = profile(
        "Max coin row dynamic", lambda: coin_row_memoised(coins)
    )
    brute_force_result = profile(
        "Max coin row brute force", lambda: coin_row_bruteforce(coins)
    )
    brute_force_slicing_result = profile(
        "Max coin row brute force slicing",
        lambda: coin_row_bruteforce_slicing(coins),
    )
    print(f"Max coin value: {dynamic_result}")
    print(f"Max coin value: {brute_force_result}")
    print(f"Max coin value: {brute_force_slicing_result}")
    assert dynamic_result == brute_force_result == brute_force_slicing_result
    print(f"Max coin value: {dynamic_result}")


if __name__ == "__main__":
    main()

