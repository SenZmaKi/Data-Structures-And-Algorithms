import heapq
from typing import cast

from graph import make_dict_graph

INFINITY = cast(int, float("inf"))


def dijkstras(
    start_node: str, graph: dict[str, dict[str, int]]
) -> dict[str, tuple[str, int]]:
    distances = {node: (start_node, INFINITY) for node in graph.keys()}
    distances[start_node] = (start_node, 0)
    priority_queue: list[tuple[int, str]] = [(0, start_node)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if (  # Not really necesarry but allows us to skip nodes we already know are bad
            current_distance > distances[current_node][1]
        ):
            continue
        for neighbour, weight in graph[current_node].items():
            new_neighbour_distance = current_distance + weight
            if new_neighbour_distance < distances[neighbour][1]:
                distances[neighbour] = (current_node, new_neighbour_distance)
                heapq.heappush(priority_queue, (new_neighbour_distance, neighbour))

    return distances


def main() -> None:

    start_node = "A"
    result = dijkstras(start_node, make_dict_graph())

    print("Shortest distances from", start_node, "to each node:")
    for node, distance in result.items():
        print(f"To {node} via {distance[0]} {distance[1]}")


if __name__ == "__main__":
    main()
