# Grid class to manage the grid and nodes
import pygame
from enum import IntEnum

from pathfinding import Node
import constants


class TerrainType(IntEnum):
    GRASS = 0
    MUD = 1
    WATER = 2
    WALL = 3
    START = 4
    END = 5
    PATH = 6


class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = [
            [Node(x, y, TerrainType.GRASS) for x in range(cols)] for y in range(rows)
        ]
        self.start_node = None
        self.end_node = None

    def draw(self, win):
        for row in self.grid:
            for node in row:
                color = constants.TERRAIN_COLORS[node.terrain_type]
                rect = pygame.Rect(
                    node.x * constants.CELL_WIDTH,
                    node.y * constants.CELL_HEIGHT,
                    constants.CELL_WIDTH,
                    constants.CELL_HEIGHT,
                )
                pygame.draw.rect(win, color, rect)
                pygame.draw.rect(win, constants.GREY, rect, 1)

    def reset(self):
        self.__init__(self.rows, self.cols)

    def get_clicked_node(self, pos):
        x, y = pos
        row = y // constants.CELL_HEIGHT
        col = x // constants.CELL_WIDTH
        if row > len(self.grid) or col > len(self.grid[row]):
            raise IndexError("Grid position out of range")

        return self.grid[row][col]

    def update_neighbors(self):
        for row in self.grid:
            for node in row:
                neighbors = set()
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy in directions:
                    x2, y2 = node.x + dx, node.y + dy
                    if 0 <= x2 < self.cols and 0 <= y2 < self.rows:
                        neighbor = self.grid[y2][x2]
                        if neighbor.terrain_type != TerrainType.WALL:
                            # cast is based on terrain type
                            cost = int(neighbor.terrain_type)
                            neighbors.add((cost, neighbor))
                node.set_neighbors(neighbors)
