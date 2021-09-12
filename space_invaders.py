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
speedOptions = [-3,3]

def showtext(msg,x,y,color):
    font = pygame.font.SysFont("freesans", 32)
    msgobj = font.render(msg,False,white)
    screen.blit(msgobj,(x,y))

class Character:
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
    
class Alien(Character):
    xMotion= random.choice(speedOptions)
    yMotion = 5
    def __init__(self, x, y, length, width):
        super().__init__(x, y, length, width)
        self.alien_image = pygame.image.load('images/alien.png')
        self.alien_sprite = pygame.transform.scale(self.alien_image, (40, 40))
        self.alien_rect = self.alien_sprite.get_rect(topleft = (self.x, self.y))

    def draw_alien(self):
        screen.blit(self.alien_sprite, self.alien_rect)

    def move_alien(self):
        self.x += self.xMotion
        self.alien_rect[0] += self.xMotion


class PlayerShip(Character):
    def __init__(self,x, y, length, width):
        super().__init__(x, y, length, width)
        self.shipSpeed = 0
    def draw_ship(self):
        ship_image = pygame.image.load('images/ship.png')
        ship_sprite = pygame.transform.scale(ship_image, (80, 40))
        screen.blit(ship_sprite, (self.x, self.y))
    def move_ship(self):
        self.x += self.shipSpeed
        
class Bullet(Character):
    yMotion= 5
    def __init__(self, x, y, length, width):
        super().__init__(x, y, length, width)
        self.bulletSpeed = 20
        self.bullet_image = pygame.image.load('images/bullet.png')
        self.bullet_sprite = pygame.transform.scale(self.bullet_image, (30, 60))
        self.bullet_rect = self.bullet_sprite.get_rect(topleft= (self.x, self.y))
    def draw_bullet(self):
      
        screen.blit(self.bullet_sprite, self.bullet_rect)

    def move_bullet(self):
        self.y -= self.bulletSpeed
        self.bullet_rect[1] -= self.yMotion

        
        if self.y+60 == 0:
            if self in bullet_list:
                bullet_list.remove(self)
        

alien_list = []
bullet_list = []

player_ship = PlayerShip(300, 550, 80, 40)

for x in range(10, 550, 55):
    for y in range(10, 300, 60):
        alien = Alien(x, y, 40, 40)
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

        print('pos: ',a.x, a.y)
        #colision with wall
        if a.x + 40 >= 600:
            print('colision with right wall') 
            for b in alien_list:
                b.y = b.y +10
                b.xMotion = -b.xMotion 
                b.alien_rect[0] = -b.xMotion
                # print('pos on right: ',a.x,  a.y)
                


        if a.x <= 0:
            print('colision with left wall')
            for b in alien_list:
                b.y = b.y +10
                b.xMotion = -b.xMotion
                b.alien_rect[0] = -b.xMotion
                # print('pos on left: ', a.x,  a.y)

    if len(alien_list) == 0:
        showtext('Game Over', 250, 100, white)
        pygame.display.update()
        time.sleep.update()
        break
        
    #colision with player ship
    if a.y+40 >= 560:
        print('GAME OVER')
        showtext('Game Over!', 250, 100, white)
        pygame.display.update()
        time.sleep(3)
        break

    
    for b in bullet_list:
        b.draw_bullet()
        b.move_bullet()

    #colision with bullet
    for a in alien_list:
        for b in bullet_list:
            if a.alien_rect.colliderect(b.bullet_rect):
                print('collision!!')
                alien_list.remove(a)
                bullet_list.remove(b)

    #boundaries
    if player_ship.x+80 >= 600:
        player_ship.x = 520
    if player_ship.x <= 0:
        player_ship.x = 0

  


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
         
                bullet = Bullet(player_ship.x+25, player_ship.y-50, 15, 20, )
                bullet_list.append(bullet)
          

                clock.tick(30)
                pygame.display.update()

                
        if event.type == KEYUP:
            if event.key == K_LEFT:
                player_ship.shipSpeed = 0
            if event.key == K_RIGHT:
                player_ship.shipSpeed = 0
           

            

    









