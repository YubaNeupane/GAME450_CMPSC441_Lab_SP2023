from lab7.ga_cities import game_fitness, setup_GA, solution_to_cities
from lab2.cities_n_routes import get_randomly_spread_cities, get_routes

import sys
import os
from pathlib import Path
import random
import numpy as np


sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))


class GameManager:
    def __init__(self, size):
        self.citites = []
        self.cityNames = []
        self.routes = []
        self.city_locations_dict = None
        self.n_cities = 10
        self.size = size

    # TODO: FIX THIS SHIT!
    def generateCityNames(self, numberOfCities):
        print("Generating city names...")
        self.cityNames = [
            "Morkomasto",
            "Morathrad",
            "Eregailin",
            "Corathrad",
            "Eregarta",
            "Numensari",
            "Rhunkadi",
            "Londathrad",
            "Baernlad",
            "Forthyr",
        ]

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
