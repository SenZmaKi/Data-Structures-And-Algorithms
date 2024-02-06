class Item:
    def __init__(self, name: str, weight: int, value: int) -> None:
        self.name = name
        self.value = value
        self.weight = weight


def knapsack_bruteforce(
    max_weight: int,
    items: list[Item],
) -> list[Item]:
    items_lists: list[list[Item]] = []
    for idx, i in enumerate(items):
        next_items = items[:]
        next_items.pop(idx)
        next_weight = max_weight - i.weight
        if next_weight > 0:
            il = knapsack_bruteforce(next_weight, next_items)
            il.insert(0, i)
            items_lists.append(il)
    if not items_lists:
        return []
    return max(items_lists, key=lambda il: sum([i.value for i in il]))


def knapsack(
    max_weight: int,
    items: list[Item],
    memo: dict[tuple[int, tuple[Item, ...]], list[Item]] = {},
) -> list[Item]:
    result = memo.get((max_weight, tuple(items)), None)
    if result is not None:
        return result
    items_lists: list[list[Item]] = []
    for idx, i in enumerate(items):
        next_items = items[:]
        next_items.pop(idx)
        next_weight = max_weight - i.weight
        if next_weight > 0:
            il = knapsack(next_weight, next_items)
            il.insert(0, i)
            items_lists.append(il)

    if not items_lists:
        memo[(max_weight, tuple(items))] = []
        return []

    to_add = max(items_lists, key=lambda il: sum([i.value for i in il]))
    memo[(max_weight, tuple(items))] = to_add
    return to_add


def main() -> None:
    items = [
        Item("laptop", 7, 9),
        Item("phone", 1, 7),
        Item("blanket", 5, 4),
        Item("mouse", 1, 1),
        Item("wifi", 3, 5),
        Item("bucket", 4, 3),
        Item("food", 4, 6),
        Item("bag", 4, 3),
    ]
    max_weight = 10
    best_items_choice = knapsack_bruteforce(max_weight, items)
    if best_items_choice:
        print(", ".join([b.name for b in best_items_choice]))


if __name__ == "__main__":
    main()

