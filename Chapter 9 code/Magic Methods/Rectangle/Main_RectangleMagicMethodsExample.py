import pygame
import sys
from pygame.locals import *
from Rectangle import *


# set up the constants
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_RECTANGLES = 10
FIRST_RECTANGLE = 'first'
SECOND_RECTANGLE = 'second'

# set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

rectanglesList = []
for i in range(0, N_RECTANGLES):
    oRectangle = Rectangle(window)
    rectanglesList.append(oRectangle)

state = FIRST_RECTANGLE
print(oRectangle)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for oRectangle in rectanglesList:
                if oRectangle.clickedInside(event.pos):
                    print('Clicked on', state, 'rectangle.')

                    if state == FIRST_RECTANGLE:
                        oFirstRectangle = oRectangle
                        state = SECOND_RECTANGLE

                    elif state == SECOND_RECTANGLE:
                        if oFirstRectangle == oRectangle:
                            print('Rectangles are the same size.')
                        else:
                            if oFirstRectangle < oRectangle:
                                print('First rectangle is smaller than second rectangle.')
                            else:
                                print('First rectangle is larger than second rectangle.')
                        state = FIRST_RECTANGLE

    # Clear the screen, and draw all rectangles
    window.fill(WHITE)
    for oRectangle in rectanglesList:
        oRectangle.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
