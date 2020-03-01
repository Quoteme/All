#!/usr/bin/python
import pygame as pygame
import random as random
import GeneralStructures as gs


def ButtonGame(screenData, pos, button,  Mode, Run):
    screen ,screen_width, screen_height, Clock= screenData

    if Mode == 'ButtonGameMenu':
        ButtonGameZeitLeaderboard = gs.Leaderboard('./RangListe')
        #verhindere automatisches doppeltes Klicken
        while button == 1:
            Mode, Run, pos, button = gs.clear(screenData, pos, button, Mode)

        while Mode == 'ButtonGameMenu':
            Mode, Run, pos, button = gs.clear(screenData, pos, button, Mode)
            #Starte das ButtonGame
            ButtonGameStartImg = pygame.image.load('Bilder/ButtonGameStarteButton.png')
            Mode = gs.CustemButtonImage(screenData, pos, button, (80, 100), 'ButtonGame', Mode, ButtonGameStartImg)
            #Satre das ButtenGame auf Zeit
            ButtonGameZeitStartImg = pygame.image.load('Bilder/ButtonGameZeitStarteButton.png')
            Mode = gs.CustemButtonImage(screenData, pos, button, (240, 100), 'ButtonGameZeit', Mode, ButtonGameZeitStartImg)
            #Zeige das Leaderboard
            ButtonGameZeitLeaderboard.show(screenData, (screen_width*3/4, screen_height/10), pygame.font.SysFont('dejavuserif', 30))


        if Mode == 'ButtonGameZeit':
            x, y, i = screen_width/2, (screen_height-20)/2-10, 0

            Los = False
            while not Los:
                Mode, Run, pos, button = gs.clear(screenData, pos, button, Mode)
                StartButton = pygame.image.load('Bilder/StartButton100x200.png')
                Los = gs.CustemButtonImage(screenData, pos, button, ((screen_width/2)-100, (screen_height/2)-50), True, False, StartButton)

            if Mode == 'ButtonGameZeit':
                Zeitvorher = pygame.time.get_ticks()
                while (i<5):
                    Mode, Run, pos, button = gs.clear(screenData, pos, button, Mode)
                    newx = random.randint(0, screen_width-40)
                    newy = random.randint(20, screen_height-40)
                    ButtonGameZeitImg = pygame.image.load('Bilder/ButtonGameZeitButton.png')
                    x, y, i = gs.CustemButtonImage(screenData, pos, button, (x,y), (newx,newy,i+1), (x,y,i), ButtonGameZeitImg)

                Zeitnachher = pygame.time.get_ticks()
                Zeit = str((Zeitnachher-Zeitvorher)/1000)
                font_dejavuserif = pygame.font.SysFont('dejavuserif', 30)
                textsurfaceZeit = font_dejavuserif.render(Zeit, False, (255, 255, 255))
                text = ''
                NamenEingegeben = True
                while NamenEingegeben:
                    Mode, Run, pos, button = gs.clear(screenData, pos, button, Mode)
                    screen.blit(textsurfaceZeit,((screen_width/2)-font_dejavuserif.size(Zeit)[0],(screen_height/2)-100))
                    Mode, Run, pos, button, text = gs.textinputbutton(screenData, pos, button, Mode, Run, 'ButtonGameZeit', ((screen_width/2)-100, (screen_height/2)-50 ,200 , 50), font_dejavuserif, text)
                    NamenEingegeben = gs.CustemButtonColor(screenData, pos, button, ((screen_width/2)+110, (screen_height/2)-50 ,50 , 50), False, True, gs.green)

                ButtonGameZeitLeaderboard.update([text, Zeit])

                #Gehe zurück ins Menu
                Mode = 'ButtonGameMenu'


        if Mode == 'ButtonGame':
            ButtonAnzahl = 50
            Buttonx = [(screen_width/2)-20 for i in range(ButtonAnzahl)]
            Buttony = [(screen_height-20)/2-20 for i in range(ButtonAnzahl)]
            Buttongr = [40 for i in range(ButtonAnzahl)]
            ButtonColor = [pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range(ButtonAnzahl)]

            while Mode == 'ButtonGame':
                Mode, Run, pos, button = gs.clear(screenData, pos, button, Mode)

                for i in range(ButtonAnzahl):
                    newgr = random.randint(20,40)
                    newx = random.randint(0, screen_width-newgr)
                    newy = random.randint(20, screen_height-newgr)
                    Buttonx[i], Buttony[i], Buttongr[i] = gs.CustemButtonColor(screenData, pos, button, (Buttonx[i], Buttony[i], Buttongr[i], Buttongr[i]), (newx, newy, newgr), (Buttonx[i], Buttony[i], Buttongr[i]), ButtonColor[i])


    return Mode, Run, pos, button
