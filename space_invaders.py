#Space Invaders Game

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
speedOptions = [-1,1]

class Character:
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
    def draw_alien(self):
        alien_image = pygame.image.load("C:/Users\plesk/Documents/python projects/space invaders sprites/alien.png")
        alien_sprite = pygame.transform.scale(alien_image, (40, 40))
        screen.blit(alien_sprite, (self.x, self.y))

    def draw_boss(self):
        pass

        # boss_alien_image = pygame.image.load("C:/Users/plesk/Documents/python projects/space invaders sprites/boss-alien.png")
        # boss_alien_sprite = pygame.transform.scale(boss_alien_image, (300, 300))
        # screen.blit(boss_alien_sprite, (self.x, self.y))


class Alien(Character):
    xMotion= random.choice(speedOptions)
    def __init__(self, x, y, length, width):
        super().__init__(x, y, length, width)
        self.check = False


    def move_alien(self):
        self.x += self.xMotion

class PlayerShip(Alien):
    def __init__(self,x, y, length, width):
        super().__init__(x, y, length, width)

alien_list = []

for x in range(10, 550, 55):
    for y in range(10, 300, 60):
        alien = Alien(x, y, 40, 40)
        alien_list.append(alien)

while True:
    clock.tick(30)
    screen.fill(black)


    for a in alien_list:
        a.draw_alien()
        a.move_alien()



        if a.x + 60 >= 600:
            for b in alien_list:
                
                b.y = b.y +20
                b.xMotion = -b.xMotion 

        if a.x <= 0:
            for c in alien_list:

                c.y = c.y +20
                c.xMotion = -c.xMotion


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()









