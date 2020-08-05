import pygame
import random
from Tkinter import*
import os
import copy
import math


class Block():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,[self.x,self.y,20,20])

class Snake():

    def __init__(self,tricky_on=False,dir="s",frame=10):
        self.xspeed = 0
        self.yspeed = 0
        x,y = random.randint(0,39)*20,random.randint(0,39)*20
        self.blocks = []
        self.blocks.append(Block(x,y,(0,255,0)))
        self.tricky_on = tricky_on
        self.dir = dir
        self.frame = frame

    def move(self,screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                length = len(self.blocks)
                if keys[pygame.K_LEFT]:
                    if(self.dir == "right" and length>1):
                        break
                    if(self.tricky_on):
                        self.xspeed = 1
                        self.yspeed = 0
                    else:
                        self.xspeed = -1
                        self.yspeed = 0
                    self.dir = "left"
                elif keys[pygame.K_RIGHT]:
                    if(self.dir == "left" and length>1):
                        break
                    if(self.tricky_on):
                        self.xspeed = -1
                        self.yspeed = 0
                    else:
                        self.xspeed = 1
                        self.yspeed = 0
                    self.dir = "right"
                elif keys[pygame.K_UP]:
                    if(self.dir == "down" and length>1):
                        break
                    if(self.tricky_on):
                        self.xspeed = 0
                        self.yspeed = 1
                    else:
                        self.xspeed = 0
                        self.yspeed = -1
                    self.dir = "up"
                elif keys[pygame.K_DOWN]:
                    if(self.dir == "up" and length>1):
                        break
                    if(self.tricky_on):
                        self.xspeed = 0
                        self.yspeed = -1
                    else:
                        self.xspeed = 0
                        self.yspeed = 1
                    self.dir = "down"


        if(self.blocks[0].x > 780 or self.blocks[0].y > 780 or
            self.blocks[0].x < 0 or self.blocks[0].y < 0):
            os.execl(sys.executable, sys.executable, *sys.argv)

        for i in range(len(self.blocks)-1):
            head = self.blocks[0]
            part = self.blocks[i+1]
            if(part.x == head.x and part.y == head.y):
                os.execl(sys.executable, sys.executable, *sys.argv)

    def draw(self,screen):
        for i, e in reversed(list(enumerate(self.blocks))):
            if(i == 0):
                self.blocks[i].x += 20*self.xspeed
                self.blocks[i].y += 20*self.yspeed
            else:
                self.blocks[i].x = self.blocks[i-1].x
                self.blocks[i].y = self.blocks[i-1].y

        self.update(screen)

    def update(self,screen):
        for i in range(len(self.blocks)):
            self.blocks[i].draw(screen)

    def grow(self,screen):
        #gets the last and second last pieces of the snake
        length = len(self.blocks)
        if(length%2!=0):
            #color = (0,0,0)
            color = (0,255,0)
        else:
            color = (0,255,0)
        if (length > 1):
            last = self.blocks[length-1]
            sec_last = self.blocks[length-2]
            xdiff = sec_last.x - last.x
            ydiff = sec_last.y - last.y

            if(xdiff == 20 and ydiff == 0):
                self.blocks.append(Block(last.x-20,last.y,color))
            elif(xdiff == -20 and ydiff == 0):
                self.blocks.append(Block(last.x+20,last.y,color))
            elif(xdiff == 0 and ydiff == 20):
                self.blocks.append(Block(last.x,last.y-20,color))
            elif(xdiff == 0 and ydiff == -20):
                self.blocks.append(Block(last.x,last.y+20,color))
        else:
            head = self.blocks[0]

            if(self.xspeed == -1 and self.yspeed == 0):
                self.blocks.append(Block(head.x,head.y,color))
            elif(self.xspeed == 1 and self.yspeed == 0):
                self.blocks.append(Block(head.x,head.y,color))
            elif(self.xspeed == 0 and self.yspeed == -1):
                self.blocks.append(Block(head.x,head.y,color))
            elif(self.xspeed == 0 and self.yspeed == 1):
                self.blocks.append(Block(head.x,head.y,color))
        set_food(screen)

def create_window(screen):
    screen.fill((127,127,127))
    eat(screen)
    s.draw(screen)
    for i in range(41):
        pygame.draw.line(screen,(255,255,255),(0+20*i,0),(0+20*i,801))
        pygame.draw.line(screen,(255,255,255),(0,0+20*i),(801,0+20*i))
    pygame.display.update()

def set_food(screen):
    global food,food2,food3,food4
    x,y = random.randint(0,39)*20,random.randint(0,39)*20
    for i in range(len(s.blocks)):
        piece = s.blocks[i]
        while(piece.x == x and piece.y == y):
            x,y = random.randint(0,39)*20,random.randint(0,39)*20

    food = Block(x,y,(255,0,0))

    x1,y1 = random.randint(0,39)*20,random.randint(0,39)*20
    for i in range(len(s.blocks)):
        piece = s.blocks[i]
        while(piece.x == x and piece.y == y):
            x1,y1 = random.randint(0,39)*20,random.randint(0,39)*20
pygame.time.delay(600)
    food2 = Block(x1,y1,(0,0,0))

    x2,y2 = random.randint(0,39)*20,random.randint(0,39)*20
    for i in range(len(s.blocks)):
        piece = s.blocks[i]
        while(piece.x == x and piece.y == y):
            x2,y2 = random.randint(0,39)*20,random.randint(0,39)*20

    food3 = Block(x2,y2,(0,0,255))

    x3,y3 = random.randint(0,39)*20,random.randint(0,39)*20
    for i in range(len(s.blocks)):
        piece = s.blocks[i]
        while(piece.x == x and piece.y == y):
            x3,y3 = random.randint(0,39)*20,random.randint(0,39)*20

    food4 = Block(x3,y3,(255,255,0))

def eat(screen):
    if (s.blocks[0].x == food.x and s.blocks[0].y == food.y):
        s.tricky_on = False
        s.frame = 10
        s.grow(screen)
    if(s.blocks[0].x == food2.x and s.blocks[0].y == food2.y):
        s.tricky_on = False
        s.frame = 10
        rand = random.randint(1,10)
        for i in range(rand):
            s.grow(screen)
            s.update(screen)
        rand = float(random.randint(1,99))/100
        rand = int(len(s.blocks)*rand)
        for i in range(rand):
            s.blocks.pop(len(s.blocks)-1)
    if(s.blocks[0].x == food3.x and s.blocks[0].y == food3.y):
        s.tricky_on = True
        s.frame = 10
        for i in range(5):
            s.grow(screen)
    if(s.blocks[0].x == food4.x and s.blocks[0].y == food4.y):
        s.tricky_on = False
        s.frame = 25
        for i in range(25):
            s.grow(screen)
    else:
        food.draw(screen)
        if(len(s.blocks)>1):
            food2.draw(screen)
            food3.draw(screen)
            food4.draw(screen)

def main():
    global s
    pygame.init()
    size = 801, 801
    screen = pygame.display.set_mode(size)
    s = Snake()
    set_food(screen)
    clock = pygame.time.Clock()
    running = True
    while running:
        pygame.time.delay(1)
        clock.tick(s.frame)
        s.move(screen)
        create_window(screen)


main()
