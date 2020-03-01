#!/usr/bin/python
import pygame as pygame

black = pygame.Color(0, 0, 0, 255)
white = pygame.Color(255, 255, 255, 255)
light_gray = pygame.Color(200, 200, 200, 255)
gray = pygame.Color(127, 127, 127, 255)
dark_gray = pygame.Color(55, 55, 55, 255)
red = pygame.Color(255, 0, 0, 255)
blue = pygame.Color(0, 0, 255, 255)
green = pygame.Color(0, 225, 0, 255)
yellow = pygame.Color(0, 255, 255, 255)

def clear(screenData, pos, button, mode, clock=True):
    screen ,screen_width, screen_height, Clock= screenData
    if clock:
        Clock.tick(60)
    else:
        Clock.tick()
    #print(mode)
    pygame.display.update()
    pygame.draw.rect(screen, black, pygame.Rect(0, 0, screen_width, screen_height))
    pos, button = getMouseMotion(pos, button)
    mode, exit = OberLeiste(screenData, pos, button, mode)
    return mode, exit, pos, button



def CustemButtonColor(screenData, pos, button, Buttondim, ClickReturn, DefaultReturn, Color):
    #Buttondim muss von der Form (left, top, width, height) sein
    screen ,screen_width, screen_height, Clock = screenData
    pygame.draw.rect(screen , Color , pygame.Rect(*Buttondim))
    if ((Buttondim[0] < pos[0] < Buttondim[0]+Buttondim[2]) and (Buttondim[1] < pos[1] < Buttondim[1]+Buttondim[3]) and (button == 1)):
        return ClickReturn
    else:
        return DefaultReturn

def CustemButtonImage(screenData, pos, button, Buttonpos, ClickReturn, DefaultReturn, Image):
    #Buttonpos muss von der Form (left, top) sein
    screen ,screen_width, screen_height, Clock = screenData
    screen.blit(Image, (Buttonpos[0],Buttonpos[1]))
    Imgwidth = Image.get_width()
    Imgheight = Image.get_height()
    if ((Buttonpos[0] < pos[0] < Buttonpos[0]+Imgwidth) and (Buttonpos[1] < pos[1] < Buttonpos[1]+Imgheight) and (button == 1)):
        return ClickReturn
    else:
        return DefaultReturn

def OberLeiste(screenData, pos, button, mode):
    screen ,screen_width, screen_height, Clock= screenData
    pygame.draw.rect(screen , dark_gray , pygame.Rect(0, 0, screen_width, 20))
    #Zurückbutton
    ZurückImg = pygame.image.load('Bilder/ZurückButton.png')
    mode = CustemButtonImage(screenData, pos, button, (0, 0), 'Menu', mode,ZurückImg)
    #Exitbutton
    exitImg = pygame.image.load('Bilder/ExitButton.png')
    exit = CustemButtonImage(screenData, pos, button, (screen_width-40, 0), False, True, exitImg)
    mode = CustemButtonImage(screenData, pos, button, (screen_width-40, 0), 'Menu', mode, exitImg)
    #gib die Position an
    font_dejavuserif = pygame.font.SysFont('dejavuserif', 18)
    textsurface = font_dejavuserif.render(str((pos,button)), False, (255, 255, 255))
    screen.blit(textsurface,(41,1))
    #gib Fps an
    textsurface = font_dejavuserif.render(str(round(Clock.get_fps())), False, (255, 255, 255))
    screen.blit(textsurface,(42+font_dejavuserif.size('((0000,000),00)')[0],1))

    return mode, exit

def getMouseMotion(pos, button):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            button = event.button
        if event.type == pygame.MOUSEBUTTONUP:
            button = 0
    return pos, button

def getKey(screenData, pos, button, mode):
    while True:
        pygame.display.update()
        mode, exit = OberLeiste(screenData, pos, button, mode)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
            if event.type == pygame.MOUSEBUTTONUP:
                button = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return pos, button, mode, exit, None
                return pos, button, mode, exit, event.unicode



def textinputbutton(screenData, pos, button, mode, exit, currentmode, Buttondim, Font, lastText):
    screen ,screen_width, screen_height, Clock= screenData
    text = ''
    Textinput = False
    Textinput = CustemButtonColor(screenData, pos, button, Buttondim, True, False, white)
    lastTextsurface = Font.render(lastText, False, (0,0,0))
    screen.blit(lastTextsurface,(Buttondim[0]+(Buttondim[2]/2)-(Font.size(lastText)[0]/2), Buttondim[1]+(Buttondim[3]/2)-(Font.size(lastText)[1]/2)))
    while Textinput:
        pos, button = getMouseMotion(pos, button)
        mode, exit = OberLeiste(screenData, pos, button, mode)
        pygame.display.update()

        pygame.draw.rect(screen, white, pygame.Rect(*Buttondim))
        textsurface = Font.render(text, False, (0,0,0))
        screen.blit(textsurface,(Buttondim[0]+(Buttondim[2]/2)-(Font.size(text)[0]/2), Buttondim[1]+(Buttondim[3]/2)-(Font.size(text)[1]/2)))

        pos, button, mode, exit, key = getKey(screenData, pos, button, mode)
        if key == None:
            break
        text = text + key
    if text == '':
        text = lastText
    return mode, exit, pos, button, text

class Leaderboard:
    def __init__(self, file):
        self.file = file

    def update(self, neu):
        RangListe = []
        #Lese die alten Einträge
        with open(self.file, mode='r') as RangListenFile:
            zeilen = RangListenFile.readlines()
        #Sortiere die alten Einträge mit dem neuen Eintrag
        for i in range(10):
            RangListe = RangListe + [[zeilen[2*i][:-1], float(zeilen[2*i+1])]]
        Eingefügt = False
        for i in range(10,0,-1):
            if (RangListe[i-1][1])<float(neu[1]):
                RangListe = RangListe[:i] + [neu] + RangListe[i:]
                Eingefügt = True
                break
        if not Eingefügt:
            RangListe = [neu] + RangListe
        #Schreibe die neuen Einträge
        with open(self.file,mode='w') as RangListenFile:
            for i in range(10):
                RangListenFile.write(str(RangListe[i][0]) + '\n')
                RangListenFile.write(str(RangListe[i][1]) + '\n')
        return self

    def show(self, screenData, pos, Font):
        screen ,screen_width, screen_height, Clock= screenData
        with open(self.file, mode='r') as RangListenFile:
            zeilen = RangListenFile.readlines()
        for i in range(10):
            platz = str(i+1) + '. ' + str(zeilen[2*i][:-1]) + '     ' + str(float(zeilen[2*i+1]))
            textsurfaceZeit = Font.render(platz, False, (255, 255, 255))
            screen.blit(textsurfaceZeit, (pos[0], pos[1]+i*Font.size(platz)[1]))
