import sys
from pathlib import Path

# line taken from turn_combat.py
sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from window import Window
import pygame

gameWindow = Window((800,800))

def startPyGameLoop():
    while gameWindow.isRunning:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameWindow.isRunning = False
            
            gameWindow.process()


if __name__ == "__main__":
    startPyGameLoop()
    