from pygame.constants import KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, MOUSEBUTTONDOWN, QUIT

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
# def showtext(msg,x,y,color):
#     font = pygame.font.SysFont("freesans", 32)
#     msgobj = font.render(msg,False,white)
#     screen.blit(msgobj,(x,y))


# class circle:
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.xMotion = random.randint(1,4)
#         self.color = random.choice(colors)
#         self.key =  random.choice(keys)
#         self.flag = False
#         self.timesPressed = 0
        
#     def draw_shapes(self):
#         if self.flag == False:
#             pygame.draw.circle(screen, self.color, (self.x, self.y), 25, 1)
#             showtext('{}'.format(self.key), self.x-10, self.y-15, white)
#         if self.flag == True:
#             pygame.draw.circle(screen, black, (self.x, self.y), 25, 1)

            

#             # if self.timesPressed == 2:
#             #     self.flag = False
       
#     def defMove(self):
#         self.x += self.xMotion
#         if self.x+25 >= 600:
#             self.xMotion = -random.randint(1,4)
#         if self.x-25 <= 0:
#             self.xMotion = random.randint(1,4)

# keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# keyChoice = random.choice(keys)

# circle1 = circle(random.randint(0,635), 30)
# circle2 = circle(random.randint(0,635), 30)
# circle3 = circle(random.randint(0,635), 30)
# circle4 = circle(random.randint(0,635), 30)
# circle5 = circle(random.randint(0,635), 30)
# circle6 = circle(random.randint(0,635), 30)
# circle7 = circle(random.randint(0,635), 30)

# circle8 = circle(random.randint(25,635), 80)
# circle9 = circle(random.randint(25,635), 80)
# circle10 = circle(random.randint(25,635), 80)
# circle11 = circle(random.randint(25,635), 80)


# topCircles = [circle1, circle2, circle3, circle4, circle5, circle6, circle7]
# bottomCircles = [circle8, circle9, circle10, circle11]
# all = [circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9, circle10, circle11]



# while True:
#     clock.tick(30)
#     pygame.display.update()
#     screen.fill(black)
#     for each in topCircles:
#         # print(circle.xMotion)
#         each.defMove()
#         each.draw_shapes()
#     for each in bottomCircles:
#         # print(each.xMotion)
#         each.defMove()
#         each.draw_shapes()

#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         elif event.type == KEYDOWN:
#             print(event.key)
#             for each in all:
#                 if chr(event.key) == each.key:
#                     each.flag = True
#                     print(each.key,'we got the key!')
#                     each.timesPressed = each.timesPressed+1
#                     print(each.key, each.timesPressed)
#                     if each.timesPressed % 2 == 0:
#                         each.flag = False
#                     # evenNum = each.timesPressed % 2
#                     # if each.timesPressed == 2:
#                     #     each.flag = False


# def showtext(msg,x,y,color):
#     font = pygame.font.SysFont("freesans", 32)
#     msgobj = font.render(msg,False,white)
#     screen.blit(msgobj,(x,y))

# placement_finisher_list = []



# class Circle:
#     global finishers
#     finishers = 0
#     def __init__(self, y):
#         self.x = 40
#         self.y = y
#         self.xMotion = random.randint(1,4)
#         self.color = random.choice(colors) 
#         self.lap_count = 0
        
#     def draw_shapes(self):
#         # for each in circles:
#         #         placement_finisher_list.append(self.placement_count)
#         #         for eachC in placement_finisher_list:
#         #             max(placement_finisher_list) +1
    
#         pygame.draw.circle(screen, self.color, (self.x, self.y), 25, 1)

#     def checkCircles(self, finishers):

#         if self.lap_count >= 2:
#             finishers += 1
#             print('self.lap_count is >= to 2')
            
#             if finishers == 1:
            
#                 self.color = red
#                 self.x = 40
#             if finishers == 2:
            
#                 self.color = blue
#                 self.x = 40
#             if finishers == 3:
            
#                 self.color = green
#                 self.x = 40 
#             if finishers >= 4:

#                 self.x = 40
#                 self.color = purple

#     def move_shapes(self):
#         self.x += self.xMotion
#         if self.x+25 >= 600:
#             self.xMotion = -random.randint(1,4)
#         if self.x-25 <= 0:
#             self.xMotion = random.randint(1,4)

#         if finishers >= 1:
#             showtext('WE HAVE A WINNER!!', 160, 40, white)

# circle1 = Circle(40)
# circle2 = Circle(110)
# circle3 = Circle(180)
# circle4 = Circle(250)
# circle5 = Circle(320)
# circle6 = Circle(390)
# circle7 = Circle(460)
# circle8 = Circle(530)
# circle9 = Circle(600)
# circle10 = Circle(660)

# circles = [circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9, circle10]


# while True:
#     clock.tick(30)
#     pygame.display.update()
#     screen.fill(black)

#     for c in circles:
#         c.draw_shapes()
#         c.move_shapes()
#         c.checkCircles(finishers)


#     for event in pygame.event.get():
#         if event.type == QUIT:
#                 pygame.quit()
#                 exit()

#     for c in circles:
#         if c.x-25 == 0:
#             c.lap_count+=1
            
            # if c.lap_count >= 2:
            #     finishers += 1
            # if c.lap_count == 0:
            #     print(finishers)
            #     print('lap_count = 0')
            #     print(finishers)
            # if c.lap_count == 1:
            #     print('lap_count = 0')
            #     print(finishers)
            # if c.lap_count == 2:
            #     print(finishers)
            
            

        # elif event.type == KEYDOWN:
        #         if event.key == K_SPACE:
        #             for each in all:
        #                 each.move_shapes()

#test
# class Circle:
#     radius = 15
#     def __init__(self):
#         pass
#     def draw(self):
#         pygame.draw.circle(screen, blue, (self.x, self.y), 25, 1)

# ob1 = Circle()
# ob2 = Circle()
# #changes the radius for all objects
# Circle.radius = 20
# #changes the radius for one object
# ob1.radius = 17
# print(ob1.radius)
# print(Circle.radius)
# print(ob2.radius)


# class Circle:
#     radius = 20
#     def __init__(self):
#         self.x = random.randint(10,590)
#         self.y = random.randint(10, 690)
#         self.color = random.choice(colors)
#     def draw(self):
#         pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 1)

# circle1 = Circle()
# circle2 = Circle()
# circle3 = Circle()
# circle4 = Circle()
# circle5 = Circle()
# circle6 = Circle()
# circle7 = Circle()
# circle8 = Circle()
# circle9 = Circle()
# circle10 = Circle()

# circles = [circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9, circle10]


# while True:
#     screen.fill(black)
#     for c in circles:
#         c.draw()
    
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == KEYDOWN:
#                 if event.key == K_UP:
#                     Circle.radius = Circle.radius + 2
#                 if event.key == K_DOWN:
#                     Circle.radius = Circle.radius - 2 
#             elif event.type == MOUSEBUTTONDOWN:
#                 print(event.button)
#                 if event.button == 3:
#                     circle1.radius+= 5
#                     print('circle 1 radius += 5')

#                     x_co, y_co = pygame.mouse.get_pos()
#                     print(pygame.mouse.get_pos())
#                     if x_co in range(c.x - c.radius, c.x + c.radius) and  y_co in range(c.y - c.radius, c.y + c.radius):
#                     # if x_co in range(c.x, c.x + c.radius*2) and y_co in range(c.y + c.radius*2):
#                         print('mouse pos inside circle')
#                         c.radius = c.radius - 2
                    
#                 if event.button == 1:
#                     circle2.radius+=5
#                     print('circle 2 radius += 5')

#                     x_co, y_co = pygame.mouse.get_pos()
#                     print(pygame.mouse.get_pos())
#                     if x_co in range(c.x - c.radius, c.x + c.radius) and  y_co in range(c.y - c.radius, c.y + c.radius):
#                     # if x_co in range(c.x, c.x + c.radius*2) and y_co in range(c.y + c.radius*2):                    
#                         print('mouse pos inside circle')
#                         c.radius = c.radius + 2
#     clock.tick(50)
#     pygame.display.update()

#up and down circles 
circleColor = [red, blue]
class Circle():
    radius = 15
    def __init__(self):
        self.color = random.choice(circleColor)
        self.x = random.randint(30, 550)
        self.y = random.randint(30, 550)
        self.xSpeed = random.randint(1,3)
        self.ySpeed = random.randint(1,3)
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 1)
    def move(self):
        if self.color == red:
            c.x += c.xSpeed
            if c.x+15 > 600:
                c.xSpeed = -random.randint(1,3)
            if c.x-15 < 0:
                c.xSpeed = random.randint(1,3)
        if self.color == blue:
            c.y += c.ySpeed
            if c.y+15 > 600:
                c.ySpeed = -random.randint(1,3)
            if c.y-15 < 0:
                c.ySpeed = random.randint(1,3)


        # if self.color == red:
            #red moves horizontally
        # self.xSpeed = 2
        # self.ySpeed = 0
       

        # if self.color == blue:
        #     #blue moves vertically
        #     self.xSpeed = 0
        #     self.ySpeed = 2
        #     self.y += self.ySpeed
        #     if self.y-15 < 0 or self.y-15 > 700:
        #         self.ySpeed = -self.ySpeed
        
        

#circles 
circle1 = Circle()
circle2 = Circle()
circle3 = Circle()
circle4 = Circle()
circle5 = Circle()
circle6 = Circle()
circle7 = Circle()
circle8 = Circle()
circle9 = Circle()
circle10 = Circle()

circles = [circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9, circle10]


while True:
    screen.fill(black)
    # draw circle
    for c in circles:
        c.draw()
        c.move()
        
        
    pygame.display.update()
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

                

      
#Circle Race Game
import pygame, random
pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
class Circle():
    def __init__(self, color, x, y, radius, speed, lap):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.lap = lap
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
# colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (200, 200, 0)
# circles
circle = []
x = 50
radius = 25
lap = 0
for y in range(50, 550, 50):
    speed = random.randint(1, 5)
    c = Circle(white, x, y, radius, speed, lap)
    circle.append(c)
# positions
first = 1
second = 0
third = 0
while True:
    # fill
    screen.fill(black)
    # close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw circle
    for c in circle:
        c.draw()
        c.x = c.x + c.speed
        # bounce
        if c.x > 950 or c.x < 25:
            c.speed = -c.speed
        # lap count
        if c.x <= 25:
            c.lap = c.lap + 1
            print('circle', circle.index(c), 'lap', c.lap)
        # color change
        if c.lap >= 5 and first == 1:
            first = 0
            second = 1
            c.color = red
            c.x = 26
            c.speed = 0
            c.lap=-1
        elif c.lap >= 5 and second == 1:
            first = 0
            second = 0
            third = 1
            c.color = green
            c.x = 26
            c.speed = 0
            c.lap=-1
        elif c.lap >= 5 and third == 1:
            first = 0
            second = 0
            third = 0
            c.color = blue
            c.x = 26
            c.speed = 0
            c.lap=-1
    # clock
    clock.tick(100)
    # update
    pygame.display.update()



                




                    




       





