import pygame, textWrap
from pygame.locals import *

# set up display refresh event
fps = 60
DISPLAY_REFRESH = USEREVENT
pygame.time.set_timer(DISPLAY_REFRESH, int(1000.0/fps))

# set some basic color constants
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)
ALPHA =(  0,   0,   0,   0)

# init all modules with defualt settings
pygame.init()

def main():
    # get a pygame.surface for the window
    DISPLAYSURF = pygame.display.set_mode((400,120))
    # set the window title
    pygame.display.set_caption("DI-SkitBoard")
    mainLoop(DISPLAYSURF)



def mainLoop(surface):
    running = True
    #display some instructions
    fontObj = pygame.font.Font('C:\Windows\Fonts\lucon.TTF', 12) # this causes a windows dependence!!!
    textRect = pygame.Rect(0, 0, 400, 120)
    textSurface = surface.convert_alpha()
    textSurface.fill(ALPHA)
    textWrap.drawText(textSurface, 'This is the soundboard for the 2013 Twist-o-Rama entry, The Wedding Cake.\n \nSPACE = Door Sound', BLACK, textRect, fontObj, True)
    while running: # main program loop
        event = pygame.event.wait()
        if event.type == QUIT: #handle the QUIT event
            pygame.quit()
            running = False
        elif event.type == DISPLAY_REFRESH:
            surface.fill(WHITE)
            surface.blit(textSurface, textRect) 
            pygame.display.update()
        
if __name__ == '__main__':
    main()