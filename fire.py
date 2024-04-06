import pygame
import numpy as np
import random

width = 80
height = 50
screen_width = 800
screen_height = 500
membuffer = np.zeros((width,height), np.int8)
colour_map = np.zeros((256, 3))

def add_fire():
     
    for x in range(0,width):
       buffer[x][height-1] = random.randint(0,255)          

def fire():
# Créer un tableau pour stocker les valeurs calculées
    result = np.zeros_like(buffer)

# Parcourir les indices x et y, mais exclure les bords
    for x in range(0, width):
        for y in range(0, height):
            result[x, y] = (buffer[(x-1)%width, (y+1)%height] + buffer[x, (y+1)%height] + buffer[(x+1)%width, (y+1)%height] + buffer[x, (y+2)%height]) >>2

# Mettre à jour les valeurs dans 'a' avec les valeurs calculées
    buffer[0:width, 0:height] = result[0:width, 0:height]     


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
screen = pygame.display.set_mode((screen_width, screen_height),0,8)

surface = pygame.Surface((width,height),0,8)
surface.set_palette(colour_map)

buffer = pygame.surfarray.array2d(surface)
clock = pygame.time.Clock()

running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick()
    print(clock.get_fps())

    add_fire()
    fire()
    pygame.surfarray.blit_array(surface, buffer)
    temp = pygame.transform.scale(surface, screen.get_size())
    screen.blit(temp,(0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()



     