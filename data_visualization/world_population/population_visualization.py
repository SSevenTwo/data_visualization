import json
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
from country import get_country_code
from pygal.maps.world import World

#Load the data into a list
filename = "data_json.json"
with open(filename) as f:
    population_data = json.load(f)

#Create a dictionary of populations
populations = {}
for pop_dictionary in population_data:
    if pop_dictionary["Year"] == 2015:
        country_name = pop_dictionary["Country Name"]
        population = pop_dictionary["Value"]
        code = get_country_code(country_name)
        
        #Some countries don't have a country code
        if code:
            populations[code] = population
    
#Seperating the countries into 3 different population levels for better visuals
population_1, population_2, population_3 = {},{},{}

for country,population in populations.items():
    if population < 10000000:
        population_1[country] = population
    elif population < 1000000000:
        population_2[country] = population
    else:
        population_3[country] = population

print(populations)

wm_style = RotateStyle("#336699", base_style = LightColorizedStyle)
wm = World(style = wm_style)
wm.title = "World Population in 2015, by Country"
wm.add("<10 Million",population_1)
wm.add("10M - 1BN",population_2)
wm.add("1BN+",population_3)
wm.force_uri_protocol = 'http'

wm.render_to_file("population.svg")
