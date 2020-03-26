#
# This the Scene A
#

import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *

class SceneA(pyghelpers.Scene):
    def __init__(self, window, sceneKey):
        # Save window and sceneKey in instance variables
        self.window = window
        self.sceneKey = sceneKey

        self.messageField = pygwidgets.DisplayText(self.window, (15, 25), 'This is Scene A', \
                                              fontSize=50, textColor=WHITE, width=610, justified='center')

        self.gotoBButton = pygwidgets.TextButton(self.window, (250, 100), 'Go to Scene B')
        self.gotoCButton = pygwidgets.TextButton(self.window, (400, 100), 'Go to Scene C')

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.gotoBButton.handleEvent(event):
                self.goToScene(SCENE_B)
            if self.gotoCButton.handleEvent(event):
                self.goToScene(SCENE_C)

            # Testing:  Press b or c to send message to those scenes
            #           Press or 2 or 3 to get data from B and C
            #           Press x to send message to all scenes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    self.send(SCENE_B, 'message', 'Sending message to Scene B')

                if event.key == pygame.K_c:
                    self.send(SCENE_C, 'message', 'Sending message to Scene C')

                if event.key == pygame.K_2:
                    answer = self.request(SCENE_B, 'get data')
                    print('Recevied data from Scene B')
                    print('Answer was:', answer)

                if event.key == pygame.K_3:
                    answer = self.request(SCENE_C, 'get data')
                    print('Recevied data from Scene C')
                    print('Answer was:', answer)

                if event.key == pygame.K_x:
                    self.sendAll('all message', 'Sending message to All scenes')

    def draw(self):
        self.window.fill(GRAYA)
        self.messageField.draw()
        self.gotoBButton.draw()
        self.gotoCButton.draw()

    def receive(self, msgType, data):
        print('In A')
        print('Received a message of type:', msgType)
        print('The data received was:', data)

    def respond(self, msgType):
        if msgType == 'get data':
            return 'Here is data from scene A'

