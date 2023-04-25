import sys

import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()
import threading

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
        self.isGenerating = False
        self.game_surface = None
        self.isRunning = True
        self.dim = dim
        self.screen = pygame.display.set_mode(dim, flags=DOUBLEBUF)
        self.screen.set_alpha(None)

        pygame.display.set_caption('Game 450 Project')
        self.screen.fill(background_color)


        print("Generating Landscape Surface...")
        # self.generateLandScape()
        self.generateTerrainThread = threading.Thread(target=self.generateLandScape, args=())
        self.generateTerrainThread.start()
        
        print("Generating Combat Surface...")
        self.generateCombatSurface()
        
        self.generateCityAndLinks()
        self.makeButtons()

        
    def regenereateButtonPress(self):
        if(self.generateTerrainThread == None):
            print("Regenereating Terrain")
            self.generateTerrainThread = threading.Thread(target=self.generateLandScape, args=([True]))
            self.generateTerrainThread.start()
            
    def makeButtons(self):
        startButton = Button(30, 670, 90, 50, 'Start', self.startGameFunction)
        quitGameButton = Button(140, 670, 90, 50, 'Quit', self.quitGameFunction)
        
        generateSurfaceButton = Button(30, 730, 200, 50, 'Regenerate Surface', self.regenereateButtonPress)
        
        windowObjects.append(startButton)
        windowObjects.append(generateSurfaceButton)
        windowObjects.append(quitGameButton)
        
    def quitGameFunction(self):
        pygame.quit()
        
    def startGameFunction(self):
        print("START GAME")
        
    def generateLandScape(self, new=False):
        size = (self.dim[0],650);
        self.game_surface = get_landscape_surface(size, new)
        self.generateCityAndLinks()
        
    def generateCombatSurface(self):
        size = (self.dim[0],650);
        self.combat_surface = get_combat_surface(size)
        
    def generateCityAndLinks(self):
        print("Generating cities and links...")
        self.gameManager.generateCityNames(10)
        self.gameManager.generateCityLinks((self.dim[0],650))
            
    def drawCityAndLinks(self):
        colorCity = (255,255,255)
        colorLine = (0,0,255)
        my_font = pygame.font.SysFont('Comic Sans MS', 20)
    
        for route in self.gameManager.routes:
            pygame.draw.line(self.game_surface,colorLine,route[0], route[1], 2)


        for name in self.gameManager.cityNames:
            x = self.gameManager.city_locations_dict.get(name)[0]
            y = self.gameManager.city_locations_dict.get(name)[1]
            pygame.draw.rect(self.game_surface, colorCity, pygame.Rect(x,y, 10, 10))
            text_surface = my_font.render(name, False, (0, 0, 0))
            self.screen.blit(text_surface, (x+20,y))
        
        
    def showGeneratingText(self):
        if self.isGenerating:
            my_font = pygame.font.SysFont('Comic Sans MS', 90)
            text_surface = my_font.render('Generating...', False, (0, 0, 0))
            self.screen.blit(text_surface, (30,self.dim[1]/2))

    #RUN THE GAME EVERY FRAME
    def process(self):
        for object in windowObjects:
            object.process(self.screen)

        if(self.generateTerrainThread != None):
            if self.generateTerrainThread.is_alive():
                self.isGenerating = True
            else:
                self.generateTerrainThread = None
                self.isGenerating = False

        if self.game_surface != None and not self.isGenerating:
            self.screen.blit(self.game_surface, (0, 0))
            self.drawCityAndLinks()

        self.showGeneratingText()
        pygame.display.flip()
