import sys
from pathlib import Path



from window import Window
import pygame

from GameManager import GameManager

gameManager = GameManager((800, 650))
gameWindow = Window((800, 800), gameManager)


def startPyGameLoop():
    while gameWindow.isRunning:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameWindow.isRunning = False

            gameWindow.process()


if __name__ == "__main__":
    startPyGameLoop()
