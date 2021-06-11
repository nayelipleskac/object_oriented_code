from pygame.constants import KEYDOWN, QUIT

import pygame, random

#1
pygame.init() 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("test")

clock = pygame.time.Clock()

red= (255, 0, 0)
blue = (0,0,255)
green = (0, 255,0)
purple = (126,0,126)
black = (0,0,0)
white = (255,255,255)
pink = (175, 0, 175)
orange = (240, 100, 0)
gray= (100,100,100)
yellow = (255,255,0)
aqua = (0,255,255)
lime = (0,255,0)

colors = [red, blue, green, purple, white, pink, orange, gray, yellow, aqua, lime]


# class circle:
#     def __init__(self, radius, x, y, color):
#         self.radius = radius
#         self.x = x
#         self.y = y
#         self.color = color
#     def draw_shapes(self):
#         pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 1)


# circle1 = circle(15, random.randint(20, 650), random.randint(20, 650), random.choice(colors))
# circle2 = circle(30, random.randint(20, 650), random.randint(20, 650), random.choice(colors))
# circle3 = circle(30, random.randint(20, 650), random.randint(20, 650), random.choice(colors))
# circle4 = circle(30, random.randint(20, 650), random.randint(20, 650), random.choice(colors))
# circle5 = circle(30, random.randint(20, 650), random.randint(20, 650), random.choice(colors))
# circle6 = circle(30, random.randint(20, 650), random.randint(20, 650), random.choice(colors))
# circle7 = circle(30, random.randint(20, 650), random.randint(20, 650), random.choice(colors))
# circle8 = circle(30, random.randint(20, 650), random.randint(20, 650), random.choice(colors))
# circle9 = circle(30, random.randint(20, 650), random.randint(20, 650), random.choice(colors))
# circle10 = circle(30, random.randint(20, 650), random.randint(20, 650), random.choice(colors))


# while True:
#     pygame.display.update()
#     circle1.draw_shapes()
#     circle2.draw_shapes()
#     circle3.draw_shapes()
#     circle4.draw_shapes()
#     circle5.draw_shapes()
#     circle6.draw_shapes()
#     circle7.draw_shapes()
#     circle8.draw_shapes()
#     circle9.draw_shapes()
#     circle10.draw_shapes()

#2
def showtext(msg,x,y,color):
    font = pygame.font.SysFont("freesans", 32)
    msgobj = font.render(msg,False,white)
    screen.blit(msgobj,(x,y))


class circle:
    
    def __init__(self, x, y, ):
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
       
    def defMove(self):
        self.x += self.xMotion
        if self.x+25 >= 600:
            self.xMotion = -random.randint(1,4)
        if self.x-25 <= 0:
            self.xMotion = random.randint(1,4)

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keyChoice = random.choice(keys)

circle1 = circle(random.randint(0,635), 30)
circle2 = circle(random.randint(0,635), 30)
circle3 = circle(random.randint(0,635), 30)
circle4 = circle(random.randint(0,635), 30)
circle5 = circle(random.randint(0,635), 30)
circle6 = circle(random.randint(0,635), 30)
circle7 = circle(random.randint(0,635), 30)

circle8 = circle(random.randint(25,635), 80)
circle9 = circle(random.randint(25,635), 80)
circle10 = circle(random.randint(25,635), 80)
circle11 = circle(random.randint(25,635), 80)


topCircles = [circle1, circle2, circle3, circle4, circle5, circle6, circle7]
bottomCircles = [circle8, circle9, circle10, circle11]
all = [circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9, circle10, circle11]



while True:
    clock.tick(30)
    pygame.display.update()
    screen.fill(black)
    for each in topCircles:
        # print(circle.xMotion)
        each.defMove()
        each.draw_shapes()
    for each in bottomCircles:
        # print(each.xMotion)
        each.defMove()
        each.draw_shapes()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            print(event.key)
            for each in all:
                if chr(event.key) == each.key:
                    each.flag = True
                    print(each.key,'we got the key!')
                    each.timesPressed = each.timesPressed+1
                    print(each.key, each.timesPressed)
                    evenNum = each.timesPressed % 2
                    if each.timesPressed == 2:
                        each.flag = False

                    




       





