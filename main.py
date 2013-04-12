import pygame, sys, textWrap
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

# init all modules with defualt settings
pygame.init()

def main():
	# get a pygame.surface for the window
	DISPLAYSURF = pygame.display.set_mode((400,300))
	# set the window title
	pygame.display.set_caption("DI-SkitBoard")
	mainLoop(DISPLAYSURF)



def mainLoop(surface):
	running = True
	#display some instructions
	fontObj = pygame.font.Font('C:\Windows\Fonts\lucon.TTF', 12) # this causes a windows dependence!!!
	textRect = pygame.Rect(0, 0, 400, 36)
	while running: # main program loop
		for event in pygame.event.get():
			if event.type == QUIT: #handle the QUIT event
				pygame.quit()
				sys.exit()
			if event.type == DISPLAY_REFRESH:
				surface.fill(WHITE)
				textWrap.drawText(surface, 'This is the soundboard for the 2013 Twist-o-Rama entry, The Wedding Cake.', BLACK, textRect, fontObj, True)
				pygame.display.update()
			pygame.time.wait(0)
		
if __name__ == '__main__':
    main()