# optimized for 3K monitor
import pygame

import grid


WIDTH, HEIGHT = 1600, 1600
ROWS, COLS = 50, 50
CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TERRAIN_COLORS = [
    (80, 180, 90),  # grass
    (139, 69, 19),  # mud
    (0, 0, 255),  # water
    (0, 0, 0),  # wall
    (0, 255, 0),  # start
    (255, 0, 0),  # end
    (143, 0, 255),  # path
]

INPUT_TO_TERRAIN_TYPE = {
    pygame.K_q: grid.TerrainType.GRASS,
    pygame.K_w: grid.TerrainType.MUD,
    pygame.K_e: grid.TerrainType.WATER,
    pygame.K_r: grid.TerrainType.WALL,
}
