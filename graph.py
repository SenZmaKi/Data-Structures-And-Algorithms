from typing import Callable, Self


class Node:
    def __init__(self, x: int, y: int, neighbours: list[Self] = []) -> None:
        self.x = x
        self.y = y
        self.neighbours = neighbours

    def add_neighbour(self, point: Self) -> None:
        self.neighbours.append(point)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def print_graph(self, visited: set[Self] = set()) -> None:
        if self in visited:
            return
        visited.add(self)
        for n in self.neighbours:
            print(f"{self} <--> {n}")
        for n in self.neighbours:
            n.print_graph()


class Graph:
    def __init__(self, root_node: Node) -> None:
        self.root_node = root_node

    def traverse(self, callback: Callable[[Node, list[Node]], None]) -> None:
        def helper(node: Node, visited: set[Node] = set()) -> None:
            if node in visited:
                return
            visited.add(node)
            callback(node, node.neighbours)
            for n in node.neighbours:
                helper(n, visited)

        helper(self.root_node)

    def print(self) -> None:
        def helper(node: Node, neighbours: list[Node]) -> None:
            for neighbour in neighbours:
                print(f"{node} <--> {neighbour}")

        self.traverse(helper)


def make_dict_graph() -> dict[str, dict[str, int]]:
    return {
        "A": {"B": 1, "D": 3},
        "B": {"A": 1, "C": 2},
        "C": {"B": 2, "D": 1},
        "D": {"A": 3, "C": 1, "E": 1},
        "E": {"C": 10, "D": 1},
    }


def make_graph() -> Graph:
    points = [
        Node(1, 1),
        Node(3, 5),
        Node(1, 5),
        Node(3, 4),
        Node(4, 1),
    ]
    points[0].add_neighbour(points[1])
    points[1].add_neighbour(points[4])
    points[0].add_neighbour(points[2])
    points[2].add_neighbour(points[3])
    return Graph(points[0])
