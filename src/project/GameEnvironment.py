
import random
import sys
from pathlib import Path

from pygame import Surface
import pygame
from lab11.agent_environment import State
from lab11.pygame_ai_player import PyGameAIPlayer
from lab11.pygame_combat import run_pygame_combat
from lab11.sprite import Sprite
from lab11.turn_combat import CombatPlayer
from GameManager import GameManager
from project.chatGpt import generateMeJournalStory

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

sprite_path = "assets/lego.png"

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
        
        self.events = {
            "start": self.gameManager.cityNames[self.state.current_city],
            "end": self.gameManager.cityNames[self.endCity],
            "journey": []
        }

    def startGame(self, player: PyGameAIPlayer):
        self.gameManager.gameOver = False

        reset = True
        
        journey = {}
        
        while True:
            action = player.selectAction(self.state)
            
            if reset:
                journey = {
                    "From":  self.gameManager.cityNames[self.state.current_city],
                    "To": self.gameManager.cityNames[self.state.destination_city],
                    "Event": []
                }
                reset = False
          
            if(self.gameManager.routeIteration >= 10):
                action = self.gameManager.hasRoute(self.state.current_city, self.state.destination_city)
                
            if 0 <= action != self.state.current_city and not self.state.travelling:
                start = self.gameManager.cities[self.state.current_city]
              
                self.state.destination_city = action
                
                destination = self.gameManager.cities[self.state.destination_city]
                
                
                self.player_sprite.set_location(
                    self.gameManager.cities[self.state.current_city])
                self.state.travelling = True
                journey["From"] = self.gameManager.cityNames[self.state.current_city]
                print(
                    "Travelling from", self.state.current_city, "to", self.state.destination_city
                )

            if not self.gameManager.hasRoute(self.state.current_city, self.state.destination_city):
                self.state.travelling = False
                continue
            
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.landscapeSurface, (0, 0))
            self.window.drawCityAndLinks()

            if  self.state.travelling:
                self.state.travelling = self.player_sprite.move_sprite(
                    destination, self.spirtSpeed)
                self.state.encounter_event = random.randint(0, 1000) < 2
                if not self.state.travelling:
                    journey["To"] = self.gameManager.cityNames[self.state.destination_city]
                    print("Arrived at", self.state.destination_city)
                    
            if not self.state.travelling:
                encounter_event = False
                self.state.current_city = self.state.destination_city
                self.events["journey"].append(journey)
                reset = True
                

            if self.state.encounter_event:
                # TODO: RUN THE RUN_PYGAME_COMBAT
                (Phealth, Ohealth, reward) = run_pygame_combat(self.combateSurface, self.screen, self.player_sprite)
                won = True
                if Phealth > 0:
                   won = True
                   self.gameManager.money += 10
                else:
                    won = False
                    self.gameManager.money -= 10


                if self.gameManager.money <= 0:
                    journey["Event"].append ({
                        "type": "No Money Left",
                        "won": False,
                        "gained": -100
                    })
                    self.events["journey"].append(journey)
                    self.gameManager.gameOver = True


                self.state.encounter_event = False
                                
            else:
                self.player_sprite.draw_sprite(self.screen)

            pygame.display.update()
            if self.state.current_city == self.endCity or self.gameManager.gameOver:
                print("You have reached the end of the game!")
                self.gameManager.gameOver = True
                self.gameManager.jounralStory = "asdsa asd asd asd asdas Hello World"
                # self.gameManager.jounralStory = generateMeJournalStory(self.events)
                break
