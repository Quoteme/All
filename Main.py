#!/usr/bin/python
import pygame as pygame
import random as random
import GeneralStructures as gs
import ButtonGame as BG
import Soundmodul as Sm
import Mandelbrot as Mb
import PingPong as PP


#Fenster erstellen
pygame.init()
screen_width = 1400
screen_height = 800
usescreen_height = 780
screen = pygame.display.set_mode([screen_width,screen_height])
Clock = pygame.time.Clock()
screenData = (screen, screen_width, screen_height, Clock)
Mode = 'Menu'
pygame.display.set_caption(Mode)

#Erstelle das Menu
def Menu(pos, button, Mode):
    if Mode == 'Menu':
        #ButtongameButton
        ButtonGameStartImg = pygame.image.load('Bilder/ButtonGameStarteButton.png')
        Mode = gs.CustemButtonImage(screenData, pos, button, (80, 100), 'ButtonGameMenu', Mode, ButtonGameStartImg)
        #SoundmodulButton
        SoundmodulStartImg = pygame.image.load('Bilder/SoundmodulStarteButton.png')
        Mode = gs.CustemButtonImage(screenData, pos, button, (240, 100), 'Soundmodul', Mode, SoundmodulStartImg)
        #SoundmodulButton
        PingPongStartImg = pygame.image.load('Bilder/PingPongStarteButton.png')
        Mode = gs.CustemButtonImage(screenData, pos, button, (400, 100), 'PingPong', Mode, PingPongStartImg)
        #MandelbrotButton
        MandelbrotStartImg = pygame.image.load('Bilder/MandelbrotStartButton.png')
        Mode = gs.CustemButtonImage(screenData, pos, button, (560, 100), 'Mandelbrot', Mode, MandelbrotStartImg)
    return Mode

#Mausbewegungen vordefinieren
pos = (-1, -1)
button = 0
Clock = pygame.time.Clock()

#Start der Hauptschleife
Run = True
while Run:
    Mode, Run, pos, button = gs.clear(screenData, pos, button, Mode)
    #Menu
    Mode = Menu(pos, button, Mode)
    #Starte das ButtonGameMenu
    Mode, Run, pos, button = BG.ButtonGame(screenData, pos, button, Mode, Run)
    #Starte das Soundmodul
    Mode, Run, pos, button = Sm.Soundmodul(screenData, pos, button, Mode, Run)
    #Sarte Mandelbrot
    Mode, Run, pos, button = Mb.Mandelbrot(screenData, pos, button, Mode, Run)
    #Starte PingPong
    Mode, Run, pos, button = PP.PingPong(screenData, pos, button, Mode, Run)
