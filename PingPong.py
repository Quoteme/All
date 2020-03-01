#!/usr/bin/python
import pygame as pygame
import random as random
import GeneralStructures as gs

class Ball():
    def __init__(self,size,pos,movement,color):
        self.size = size
        self.movement = movement
        self.pos = pos
        self.color = color

    def show(self,screenData):
        screen ,screen_width, screen_height, Clock= screenData
        BallRect = pygame.Rect(self.pos[0]-(self.size[0]/2), self.pos[1]-(self.size[1]/2), self.size[0], self.size[1])
        pygame.draw.rect(screen , self.color , BallRect)


    def checkpos(self,screenData):
        screen ,screen_width, screen_height, Clock= screenData
        if not (100+self.size[0]/2 < self.pos[0] <screen_width-(100+self.size[0]/2)):
            self.movement[0] = -self.movement[0]
        if not (100+self.size[1]/2 < self.pos[1] <screen_height-(100+self.size[1]/2)):
            self.movement[1] = -self.movement[1]
        return self

    def move(self):
        print(self.pos)
        for i in range(2):
            self.pos[i] = self.pos[i] + self.movement[i]

class Player():
    def __init__(self,size,pos,movement,color):
        self.size = size
        self.movement = movement
        self.pos = pos
        self.color = color

    def move(self, screenData, upkey, downkey):
        screen ,screen_width, screen_height, Clock= screenData
        if upkey==1 and 100 < self.pos[1]-self.size[1]/2:
            self.pos[1] = self.pos[1] - self.movement[1]
        if downkey==1 and screen_height-100 > self.pos[1]+self.size[1]/2:
            self.pos[1] = self.pos[1] + self.movement[1]

    def show(self,screenData):
        screen ,screen_width, screen_height, Clock= screenData
        PlayerRect = pygame.Rect(self.pos[0]-(self.size[0]/2), self.pos[1]-(self.size[1]/2), self.size[0], self.size[1])
        pygame.draw.rect(screen , self.color , PlayerRect)



def PingPong(screenData, pos, button, Mode, Run):
    screen ,screen_width, screen_height, Clock= screenData
    ball = Ball((200,400), [screen_width/2, screen_height/2], [3,30swswsswswsw], gs.red)
    playerl = Player((20,100), [200, screen_height/2], [10,10], gs.white)
    playerr = Player((20,100), [screen_width-200, screen_height/2], [10,10], gs.white)

    while Mode == 'PingPong':
        Mode, Run, pos, button = gs.clear(screenData, pos, button, Mode, clock=True)
        #Male das Feld
        FeldRect = pygame.Rect(100, 100, screen_width-200, screen_height-200)
        pygame.draw.rect(screen , gs.white , FeldRect)
        FeldRect = pygame.Rect(102, 102, screen_width-204, screen_height-204)
        pygame.draw.rect(screen , gs.black , FeldRect)

        playerl.show(screenData)
        playerl.move(screenData, pygame.key.get_pressed()[119], pygame.key.get_pressed()[115])

        playerr.show(screenData)
        playerr.move(screenData, pygame.key.get_pressed()[275], pygame.key.get_pressed()[274])

        ball.show(screenData)
        ball.move()
        ball.checkpos(screenData)




    return Mode, Run, pos, button
