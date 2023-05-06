# Write a query that returns all the Pokemon with an ability of "Overgrow"

import sqlite3
import sys
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# finds Pokemon with ability of "Overgrow"
pokemon_ability_overgrow = pokemonColl.find({ "abilities": { "$regex": ".*Overgrow.*" } })

# Prints
for pokemon in pokemon_ability_overgrow:
    print(pokemon)