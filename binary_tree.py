from typing import Self


class Node:
    def __init__(
        self, value: int, left: Self | None = None, right: Self | None = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.left.value if self.left else None} <- {self.value} -> {self.right.value if self.right else None}"

    def print(self) -> None:
        print(self)
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()

    def height(self) -> int:
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return max(left_height, right_height) + 1


def main() -> None:
    r"""
                             0
                      /            \
                     1              2
                   /   \           /  \ 
                  3    4          5    9   
                 /    / \        /
                6     7  8      10
                                 \
                                  11
    """
    nodes = [
        Node(0),
        Node(1),
        Node(2),
        Node(3),
        Node(4),
        Node(5),
        Node(6),
        Node(7),
        Node(8),
        Node(9),
        Node(10),
        Node(11),
    ]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[9]
    nodes[3].left = nodes[6]
    nodes[4].left = nodes[7]
    nodes[4].right = nodes[8]
    nodes[5].left = nodes[10]
    nodes[10].right = nodes[11]

    print(nodes[0].height())


if __name__ == "__main__":
    main()

