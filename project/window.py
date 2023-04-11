import pygame
pygame.init()
pygame.font.init()

from button import Button

(width, height) = (300,200)
background_color = (255,255,255)

windowObjects = [];


def startGameFunction():
    print("START GAME")


class Window:
    def __init__(self, dim:tuple):
        self.isRunning = True
        self.screen = pygame.display.set_mode(dim)
        pygame.display.set_caption('Game 450 Project')
        self.screen.fill(background_color)
        
        startButton = Button(30, 30, 400, 100, 'Button One (onePress)', startGameFunction)
        
        windowObjects.append(startButton)
        
    
    def process(self):
        for object in windowObjects:
            object.process(self.screen)
        
        pygame.display.flip()
        