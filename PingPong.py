#!/usr/bin/python
import pygame as pygame
import random as random
import math as math
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
        for i in range(2):
            self.pos[i] = self.pos[i] + self.movement[i]

class Player():
    def __init__(self,size,pos,movement,color, richtung):
        self.size = size
        self.movement = movement
        self.pos = pos
        self.color = color
        self.arrowkonst = math.pi/2
        self.richtung = richtung

    def move(self, screenData, upkey, downkey):
        screen ,screen_width, screen_height, Clock = screenData
        if upkey==1 and 100 < self.pos[1]-self.size[1]/2:
            self.pos[1] = self.pos[1] - self.movement[1]
        if downkey==1 and screen_height-100 > self.pos[1]+self.size[1]/2:
            self.pos[1] = self.pos[1] + self.movement[1]

    def show(self,screenData):
        screen ,screen_width, screen_height, Clock = screenData
        PlayerRect = pygame.Rect(self.pos[0]-(self.size[0]/2), self.pos[1]-(self.size[1]/2), self.size[0], self.size[1])
        pygame.draw.rect(screen , self.color , PlayerRect)

    def Schussrichtung(self,screenData,upkey,downkey):
        screen ,screen_width, screen_height, Clock = screenData
        if upkey==1 and  self.arrowkonst < math.pi:
            self.arrowkonst = self.arrowkonst+math.pi/100
        if downkey==1 and  self.arrowkonst > 0:
            self.arrowkonst = self.arrowkonst-math.pi/100
        if self.richtung == 'l':
            lineendpos = (self.pos[0]-(self.size[0]/2)-math.sin(self.arrowkonst)*50, self.pos[1]+math.cos(self.arrowkonst)*50)
            linestartpos = (self.pos[0]-self.size[0], self.pos[1])
        else:
            lineendpos = (self.pos[0]+self.size[0]+math.sin(self.arrowkonst)*50, self.pos[1]+math.cos(self.arrowkonst)*50)
            linestartpos = (self.pos[0]+self.size[0], self.pos[1])
        pygame.draw.line(screen, self.color, linestartpos, lineendpos)

    def collision(self,ball):
        if abs(self.pos[0]-ball.pos[0]) < (self.size[0]/2)+(ball.size[0]/2):
            if abs(self.pos[1]-ball.pos[1]) < (self.size[1]/2)+(ball.size[1]/2):
                xabstand = abs(abs(self.pos[0]-ball.pos[0]) - self.size[0])
                yabstand = abs(abs(self.pos[1]-ball.pos[1]) - self.size[1])
                if self.richtung == 'l':
                    if xabstand <= yabstand:
                        if self.pos[0]<ball.pos[0]:
                            print('laal')
                            ball.movement[0] = -math.sin(self.arrowkonst) * math.sqrt(ball.movement[0]**2 + ball.movement[1]**2)
                            ball.movement[1] = -math.cos(self.arrowkonst) * math.sqrt(ball.movement[0]**2 + ball.movement[1]**2)
                        else:
                            ball.movement[1] = -ball.movement[1]
                        if xabstand >= yabstand:
                            ball.movement[0] = -ball.movement[0]
                else:
                    if xabstand <= yabstand:
                        if self.pos[0]<ball.pos[0]:
                            print('laal')
                            ball.movement[0] = math.sin(self.arrowkonst) * math.sqrt(ball.movement[0]**2 + ball.movement[1]**2)
                            ball.movement[1] = -math.cos(self.arrowkonst) * math.sqrt(ball.movement[0]**2 + ball.movement[1]**2)
                        else:
                            ball.movement[1] = -ball.movement[1]
                        if xabstand >= yabstand:
                            ball.movement[0] = -ball.movement[0]

                return True
        return False


class Powerup():
    def __init__(self,pos,effect,image):
        self.pos = pos
        self.effect = effect

    #def

# def collision(Fixed, Moved):
#     if abs(Fixed.pos[0]-Moved.pos[0]) < (Fixed.size[0]/2)+(Moved.size[0]/2):
#         if abs(Fixed.pos[1]-Moved.pos[1]) < (Fixed.size[1]/2)+(Moved.size[1]/2):
#             xabstand = abs(abs(Fixed.pos[0]-Moved.pos[0]) - Fixed.size[0])
#             yabstand = abs(abs(Fixed.pos[1]-Moved.pos[1]) - Fixed.size[1])
#             if Fixed.richtung == 'l':
#                 if xabstand <= yabstand:
#                     if Fixed.pos[0]<Moved.pos[0]:
#                         print('laal')
#                         Moved.movement[0] = -math.sin(Fixed.arrowkonst) * math.sqrt(Moved.movement[0]**2 + Moved.movement[1]**2)
#                         Moved.movement[1] = -math.cos(Fixed.arrowkonst) * math.sqrt(Moved.movement[0]**2 + Moved.movement[1]**2)
#                     else:
#                         Moved.movement[1] = -Moved.movement[1]
#                     if xabstand >= yabstand:
#                         Moved.movement[0] = -Moved.movement[0]
#             else:
#                 if xabstand <= yabstand:
#                     if Fixed.pos[0]>Moved.pos[0]:
#                         print('laal')
#                         Moved.movement[0] = math.sin(Fixed.arrowkonst) * math.sqrt(Moved.movement[0]**2 + Moved.movement[1]**2)
#                         Moved.movement[1] = -math.cos(Fixed.arrowkonst) * math.sqrt(Moved.movement[0]**2 + Moved.movement[1]**2)
#                     else:
#                         Moved.movement[1] = -Moved.movement[1]
#                     if xabstand >= yabstand:
#                         Moved.movement[0] = -Moved.movement[0]
#
#             return True
#     return False



def PingPong(screenData, pos, button, Mode, Run):
    screen ,screen_width, screen_height, Clock= screenData
    ball = Ball((20,20), [screen_width/2, screen_height/2], [3.5,3], gs.red)
    playerl = Player((20,100), [200, screen_height/2], [10,10], gs.white, 'r')
    playerr = Player((20,100), [screen_width-200, screen_height/2], [10,10], gs.white, 'l')

    while Mode == 'PingPong':
        print(ball.movement)
        Mode, Run, pos, button = gs.clear(screenData, pos, button, Mode, clock=True)
        #Male das Feld
        FeldRect = pygame.Rect(100, 100, screen_width-200, screen_height-200)
        pygame.draw.rect(screen , gs.white , FeldRect)
        FeldRect = pygame.Rect(102, 102, screen_width-204, screen_height-204)
        pygame.draw.rect(screen , gs.black , FeldRect)

        playerl.show(screenData)
        playerl.move(screenData, pygame.key.get_pressed()[119], pygame.key.get_pressed()[115])
        playerl.Schussrichtung(screenData, pygame.key.get_pressed()[97], pygame.key.get_pressed()[100])

        playerr.show(screenData)
        playerr.move(screenData, pygame.key.get_pressed()[273], pygame.key.get_pressed()[274])
        playerr.Schussrichtung(screenData, pygame.key.get_pressed()[276], pygame.key.get_pressed()[275])

        playerlcollision = playerl.collision(ball)
        playerrcollision = playerr.collision(ball)

        ball.show(screenData)
        ball.move()
        ball.checkpos(screenData)




    return Mode, Run, pos, button
