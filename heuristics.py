from math import sqrt
from pathfinding import Node


def manhattan_distance(node_1: Node, node_2: Node) -> float:
    return abs(node_2.x - node_1.x) + abs(node_2.y - node_1.y)


def euclidean_distance(node_1: Node, node_2: Node) -> float:
    return sqrt((node_2.x - node_1.x) ** 2, (node_2.y - node_1.y) ** 2)
