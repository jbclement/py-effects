import pygame
import numpy
from random import randint

buffer = numpy.zeros((320,200), numpy.int8)
colour_map = numpy.zeros((256, 3))
for i in range(0,64):
        colour_map[i][0] = i * 4
        colour_map[i][1] = 0
        colour_map[i][2] = 0
        
        colour_map[i+128][0] = 255
        colour_map[i+64][1] = i * 2
        colour_map[i+64][2] = 0
            
        colour_map[i+128][0] = 255     
        colour_map[i+128][1] = 128 + i * 2
        colour_map[i+128][2] = i * 2
     
        colour_map[i+192][0] = 255        
        colour_map[i+192][1] = 255
        colour_map[i+192][2] = 128 + i * 2

# pygame setup
pygame.init()
screen = pygame.display.set_mode((320, 200),0,8)

surface = pygame.Surface((320,200),0,8)
surface.set_palette(colour_map)
pygame.surfarray.blit_array(surface, buffer)
screen.blit(surface,(0,0))
# clock = pygame.time.Clock()
running = True
# dt = 0

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    # dt = clock.tick(60) / 1000

pygame.quit()