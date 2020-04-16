#!/usr/bin/python
import pygame as pygame
import GeneralStructures as gs
import math as math

def checkMandelbrot(a,b):
    itt = 0
    z = [0,0]
    while betrag(z[0], z[1])<=2 and itt<100:
        itt = itt + 1
        z[0], z[1] = z[0]**2 - z[1]**2 + a , 2*(z[0]*z[1])+b
        #print(z)
    return itt

def betrag(a,b):
    return math.sqrt(a*a +b*b)

def Mandelbrot(screenData, pos, button, Mode, Run):
    screen ,screen_width, screen_height, Clock= screenData
    if Mode == 'Mandelbrot':
        Mode, Run, pos, button = gs.clear(screenData, pos, button, Mode, clock=True)
        n = 1
        for i in range(300,screen_width-299,n):
            for j in range(20,screen_height+1,n):
                Mode, Run = gs.OberLeiste(screenData, pos, button, Mode)
                #Clock.tick(100)
                a = ((-(screen_width/2)+i)*7)/(screen_width)
                b = -((-(screen_height/2)+j)*4)/(screen_height)

                rect = pygame.Rect(i, j, n, n)
                itt = checkMandelbrot(a,b)
                print(i,j)
                if itt == 100:
                    color = pygame.Color(0, 0, 0)
                else:
                    newitt = -100*(1.05**(-itt))+100
                    color = pygame.Color(0, 0, round(2.55*newitt))

                pygame.draw.rect(screen, color, rect)
                pygame.display.update()
        while Mode == 'Mandelbrot':
            laal ='LaaL'
            Clock.tick(100)

    return Mode, Run, pos, button
