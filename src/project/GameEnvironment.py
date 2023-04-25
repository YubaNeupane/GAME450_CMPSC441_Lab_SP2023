
import sys
from pathlib import Path
from lab11.agent_environment import State
from lab11.turn_combat import CombatPlayer

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

#TODO: THIS FUCKING SHIT
class GameEnvironment:
    def __init__(self, state:State):
        self.state = state
    

    def startGame(self, player:CombatPlayer):
        while True:
            action = player.selectAction()

            
