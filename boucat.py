from turtle import back
import pygame
from pygame.locals import *
from sys import exit
import sched
import threading
import time


pygame.init()

width = 640
height = 480

black_color = (0,0,0)
white_color = (255,255,255)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sprites')

font = pygame.font.SysFont('arial',30 ,True, True)

class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/background/sprite_00.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_01.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_02.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_03.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_04.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_05.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_06.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_07.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_08.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_09.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_10.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_11.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_12.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_13.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_14.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_15.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_16.png'))
        self.sprites.append(pygame.image.load('sprites/background/sprite_17.png'))
        self.current = 0
        self.image = self.sprites[self.current]
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0

    def update(self):
        self.current += 0.1
        if self.current >= len(self.sprites):
            self.current = 0
    
        self.image = self.sprites[int(self.current)]
        self.image = pygame.transform.scale(self.image, (width, height))

class Bou(pygame.sprite.Sprite):

    hunger = 100
    tired = 0
    joy = 100
    alive = True

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/sprite_0.png'))
        self.sprites.append(pygame.image.load('sprites/sprite_1.png'))
        self.sprites.append(pygame.image.load('sprites/sprite_1.png'))
        self.sprites.append(pygame.image.load('sprites/sprite_2.png'))
        self.sprites.append(pygame.image.load('sprites/sprite_2.png'))
        self.sprites.append(pygame.image.load('sprites/sprite_3.png'))
        self.sprites.append(pygame.image.load('sprites/sprite_3.png'))
        self.current = 0
        self.image = self.sprites[self.current]
        self.image = pygame.transform.scale(self.image, (32*6, 32*6))

        self.shine = False
        self.eating = False
        self.sleeping = False
        self.awake = False
        self.action = False
        self.playing = False

        self.sprites_action = []
        self.sprites_action.append(pygame.image.load('sprites/action/sprite_0.png'))
        self.sprites_action.append(pygame.image.load('sprites/action/sprite_1.png'))
        self.sprites_action.append(pygame.image.load('sprites/action/sprite_2.png'))
        self.sprites_action.append(pygame.image.load('sprites/action/sprite_3.png'))
        self.sprites_action.append(pygame.image.load('sprites/action/sprite_4.png'))
        self.sprites_action.append(pygame.image.load('sprites/action/sprite_5.png'))
        self.sprites_action.append(pygame.image.load('sprites/action/sprite_6.png'))
        self.sprites_action.append(pygame.image.load('sprites/action/sprite_7.png'))

        self.sprites_action_eat = []
        self.sprites_action_eat.append(pygame.image.load('sprites/action/eat/sprite_0.png'))
        self.sprites_action_eat.append(pygame.image.load('sprites/action/eat/sprite_1.png'))
        self.sprites_action_eat.append(pygame.image.load('sprites/action/eat/sprite_2.png'))
        self.sprites_action_eat.append(pygame.image.load('sprites/action/eat/sprite_3.png'))
        self.sprites_action_eat.append(pygame.image.load('sprites/action/eat/sprite_4.png'))
        self.sprites_action_eat.append(pygame.image.load('sprites/action/eat/sprite_5.png'))
        self.sprites_action_eat.append(pygame.image.load('sprites/action/eat/sprite_6.png'))
        self.sprites_action_eat.append(pygame.image.load('sprites/action/eat/sprite_6.png'))
        self.sprites_action_eat.append(pygame.image.load('sprites/action/eat/sprite_6.png'))

        self.sprites_action_sleep = []
        self.sprites_action_sleep.append(pygame.image.load('sprites/action/sleep/sprite_0.png'))
        self.sprites_action_sleep.append(pygame.image.load('sprites/action/sleep/sprite_1.png'))
        self.sprites_action_sleep.append(pygame.image.load('sprites/action/sleep/sprite_2.png'))
        self.sprites_action_sleep.append(pygame.image.load('sprites/action/sleep/sprite_3.png'))
        self.sprites_action_sleep.append(pygame.image.load('sprites/action/sleep/sprite_0.png'))
        self.sprites_action_sleep.append(pygame.image.load('sprites/action/sleep/sprite_1.png'))
        self.sprites_action_sleep.append(pygame.image.load('sprites/action/sleep/sprite_2.png'))
        self.sprites_action_sleep.append(pygame.image.load('sprites/action/sleep/sprite_3.png'))

        self.sprites_action_awake = []
        self.sprites_action_awake.append(pygame.image.load('sprites/action/awake/sprite_0.png'))
        self.sprites_action_awake.append(pygame.image.load('sprites/action/awake/sprite_1.png'))
        self.sprites_action_awake.append(pygame.image.load('sprites/action/awake/sprite_2.png'))
        self.sprites_action_awake.append(pygame.image.load('sprites/action/awake/sprite_3.png'))
        self.sprites_action_awake.append(pygame.image.load('sprites/action/awake/sprite_4.png'))
        self.sprites_action_awake.append(pygame.image.load('sprites/action/awake/sprite_4.png'))
        self.sprites_action_awake.append(pygame.image.load('sprites/action/awake/sprite_4.png'))

        self.sprites_action_play = []
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_00.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_01.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_02.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_03.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_04.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_05.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_06.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_07.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_08.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_09.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_10.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_11.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_12.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_13.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_14.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_15.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_16.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_17.png'))
        self.sprites_action_play.append(pygame.image.load('sprites/action/play/sprite_18.png'))

        self.rect = self.image.get_rect()
        self.rect.topleft = 215, 300
    
    def update(self):
        if self.shine:
            self.current += 0.1
            if self.current >= len(self.sprites_action):
                self.current = 0
                self.shine = False
                self.action = False
            
            self.image = self.sprites_action[int(self.current)]
            self.image = pygame.transform.scale(self.image, (32*6, 32*6))

        elif self.eating:
            self.current += 0.1
            if self.current >= len(self.sprites_action_eat):
                self.current = 0
                self.eating = False
                self.action = False
            
            self.image = self.sprites_action_eat[int(self.current)]
            self.image = pygame.transform.scale(self.image, (32*6, 32*6))
        elif self.sleeping:
            self.current += 0.01
            if self.current >= len(self.sprites_action_sleep):
                self.current = 0
                self.sleeping = False   
                self.awake = True
                self.action = False
            
            self.image = self.sprites_action_sleep[int(self.current)]
            self.image = pygame.transform.scale(self.image, (32*6, 32*6))
        elif self.awake:
            self.current += 0.05
            if self.current >= len(self.sprites_action_awake):
                self.current = 0
                self.awake = False   
                self.action = False
            
            self.image = self.sprites_action_awake[int(self.current)]
            self.image = pygame.transform.scale(self.image, (32*6, 32*6))

        elif self.playing:
            self.current += 0.1
            if self.current >= len(self.sprites_action_play):
                self.current = 0
                self.playing = False   
                self.action = False
            
            self.image = self.sprites_action_play[int(self.current)]
            self.image = pygame.transform.scale(self.image, (32*6, 32*6))

        elif not self.alive:
            self.image = pygame.image.load('sprites/action/dead/sprite_0.png')
            self.image = pygame.transform.scale(self.image, (32*6, 32*6))
        else:
            self.current += 0.1
            if self.current >= len(self.sprites):
                self.current = 0
                self.action = False
            
            self.image = self.sprites[int(self.current)]
            self.image = pygame.transform.scale(self.image, (32*6, 32*6))

    def shinee(self):
        self.shine = True
        self.action = True

    def eat(self):
        if self.hunger >= 110:
            self.hunger = 110
        else:
            self.hunger += 5
        self.eating = True
        self.action = True

    def sleep(self):
        if self.tired >= 10:
            self.tired -= 10
        else:
            self.tired = 0

        self.sleeping = True
        self.action = True

    def play(self):
        if self.joy >= 100:
            self.joy = 100
        else:
            self.joy += 5
        self.playing = True

    def pass_time(self):
        if self.hunger <= -10 or self.tired >= 100:
            self.alive = False
        self.hunger -= 3
        self.joy -= 2
        if not self.sleeping:
            self.tired += 2


all_sprites_bou = pygame.sprite.Group()
all_sprites_background = pygame.sprite.Group()

bou = Bou()
all_sprites_bou.add(bou)

background = Background()
all_sprites_background.add(background)

clock = pygame.time.Clock()

def main():
    s =  sched.scheduler(time.time, time.sleep)
    def run(sc):
        bou.pass_time()
        if bou.alive:
            s.enter(10, 1, run, (sc,))
        
    s.enter(10, 1, run, (s,))
    t = threading.Thread(target=s.run)
    t.start()  

if __name__ == "__main__":
    main()

while True:
    clock.tick(30)
    window.fill((white_color))

    bou_name = 'Rogerio'
    text = font.render(bou_name, True, white_color)

    if bou.sleeping:
        s =  sched.scheduler(time.time, time.sleep)
        bou_tired = 'Tired: ' + str(bou.tired) + " ( -10 )"
        text_tired = font.render(bou_tired, True, white_color)
    else:
        bou_tired = 'Tired: ' + str(bou.tired)
        text_tired = font.render(bou_tired, True, white_color)

    if bou.eating:
        s =  sched.scheduler(time.time, time.sleep)
        bou_food = 'Food: ' + str(bou.hunger) + " ( +5 )"
        text_hunger = font.render(bou_food, True, white_color)

    else:
        bou_food = 'Food: ' + str(bou.hunger)
        text_hunger = font.render(bou_food, True, white_color)

    if bou.playing:
        s =  sched.scheduler(time.time, time.sleep)
        bou_joy = 'Joy: ' + str(bou.joy) + " ( +5 )"
        text_joy = font.render(bou_joy, True, white_color)
    else:
        bou_joy = 'Joy: ' + str(bou.joy)
        text_joy = font.render(bou_joy, True, white_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN :
            if event.key == K_t and bou.action == False:
                bou.shinee()
            if event.key == K_f and bou.action == False:
                bou.eat()
            if event.key == K_g and bou.action == False:
                bou.sleep()
            if event.key == K_h and bou.action == False:
                bou.play()

    
    all_sprites_background.draw(window)
    all_sprites_background.update()

    all_sprites_bou.draw(window)
    all_sprites_bou.update()

    # window.blit(text, (170, 90))
    window.blit(text_hunger, (30, 5))
    window.blit(text_tired, (30, 40))
    window.blit(text_joy, (30, 75))
    pygame.display.flip()

