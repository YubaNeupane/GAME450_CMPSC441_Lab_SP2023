import sys
from pathlib import Path
import random

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))
from lab2.cities_n_routes import get_randomly_spread_cities, get_routes

class GameManager:
    def __init__(self):
         self.citites = [];
         self.cityNames = []
         self.routes = []
         self.city_locations_dict = None
         
    #TODO: FIX THIS SHIT!
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
    
    def generateCityLinks(self, mapsize:tuple):
        print("Generating city links...")
        self.cities = get_randomly_spread_cities(mapsize, len(self.cityNames))
        self.routes = get_routes(self.cities)
        random.shuffle(self.routes)
        self.routes = self.routes[:10]
        
        self.city_locations_dict = {name: location for name, location in zip(self.cityNames, self.cities)}
    
        
    def generateStory(self):
        print("Generating story...")