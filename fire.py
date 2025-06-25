import pygame
import numpy as np
import random
from numba import njit, prange


class Fire:
    def __init__(self, app):
        self.app = app

        self.width = 800
        self.height = 600
        self.screen_width = 800
        self.screen_height = 600
        self.colour_map = np.zeros((256, 3), np.uint8)

        self.set_palette()  # Set the colour palette
        self.surface = pygame.Surface((self.width, self.height), 0, 8)

        self._buffer = pygame.surfarray.array2d(self.surface)

        self.surface.set_palette(self.colour_map)

    def set_palette(self):
        for i in range(0, 64):
            self.colour_map[i][0] = i * 2
            self.colour_map[i][1] = 0
            self.colour_map[i][2] = 0

            self.colour_map[i + 64][0] = 128 + i * 2
            self.colour_map[i + 64][1] = i * 2
            self.colour_map[i + 64][2] = 0

            self.colour_map[i + 128][0] = 255
            self.colour_map[i + 128][1] = 128 + i * 2
            self.colour_map[i + 128][2] = i * 2

            self.colour_map[i + 192][0] = 255
            self.colour_map[i + 192][1] = 255
            self.colour_map[i + 192][2] = 128 + i * 2

    @staticmethod
    @njit(parallel=True, fastmath=True)
    def add_fire(buffer):

        for x in prange(0, buffer.shape[0]):
            buffer[x][buffer.shape[1] - 1] = random.randint(0, 255)

        return buffer

    @staticmethod
    @njit(parallel=True, fastmath=True)
    def fire(width, height, buffer):
        # Créer un tableau pour stocker les valeurs calculées
        result = np.zeros_like(buffer)

        # Parcourir les indices x et y, mais exclure les bords
        for x in prange(0, width):
            for y in prange(0, height):
                result[x, y] = (
                    buffer[(x - 1) % width, (y + 1) % height]
                    + buffer[x, (y + 1) % height]
                    + buffer[(x + 1) % width, (y + 1) % height]
                    + buffer[x, (y + 2) % height]
                ) >> 2

        return result

    def update(self):
        self._buffer = self.add_fire(self._buffer)
        self._buffer = self.fire(self.width, self.height, self._buffer)

    def draw(self):

        pygame.surfarray.blit_array(self.surface, self._buffer)
        self.app.screen.blit(self.surface, (0, 0))
