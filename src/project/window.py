import sys

import pygame
pygame.init()
pygame.font.init()

from pathlib import Path
from button import Button


sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))
from lab11.agent_environment import get_landscape_surface, get_combat_surface



(width, height) = (300,200)
background_color = (255,255,255)

windowObjects = [];


def startGameFunction():
    print("START GAME")


class Window:
    def __init__(self, dim:tuple):
        print("HERE")
        self.isRunning = True
        self.screen = pygame.display.set_mode(dim)
        pygame.display.set_caption('Game 450 Project')
        self.screen.fill(background_color)
        
        self.generateLandScape()
        self.generateCombatSurface()
        
        startButton = Button(30, 30, 400, 100, 'Button One (onePress)', startGameFunction)
        
        windowObjects.append(startButton)
        
    def generateLandScape(self):
        size = (640,640);
        self.game_surface = get_landscape_surface(size)
        
    def generateCombatSurface(self):
        size = (640,640);
        self.combat_surface = get_combat_surface(size)
 
    
    def process(self):
        for object in windowObjects:
            object.process(self.screen)
        
        self.screen.blit(self.game_surface, (0, 0))
        pygame.display.update()
        