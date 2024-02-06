def coin_change(amount: int, coins: list[int], memo: dict[int, int] = {}) -> int:
    result = memo.get(amount, None)
    if result is not None:
        return result
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    potential_changes = [coin_change(amount - c, coins, memo) for c in coins]
    potential_changes = [pc for pc in potential_changes if pc != -1]
    if not potential_changes:
        memo[amount] = -1
        return -1
    to_add = min(potential_changes) + 1
    memo[amount] = to_add
    return to_add


def coin_change_brute_force(amount: int, coins: list[int]) -> int:
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    potential_changes = [coin_change_brute_force(amount - c, coins) for c in coins]
    potential_changes = [pc for pc in potential_changes if pc != -1]
    if not potential_changes:
        return -1
    to_add = min(potential_changes) + 1
    return to_add


def coin_change_list(
    amount: int,
    coins: list[int],
    memo: dict[tuple[int, int], list[int]] = {},
    curr_coin=0,
) -> list[int]:
    result = memo.get((amount, curr_coin), None)
    if result is not None:
        return result
    if amount < 0:
        return []
    if amount == 0:
        return [curr_coin]
    potential_changes = [coin_change_list(amount - c, coins, memo, c) for c in coins]
    potential_changes = [pc for pc in potential_changes if pc]
    if not potential_changes:
        memo[(amount, curr_coin)] = []
        return []
    min_change = min(potential_changes, key=len)[:]
    if curr_coin != 0:
        min_change.insert(0, curr_coin)
    memo[(amount, curr_coin)] = min_change[:]
    return min_change


def main() -> None:
    pass


if __name__ == "__main__":
    main()

