
import random
import sys
from pathlib import Path

from pygame import Surface
import pygame
from lab11.agent_environment import State
from lab11.pygame_ai_player import PyGameAIPlayer
from lab11.sprite import Sprite
from lab11.turn_combat import CombatPlayer
from GameManager import GameManager

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

sprite_path = "assets/lego.png"
# TODO: THIS FUCKING SHIT


class GameEnvironment:
    def __init__(self, state: State, gameManager: GameManager, screen: Surface, landscapeSurface: Surface, combateSurface: Surface, window):
        self.state = state
        self.gameManager = gameManager
        self.player_sprite = Sprite(sprite_path, self.gameManager.cities[0])
        self.screen = screen
        self.landscapeSurface = landscapeSurface
        self.combateSurface = combateSurface
        self.window = window
        self.endCity = 9
        self.spirtSpeed = 1

    def startGame(self, player: PyGameAIPlayer):
        while True:
            action = player.selectAction(self.state)
            if 0 <= action != self.state.current_city and not self.state.travelling:
                start = self.gameManager.cities[self.state.current_city]
                self.state.destination_city = action
                destination = self.gameManager.cities[self.state.destination_city]
                self.player_sprite.set_location(
                    self.gameManager.cities[self.state.current_city])
                self.state.travelling = True
                print(
                    "Travelling from", self.state.current_city, "to", self.state.destination_city
                )

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.landscapeSurface, (0, 0))
            self.window.drawCityAndLinks()

            if  self.state.travelling:
                self.state.travelling = self.player_sprite.move_sprite(
                    destination, self.spirtSpeed)
                self.state.encounter_event = random.randint(0, 1000) < 2
                if not self.state.travelling:
                    print("Arrived at", self.state.destination_city)

            if not self.state.travelling:
                encounter_event = False
                self.state.current_city = self.state.destination_city

            if self.state.encounter_event:
                # TODO: RUN THE RUN_PYGAME_COMBAT
                self.state.encounter_event = False
            else:
                self.player_sprite.draw_sprite(self.screen)

            pygame.display.update()
            if self.state.current_city == self.endCity:
                print("You have reached the end of the game!")
                break
