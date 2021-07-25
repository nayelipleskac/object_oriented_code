#Pong with classes

import pygame, random, time

from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w
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

#reminder: get colliderect to work on paddles
 
class Ball():     
    def __init__(self):         
        self.x = 300         
        self.y = 300         
        self.color = red        
        self.radius = 10         
        self.xmovement = 2         
        self.ymovement = 2 
        self.rect = None
    def drawBall(self):
        self.rect = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)
    def moveBall(self):
        ball.x += ball.xmovement
        ball.y += ball.ymovement

        #hitting bottom wall
        if ball.y + ball.radius > 600:
            print('bottom')
            ball.ymovement = -ball.ymovement

        #hitting top wall
        if ball.y - ball.radius < 0:
            print('top')
            ball.ymovement = -ball.ymovement

        #hitting left
        if ball.x + ball.radius > 600:
            p1.score +=1
            ball.x = 300
            ball.y = 300
            print('right')
            print( 'p1: ',p1.score, 'p2: ', p2.score)
        
            

        #hitting right
        if ball.x - ball.radius < 0:
            ball.x = 300
            ball.y = 300
            p2.score += 1
            print('left,')
            print( 'p1: ',p1.score, 'p2: ', p2.score)
            
        
        #collison with paddles
        #checking front
        if ball.x - ball.radius in range(p1.x, p1.x + 25) and ball.y- ball.radius in range(p1.y, p1.y + 150):
            ball.x = ball.x + ball.radius-5
            print('ball x col. with left paddle ', ball.x)
            ball.xmovement = 1


        if ball.x + ball.radius in range(p2.x, p2.x + 25) and ball.y+ ball.radius in range(p2.y, p2.y + 150):
            ball.x = ball.x- ball.radius- 5
            print('ball x col. with right paddle ', ball.x)
            ball.xmovement = -1

        #checking top p1
        if ball.y- ball.radius in range(p1.x, p1.x+25):
            ball.ymovement = 1
        #checking bottom p1
        if ball.y+ ball.radius in range(p1.x-150, p1.x-150+25):
            ball.ymovement = -1
        #checking top p2
        if ball.y- ball.radius in range(p2.x, p2.x+25):
            ball.ymovement = 1
        #checking bottom p2
        if ball.y+ ball.radius in range(p2.x-150, p2.x-150+25):
            ball.ymovement = -1
           

        # if (ball.rect).colliderect(p1.rect):
        #     ball.xmovement = 1
        # if (ball.rect).colliderect(p2.rect):
        #     ball.xmovement = -1

        
ball = Ball()  

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
        self.speed = 1
        self.rect = None

    def drawPaddle(self):
        self.rect = pygame.draw.rect(screen, self.color, (self.x, self.y, 25, 150),0)
    def showScore(self, text, x, y, color):
        font = pygame.font.SysFont('freesans', 32)
        msg = font.render(text, True, color)
        screen.blit(msg, (x,y))

p1 = Paddle(green, 10, 200)    
p2 = Paddle(blue, 565, 200) 


while True:

    screen.fill(black)
    clock.tick(100)
    ball.drawBall()
    ball.moveBall()
    p1.drawPaddle()
    p2.drawPaddle()
    p1.showScore('Left Paddle: {}'.format(p1.score), 100, 35, white)
    p2.showScore('Right Paddle: {}'.format(p2.score), 300, 35, white)

    # print(p1.x, p1.y)
    #boundaries 
    if p2.y <= 0:
        p2.y = 0
    if p2.y+150 >= 600:
        p2.y = 450
    if p1.y <= 0:
        p1.y = 0
    if p1.y+150 >= 600:
        p1.y = 450

    #movement
    if p2.up == True:
        p2.y -= p2.speed
    if p2.down == True:
        p2.y += p2.speed
    if p1.up == True:
        p1.y -= p1.speed
    if p1.down == True:
        p1.y += p1.speed

    #managing score
    if p1.score >= 10:
        
        p1.showScore('LEFT PADDLE WINS!!', 175, 100, white)
        p2.showScore('', 200, 35, white)
        print('P1 WON!!')
        pygame.display.update()
        time.sleep(5)
        break
    if p2.score >= 10:
        
        p1.showScore('', 200, 35, white)
        p2.showScore('RIGHT PADDLE WINS!!', 175, 100, white)
        print('P2 WON!!')
        pygame.display.update()
        time.sleep(5)
        break


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                p2.up = True
                print('right paddle up!')
                
            if event.key == K_DOWN:
                p2.down = True
                print('right paddle down!')
                
            if event.key == K_w:
                p1.up = True
                print('left paddle up!')
            
            if event.key == K_s:
                p1.down = True
                print('left paddle down!')

        if event.type == KEYUP:
            if event.key == K_UP:
                p2.up = False
            if event.key == K_DOWN:
                p2.down = False
            if event.key == K_w:
                p1.up = False
            if event.key == K_s:
                p1.down = False

    pygame.display.update()
                
                

            
            
            
 
                    

