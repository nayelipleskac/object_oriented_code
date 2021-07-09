#Pong with classes

import pygame, random, time

from pygame.constants import KEYDOWN, K_DOWN, K_UP, K_s, K_w
pygame.init()
pygame.display.set_caption("Pong!")
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (200, 200, 0)

#Basic syntax for Ball class: 
class Ball():     
    def __init__(self):         
        self.x = 300         
        self.y = 300         
        self.color = red        
        self.radius = 20         
        self.xmovement = 8         
        self.ymovement = 10 
    def drawBall(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)

ball = Ball()  # Creating an object/instance of this class. 

#Basic syntax for Paddle class: 
#arrows are for right Paddle
#WASD for left paddle

class Paddle():     
    def __init__(self, color, x, y):         
        self.color = color         
        self.x = x         
        self.y = y         
        self.width = 20         
        self.height = 200 
        self.up = False         
        self.down = False         
        self.score = 0         
        self.speed = 0 
    def drawPaddle(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 150),0)

p1 = Paddle(green, 10, 200)    # Paddle 1 
p2 = Paddle(blue, 540, 200)  # Paddle 2 

while True:

    ball.drawBall()
    p1.drawPaddle()
    p2.drawPaddle()
    pygame.display.update()
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                print('right paddle up!')
                p2.speed = 5
                p2.up = True
                p2.y -= p2.speed
            if event.key == K_DOWN:
                print('right paddle down!')
                p2.speed = 5
                p2.down = True
                p2.y += p2.speed
            if event.key == K_w:
                print('left paddle up!')
                p1.speed = 5
                p1.up = True
                p1.y -= p1.speed
            if event.key == K_s:
                print('left paddle down!')
                p1.speed = 5
                p1.down = True
                p1.y += p1.speed
 
                    

