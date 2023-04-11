import sys

import pygame
pygame.init()
pygame.font.init()

from pathlib import Path
from button import Button


sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))
from lab11.agent_environment import get_landscape_surface, get_combat_surface
from project.GameManager import GameManager

(width, height) = (300,200)
background_color = (0,0,0)

windowObjects = [];


class Window:
    def __init__(self, dim:tuple, gameManager: GameManager):
        self.gameManager = gameManager
        self.isRunning = True
        self.dim = dim
        self.screen = pygame.display.set_mode(dim)
        pygame.display.set_caption('Game 450 Project')
        self.screen.fill(background_color)
        
        print("Generating Landscape Surface...")
        self.generateLandScape()
        
        print("Generating Combat Surface...")
        self.generateCombatSurface()
        
        self.generateCityAndLinks()
        
        self.makeButtons()
 
        
    def makeButtons(self):
        startButton = Button(30, 670, 90, 50, 'Start', self.startGameFunction)
        quitGameButton = Button(140, 670, 90, 50, 'Quit', self.quitGameFunction)
        
        generateSurfaceButton = Button(30, 730, 200, 50, 'Regenerate Surface', self.generateLandScape)
        
        
        windowObjects.append(startButton)
        windowObjects.append(generateSurfaceButton)
        windowObjects.append(quitGameButton)
        
    def quitGameFunction(self):
        pygame.quit()
        
    def startGameFunction(self):
        print("START GAME")
        
    def generateLandScape(self):
        size = (self.dim[0],650);
        self.game_surface = get_landscape_surface(size)
        
    def generateCombatSurface(self):
        size = (self.dim[0],650);
        self.combat_surface = get_combat_surface(size)
        
    def generateCityAndLinks(self):
        print("Generating cities and links...")
        self.gameManager.generateCityNames(10)
        self.gameManager.generateCityLinks((self.dim[0],650))
            
    def drawCityAndLinks(self):
        print("Drawing cities and links...")
        
    
    
    #RUN THE GAME EVERY FRAME
    def process(self):
        for object in windowObjects:
            object.process(self.screen)
        
        self.screen.blit(self.game_surface, (0, 0))
        # self.drawCityAndLinks()
        
        pygame.display.update()
        