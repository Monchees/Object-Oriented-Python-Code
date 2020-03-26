# pygame demo 4(b), One image, bounce around the window using rects

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sounds,  etc.
ballImage = pygame.image.load('images/ball.png')

# 5 - Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
 
# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()
    
    # 8 - Do any "per frame" actions
    if (ballRect.left < 0) or (ballRect.right > WINDOW_WIDTH):
        xSpeed = -xSpeed  # reverse X direction

    if (ballRect.top < 0) or (ballRect.bottom > WINDOW_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction

    # update the rectangle of the ball, based on the speed in two directions
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    # 9 - Clear the screen before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the screen elements
    window.blit(ballImage, ballRect)

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount


