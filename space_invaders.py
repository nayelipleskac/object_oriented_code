#Space Invaders

import random, pygame, time
screen = pygame.display.set_mode((600, 600))
pygame.init()
pygame.display.set_caption("Space Invaders!!")
from pygame.constants import KEYDOWN, K_c, K_r, K_s, QUIT
clock = pygame.time.Clock()


black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (200, 200, 0)

colors = [red, green, blue, white, yellow]

class Character:
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
    def draw(self):
        alien_image = pygame.image.load("C:/Users\plesk/Documents/python projects/space invaders sprites/alien.png")
        alien_sprite = pygame.transform.scale(alien_image, 150, 150)
        pygame.blit(self.x, self.y)


