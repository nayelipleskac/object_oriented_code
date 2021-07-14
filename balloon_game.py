#Balloon Game with Classes

import pygame, random, time

from pygame.constants import KEYDOWN, QUIT
pygame.init()
pygame.display.set_caption("Balloon Game!")
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (200, 200, 0)

colors = [red, green, blue, white, yellow]


def showtext(msg,x,y,color):
    font = pygame.font.SysFont("freesans", 32)
    msgobj = font.render(msg,False,white)
    screen.blit(msgobj,(x,y))


class circle:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xMotion = random.randint(1,4)
        self.color = random.choice(colors)
        self.key =  random.choice(keys)
        self.flag = False
        self.timesPressed = 0
        
    def draw_shapes(self):
        if self.flag == False:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 25, 1)
            showtext('{}'.format(self.key), self.x-10, self.y-15, white)
        if self.flag == True:
            pygame.draw.circle(screen, black, (self.x, self.y), 25, 1)

            

            # if self.timesPressed == 2:
            #     self.flag = False
       
    def move(self):
        self.x += self.xMotion
        if self.x+25 >= 600:
            self.xMotion = -random.randint(1,4)
        if self.x-25 <= 0:
            self.xMotion = random.randint(1,4)

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keyChoice = random.choice(keys)

circle1 = circle(random.randint(0,635), random.randint(25,575))
circle2 = circle(random.randint(0,635), random.randint(25,575))
circle3 = circle(random.randint(0,635), random.randint(25,575))
circle4 = circle(random.randint(0,635), random.randint(25,575))
circle5 = circle(random.randint(0,635), random.randint(25,575))
circle6 = circle(random.randint(0,635), random.randint(25,575))
circle7 = circle(random.randint(0,635), random.randint(25,575))

circle8 = circle(random.randint(25,635), random.randint(25,575))
circle9 = circle(random.randint(25,635), random.randint(25,575))
circle10 = circle(random.randint(25,635), random.randint(25,575))

circles_list = [circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9, circle10]

while True:
    clock.tick(30)
    pygame.display.update()
    screen.fill(black)
    for c in circles_list:
        c.move()
        c.draw_shapes()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            print(event.key)
            for c in circles_list:
                if chr(event.key) == c.key:
                    c.flag = True
                    print(c.key,'we got the key!')
                    c.timesPressed = c.timesPressed+1
                    print(c.key, c.timesPressed)
                    if c.timesPressed % 2 == 0:
                        c.flag = False
             
