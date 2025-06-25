import pygame
import sys
from fire import Fire

width = 800
height = 600
screen_width = 800
screen_height = 600


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height),0,8)
        self.clock = pygame.time.Clock()
        self.fire = Fire(self)

    def update(self):
        self.fire.update()
        self.clock.tick()
        pygame.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self):
        self.fire.draw()
        pygame.display.flip()

    def get_time(self):
        self.time = pygame.time.get_ticks() * 0.001

    def check_event(self):
        for i in pygame.event.get():
            if i.type == pygame.QUIT or (i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_event()
            self.get_time()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()