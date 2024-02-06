import heapq
from graph import make_dict_graph
from random import choice as random_choice


def prims(
    graph: dict[str, dict[str, int]], start_vertex: str = ""
) -> list[tuple[str, str, int]]:
    if not start_vertex:
        start_vertex = random_choice(list(graph.keys()))
    visited = set(start_vertex)
    minimum_spanning_tree: list[tuple[str, str, int]] = []
    edges = [
        (weight, vertex, start_vertex) for vertex, weight in graph[start_vertex].items()
    ]
    heapq.heapify(edges)
    while edges:
        weight, current_vertex, parent_vertex = heapq.heappop(edges)
        if current_vertex not in visited:
            visited.add(current_vertex)
            minimum_spanning_tree.append((current_vertex, parent_vertex, weight))
            for neighbour, weight in graph[current_vertex].items():
                heapq.heappush(edges, (weight, neighbour, current_vertex))
    return minimum_spanning_tree


def main() -> None:
    result = prims(make_dict_graph())
    total_cost = sum(w for _, _, w in result)
    print(f"Minimum spanning tree total cost: {total_cost}")
    for node in result:
        print(f"From {node[1]} to {node[0]} {node[2]}")


if __name__ == "__main__":
    main()
