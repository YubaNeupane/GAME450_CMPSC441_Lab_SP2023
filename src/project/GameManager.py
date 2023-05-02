from lab7.ga_cities import game_fitness, setup_GA, solution_to_cities
from lab2.cities_n_routes import get_randomly_spread_cities, get_routes

import sys
import os
from pathlib import Path
import random
import numpy as np



sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from project.chatGpt import generateCityNames

class GameManager:
    def __init__(self, size):
        self.citites = []
        self.cityNames = []
        self.routes = []
        self.city_locations_dict = None
        self.n_cities = 10
        self.size = size
        self.routeIteration = 0;
        self.gameOver = False
        self.jounralStory = ""
        self.money = 100.0

    # TODO: FIX THIS SHIT!
    def generateCityNames(self, numberOfCities):
        print("Generating city names...")
        self.cityNames = generateCityNames(self.n_cities)
        # self.cityNames = [
        #     "Morkomasto",
        #     "Morathrad",
        #     "Eregailin",
        #     "Corathrad",
        #     "Eregarta",
        #     "Numensari",
        #     "Rhunkadi",
        #     "Londathrad",
        #     "Baernlad",
        #     "Forthyr",
        # ]
        

    def generateCities(self):
        if os.path.exists("landscapeElevation.npy"):
            with open("landscapeElevation.npy", "rb") as f:
                self.elevation = np.load(f)
        else:
            return np.array(get_randomly_spread_cities(self.size, self.n_cities))

        self.elevation = np.array(self.elevation)
        self.elevation = (self.elevation - self.elevation.min()) / \
            (self.elevation.max() - self.elevation.min())

        def fitness(cities, idx): return game_fitness(
            cities, idx, elevation=self.elevation, size=self.size
        )
        _, ga_instance = setup_GA(fitness, self.n_cities, self.size)
        ga_instance.run()
        cities = ga_instance.best_solution()[0]
        cities = solution_to_cities(cities, self.size)
        return cities
    
    def getElevation(self, x, y):
        return self.elevation[x][y]

    def hasRoute(self, start, end):
        startloc = self.city_locations_dict[self.cityNames[start]]
        endloc = self.city_locations_dict[self.cityNames[end]]
        
        
        if(self.routeIteration >= 10):
            for link in self.routes:
                if(link[0][0] == startloc[0] and link[0][1] == startloc[1]):
                    endloc = link[1]
                    break
                if(link[1][0] == startloc[0] and link[1][1] == startloc[1]):
                    endloc = link[0]
                    break

            i = 0
            
            for name in self.cityNames:
                if self.city_locations_dict[name][0] == endloc[0] and self.city_locations_dict[name][1] == endloc[1]:
                    self.routeIteration = 0
                    return i
                i += 1
        
        for link in self.routes:
            if(link[0][0] == startloc[0] and link[0][1] == startloc[1]):
                if(link[1][0] == endloc[0] and link[1][1] == endloc[1]):
                    self.routeIteration = 0;
                    return True
            
            if(link[1][0] == startloc[0] and link[1][1] == startloc[1]):
                if(link[0][0] == endloc[0] and link[0][1] == endloc[1]):
                    self.routeIteration = 0;
                    return True
               
        
        self.routeIteration +=1
        return False

    def generateCityLinks(self, mapsize: tuple):
        print("Generating city links...")
        self.cities = self.generateCities()

        self.routes = get_routes(self.cities)
        random.shuffle(self.routes)
        self.routes = self.routes[:10]

        self.city_locations_dict = {
            name: location for name, location in zip(self.cityNames, self.cities)}

    def generateStory(self):
        print("Generating story...")
