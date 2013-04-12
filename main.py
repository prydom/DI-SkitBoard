import pygame, sys
from pygame.locals import *

# init all modules with defualt settings
pygame.init()

# get a pygame.surface for the window
DISPLAYSURF = pygame.display.set_mode((400,300))

# set the window title
pygame.display.set_caption("DI-SkitBoard")

while True: # main program loop
	for event in pygame.event.get():
		if event.type == QUIT: #handle the QUIT event
			pygame.quit()
			sys.exit()
		pygame.display.update()
		