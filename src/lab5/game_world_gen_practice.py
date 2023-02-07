'''
Lab 5: PCG and Project Lab

This a combined procedural content generation and project lab. 
You will be creating the static components of the game that will be used in the project.
Use the landscape.py file to generate a landscape for the game using perlin noise.
Use the lab 2 cities_n_routes.py file to generate cities and routes for the game.
Draw the landscape, cities and routes on the screen using pygame.draw functions.
Look for triple quotes for instructions on what to do where.
The intention of this lab is to get you familiar with the pygame.draw functions, 
use perlin noise to generate a landscape and more importantly,
build a mindset of writing modular code.
This is the first time you will be creating code that you may use later in the project.
So, please try to write good modular code that you can reuse later.
You can always write non-modular code for the first time and then refactor it later.
'''
from landscape import get_landscape
import numpy as np
import random
import pygame
import sys

from pathlib import Path
sys.path.append(str((Path(__file__)/'..'/'..').resolve().absolute()))

from lab2.cities_n_routes import get_randomly_spread_cities, get_routes

# TODO: Demo blittable surface helper function

''' Create helper functions here '''
def generate_surface(size):
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface

def drawCities(city_locations_dict, city_names, displayNames = False):
    color = (255,255,255)
    for name in city_names:
        pygame.draw.rect(pygame_surface, color, pygame.Rect(city_locations_dict.get(name)[0], city_locations_dict.get(name)[1], 10, 10))
    
    if(displayNames): displayCityNames(city_locations_dict, city_names)
    
def drawCitiesRoutes(city_locations_dict, routes):
    Color_line = (0,0,0)
    for (startCityName, endCityName) in routes:
        startCord= (city_locations_dict.get(startCityName)[0], city_locations_dict.get(startCityName)[1])
        endCord = (city_locations_dict.get(endCityName)[0], city_locations_dict.get(endCityName)[1])
        pygame.draw.line(pygame_surface, Color_line, startCord,endCord,3)

def displayCityNames(city_locations_dict, city_names):
    for name in city_names:
        text_surface = my_font.render(name, True, (0, 0, 150))
        screen.blit(text_surface, (city_locations_dict.get(name)[0],city_locations_dict.get(name)[1]))
        
    

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 15)

    size = width, height = 640, 480
    black = 1, 1, 1

    screen = pygame.display.set_mode(size)
    pygame_surface = generate_surface(size)

    city_names = ['Morkomasto', 'Morathrad', 'Eregailin', 'Corathrad', 'Eregarta',
                  'Numensari', 'Rhunkadi', 'Londathrad', 'Baernlad', 'Forthyr']

    city_locations = []
    routes = []

    ''' Setup cities and routes in here'''
    city_locations = get_randomly_spread_cities(size, len(city_names))
    routes = get_routes(city_names)

    city_locations_dict = {name: location for name,
                           location in zip(city_names, city_locations)}
    random.shuffle(routes)
    routes = routes[:10]
    displayNames = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    displayNames = not displayNames

        screen.fill(black)
        screen.blit(pygame_surface, (0, 0))

        ''' draw cities '''
        drawCities(city_locations_dict, city_names,displayNames=displayNames)

        ''' draw first 10 routes '''
        drawCitiesRoutes(city_locations_dict, routes)

        pygame.display.flip()
