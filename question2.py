# Write a query that returns all the Pokemon with an attack greater than 150

import sqlite3
import sys
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data'

# Finding Pokemon with an attack greater than 150
pokemon_attack = pokemonColl.find({ "attack": { "$gt": 150 } })

# Print
for pokemon in pokemon_attack:
    print(pokemon)