#Space Invaders Game

import random, pygame, time
screen = pygame.display.set_mode((600, 600))
pygame.init()
pygame.display.set_caption("Space Invaders!!")
from pygame.constants import KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_SPACE, K_c, K_r, K_s, QUIT
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
    
        # boss_alien_image = pygame.image.load("C:/Users/plesk/Documents/python projects/space invaders sprites/boss-alien.png")
        # boss_alien_sprite = pygame.transform.scale(boss_alien_image, (300, 300))
        # screen.blit(boss_alien_sprite, (self.x, self.y))


class Alien(Character):
    xMotion= random.choice(speedOptions)
    def __init__(self, x, y, length, width, alien_rect):
        super().__init__(x, y, length, width)
        self.check = False
        self.alien_rect = alien_rect

    def draw_alien(self):
        alien_image = pygame.image.load("C:/Users\plesk/Documents/python projects/space invaders sprites/alien.png")
        alien_sprite = pygame.transform.scale(alien_image, (40, 40))
        alien_get_rect = alien_sprite.get_rect()
        screen.blit(alien_sprite, (self.x, self.y))

    def move_alien(self):
        self.x += self.xMotion

class PlayerShip(Character):
    def __init__(self,x, y, length, width):
        super().__init__(x, y, length, width)
        self.shipSpeed = 0
    def draw_ship(self):
        ship_image = pygame.image.load("C:/Users/plesk/Documents/python projects/space invaders sprites/ship.png")
        ship_sprite = pygame.transform.scale(ship_image, (80, 40))
        screen.blit(ship_sprite, (self.x, self.y))
    def move_ship(self):
        self.x += self.shipSpeed
        
class Bullet(Character):
    def __init__(self, x, y, length, width, bullet_rect):
        super().__init__(x, y, length, width)
        self.bulletSpeed = 20
        self.bullet_rect = bullet_rect
    def draw_bullet(self):
        bullet_image = pygame.image.load("C:/Users/plesk/Documents/python projects/space invaders sprites/bullet.png")
        bullet_sprite = pygame.transform.scale(bullet_image, (30, 60))
        bullet_get_rect = bullet_sprite.get_rect()
        screen.blit(bullet_sprite, (self.x, self.y))

    def move_bullet(self):
        self.y -= self.bulletSpeed
        
        if self.y+60 <= 0:
            print(bullet_list)
            if self in bullet_list:
                bullet_list.remove(self)
            

    def check(self):
        #checking for alien collision
        pass
        
        # if self.bullet_get_rect.colliderect(alien_get_rect):
        #     bullet_list.remove(self)
        #     alien_list.remove(alien)
            

alien_list = []
bullet_list = []

player_ship = PlayerShip(300, 550, 80, 40)

for x in range(10, 550, 55):
    for y in range(10, 300, 60):
        alien = Alien(x, y, 40, 40, [x, y, 40, 40])
        alien_list.append(alien)

while True:
    clock.tick(30)
    pygame.display.update()
    screen.fill(black)

    player_ship.draw_ship()
    player_ship.move_ship()

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

    

    for b in bullet_list:
        b.draw_bullet()
        b.move_bullet()
        b.check()

    for a in alien_list:
        for b in bullet_list:
            if a.alien_rect.colliderect(b.bullet_rect):
                print('collision!!')

    #boundaries
    if player_ship.x+80 >= 600:
        player_ship.x = 520
    if player_ship.x <= 0:
        player_ship.x = 80

    # if alien


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:

            if event.key == K_LEFT:
                player_ship.shipSpeed = -10
            if event.key == K_RIGHT:
                player_ship.shipSpeed = 10
            if event.key == K_SPACE:
                #shoot bullet
         
                bullet = Bullet(player_ship.x+25, player_ship.y-50, 15, 20, [x, y, 15, 20])
                bullet_list.append(bullet)
                # print(bullet_list)

                clock.tick(30)
                pygame.display.update()

                
        if event.type == KEYUP:
            if event.key == K_LEFT:
                player_ship.shipSpeed = 0
            if event.key == K_RIGHT:
                player_ship.shipSpeed = 0
           

            

    









