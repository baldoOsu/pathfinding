from __future__ import annotations
from typing import Callable

import heapq

# avoid circular import by not using from x import y
import grid


class Node:
    x: float
    y: float
    neighbors: set[tuple[float, Node]]

    # neighbors is a list of (cost, node)
    def __init__(
        self,
        x: float,
        y: float,
        terrain_type: grid.TerrainType,
        neighbors: set[tuple[float, Node]] = None,
    ):
        self.x = x
        self.y = y
        self.terrain_type = terrain_type
        self.neighbors = neighbors

    def set_neighbors(self, neighbors: set[tuple[float, Node]]) -> None:
        self.neighbors = neighbors

    # required for heapq
    def __lt__(self, other):
        return False


class AStar:
    def search(
        self,
        start_node: Node,
        end_node: Node,
        heuristic: Callable[[Node, Node], float],
    ) -> list[Node]:
        open_queue: list[tuple[float, Node]] = []
        total_g_scores: dict[Node, float] = {}
        came_from: dict[Node, Node] = {}

        heapq.heappush(open_queue, (0, start_node))
        total_g_scores[start_node] = 0

        while len(open_queue) > 0:
            _, node = heapq.heappop(open_queue)

            if node == end_node:
                return self._reconstruct_path(node, came_from)

            for cost, neighbor in node.neighbors:
                g_score = total_g_scores[node] + cost
                prev_g_score = total_g_scores.get(neighbor)
                if prev_g_score is not None and g_score >= prev_g_score:
                    continue

                h_score = heuristic(neighbor, end_node)
                f_score = g_score + h_score

                heapq.heappush(open_queue, (f_score, neighbor))
                came_from[neighbor] = node
                total_g_scores[neighbor] = g_score

        # no solution was found
        return None

    def _reconstruct_path(
        self,
        node: Node,
        came_from: dict[Node, Node],
        path: list[Node] = None,
    ) -> list[Node]:
        if path is None:
            path = []

        parent_node = came_from.get(node)
        if node is None:
            path.reverse()
            return path

        path.append(node)
        return self._reconstruct_path(parent_node, came_from, path)
