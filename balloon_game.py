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




class balloon:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xMotion = random.randint(1,4)
        self.color = random.choice(colors)
        self.key =  chr(random.randint(97,122))
        self.flag = False
        # self.score = 0
        
        
    def draw_shapes(self):
        if self.flag == False:
            # pygame.draw.circle(screen, self.color, (self.x, self.y), 25, 1)
            balloon_image = pygame.image.load("C:/Users/plesk/Downloads/balloon-sprite-removebg-preview.png")
            balloon_sprite = pygame.transform.scale(balloon_image, (60, 60))
            screen.blit(balloon_sprite, (self.x, self.y))
            showtext('{}'.format(self.key), self.x-10, self.y-15, white)
        if self.flag == True:
            #the sprite disappears
            circles_list.remove(self)
            print(len(circles_list))
            # pygame.draw.circle(screen, black, (self.x, self.y), 25, 1)
       
    def move(self):
        self.x += self.xMotion
        if self.x+25 >= 560:
            self.xMotion = -random.randint(1,4)
        if self.x-25 <= 0:
            self.xMotion = random.randint(1,4)
    
        


circle2 = balloon(random.randint(0,500), random.randint(25,550))
circle1 = balloon(random.randint(0,500), random.randint(25,550))
circle3 = balloon(random.randint(0,500), random.randint(25,550))
circle4 = balloon(random.randint(0,500), random.randint(25,550))
circle5 = balloon(random.randint(0,500), random.randint(25,550))
circle6 = balloon(random.randint(0,500), random.randint(25,550))
circle7 = balloon(random.randint(0,500), random.randint(25,550))

circle8 = balloon(random.randint(25,500), random.randint(25,550))
circle9 = balloon(random.randint(25,500), random.randint(25,550))
circle10 = balloon(random.randint(25,500), random.randint(25,550))

circles_list = [circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9, circle10]
check = 0

# def showtext(text, color, x, y):
#     font = pygame.font.SysFont('freesans', 32)
#     msg = font.render(text, True, color)
#     screen.blit(msg, (x,y))

score = 0

while True:
    screen.fill(black)

    clock.tick(30)
    showtext('Score: {}'.format(score), 480, 25, white)

    for c in circles_list:
        c.move()
        c.draw_shapes()
        

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            print(event.key)
            key_pressed = pygame.key.name(event.key)
            print(key_pressed)
            for balloon_object in circles_list:
                if key_pressed == balloon_object.key:
                    check = 1
                
                if check == 1:
                    score+= 1
                    circles_list.remove(balloon_object)
                    circles_list.append(balloon(random.randint(0,500), random.randint(25,550)))
                    check = 0
                # elif key_pressed != balloon_object.key:
                #     check = 0
                #     if check == 0:

                #         score -= 1
    pygame.display.update()


                    # c.flag = True
                    # print(c.key,'we got the key!')
                    # c.timesPressed = c.timesPressed+1
                    # print(c.key, c.timesPressed)
                    # if c.timesPressed % 2 == 0:
                    #     c.flag = False
             
