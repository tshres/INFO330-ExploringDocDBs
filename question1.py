# Write a query that returns all the Pokemon named "Pikachu"

import sqlite3
import sys
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Finding Pikachu Pokemon
pikachu_find = pokemonColl.find({"name": "Pikachu"})

# Print
for pokemon in pikachu_find:
    print(pokemon)