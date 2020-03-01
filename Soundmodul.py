#!/usr/bin/python
import pygame as pygame
import math as math
import GeneralStructures as gs

def Soundmodul(screenData, pos, button, Mode, Run):
    screen ,screen_width, screen_height, Clock= screenData

    while Mode == 'Soundmodul':
        Mode, Run, pos, button = gs.clear(screenData, pos, button, Mode)
        sound.play()



    return Mode, Run, pos, button
