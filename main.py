import pygame, sys
from pygame.locals import *

# set some basic color constants
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

# init all modules with defualt settings
pygame.init()

# get a pygame.surface for the window
DISPLAYSURF = pygame.display.set_mode((400,300))

# set the window title
pygame.display.set_caption("DI-SkitBoard")

#display some instructions
fontObj = pygame.font.Font('C:\Windows\Fonts\lucon.TTF', 12) # this causes a windows dependence!!!
textInstuctionsSurface = fontObj.render('This is a test', True, BLACK)
textRectObj = textInstuctionsSurface.get_rect()
textRectObj.center = (200,150)

while True: # main program loop
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(textInstuctionsSurface, textRectObj)
	for event in pygame.event.get():
		if event.type == QUIT: #handle the QUIT event
			pygame.quit()
			sys.exit()
		pygame.display.update()
		