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

    def __init__(self, x, y, key):
        self.x = x
        self.y = y
        self.yMotion = random.randint(1,4)
        self.color = random.choice(colors)
        self.key =  key
        
    def draw_shapes(self):

        balloon_image = pygame.image.load("C:/Users/plesk/Downloads/balloon-sprite-removebg-preview.png")
        balloon_sprite = pygame.transform.scale(balloon_image, (60, 60))
        screen.blit(balloon_sprite, (self.x, self.y))
        showtext('{}'.format(self.key), self.x-10, self.y-15, white)
    
       
    def move(self):
        self.y -= self.yMotion
 
 
key_list = []
circles_list = []

for x in range(10):
    letter = chr(random.randint(97, 122))
    key_list.append(letter)
    circle = balloon(random.randint(30,560), 530, letter)
    circles_list.append(circle)

decrease = 0
score = 0
check = False


while True:
    screen.fill(black)

    clock.tick(30)
    showtext('Score: {}'.format(score), 480, 25, white)

    for c in circles_list:
        c.move()
        c.draw_shapes()

    #scoring  
    if score >= 10:
        showtext('You Won!', 250, 300, white)
        pygame.display.update()
        time.sleep(3)
        break

    if score <= -3:
        showtext('You lost! Too many wrong guesses!', 20, 15, white)
        pygame.display.update()
        time.sleep(3)
        break


    #balloon went off screen- end game
    if c.y+25 <= 0:
        showtext('You lost! A balloon went off the screen.', 50, 320, white)
        pygame.display.update()
        time.sleep(3)
        break

    if score % 2 == 0:
        yMotion = 5

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
                    score+= 1
                    circles_list.remove(balloon_object)
                    key_list.remove(key_pressed)
                    #balloon pop sprite
                    balloon_pop_image = pygame.image.load("C:/Users/plesk/Downloads/balloon_pop-removebg-preview.png")
                    balloon_pop_sprite = pygame.transform.scale(balloon_pop_image, (150, 150))
                    screen.blit(balloon_pop_sprite, (balloon_object.x-45, balloon_object.y-45))
                    pygame.display.update()
                    time.sleep(0.5)
                    break

            else:
                letter = chr(random.randint(97, 122))
                key_list.append(letter)
                circle = balloon(random.randint(25,500), random.randint(25,550), letter)
                circles_list.append(circle)
                score -= 1


    pygame.display.update()


        
