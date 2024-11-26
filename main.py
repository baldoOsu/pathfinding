import pygame
import sys

from constants import COLS, HEIGHT, INPUT_TO_TERRAIN_TYPE, ROWS, WHITE, WIDTH
from grid import Grid, TerrainType
from heuristics import manhattan_distance
from pathfinding import AStar, Node


pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A*")


def main(win):
    grid = Grid(ROWS, COLS)
    run = True
    started = False
    path = []
    selected_terrain_type = TerrainType.WALL

    while run:
        win.fill(WHITE)
        grid.draw(win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if started:
                continue

            # left click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                try:
                    node = grid.get_clicked_node(pos)
                except IndexError:
                    continue
                if not grid.start_node and node != grid.end_node:
                    grid.start_node = node
                    node.terrain_type = TerrainType.START
                elif not grid.end_node and node != grid.start_node:
                    grid.end_node = node
                    node.terrain_type = TerrainType.END
                elif node != grid.start_node and node != grid.end_node:
                    node.terrain_type = selected_terrain_type

            # right click
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                try:
                    node = grid.get_clicked_node(pos)
                except IndexError:
                    continue
                if node == grid.start_node:
                    grid.start_node = None
                elif node == grid.end_node:
                    grid.end_node = None
                node.terrain_type = TerrainType.GRASS

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and grid.start_node and grid.end_node:
                    started = True
                    grid.update_neighbors()
                    astar = AStar()
                    path = astar.search(
                        grid.start_node, grid.end_node, manhattan_distance
                    )
                    if path:
                        for node in path:
                            if node != grid.start_node and node != grid.end_node:
                                node.terrain_type = TerrainType.PATH
                    else:
                        print("No path found.")
                    started = False

                if event.key == pygame.K_c:
                    grid.reset()
                    path = []

                if event.key in INPUT_TO_TERRAIN_TYPE.keys():
                    selected_terrain_type = INPUT_TO_TERRAIN_TYPE[event.key]


if __name__ == "__main__":
    main(WIN)
