import sqlite3
import sys
from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017/")
pokemon_db = mongo_client["pokemon"]
pokemon_collection = pokemon_db["pokemon_data"]

connection = sqlite3.connect('pokemon.sqlite')
cursor = connection.cursor()

query = """
        SELECT pokemon.name, pokemon.id, pokemon.pokedex_number, pokemon.hp, pokemon.attack, pokemon.defense, pokemon.speed, pokemon.sp_attack, pokemon.sp_defense,
        FROM pokemon
        LEFT JOIN pokemon_abilities ON pokemon.id = pokemon_abilities.pokemon_id
        LEFT JOIN ability ON pokemon_abilities.ability_id = ability.id
        LEFT JOIN pokemon_type ON pokemon.id = pokemon_type.pokemon_id

    """

cursor.execute(query)
data = cursor.fetchall()

pokemon = {}
for row in data:
    pokemon["name"] = row[0]
    pokemon["id"] = row[1]
    pokemon["pokedex_number"] = row[2]
    pokemon["types"] = row[3]
    pokemon["hp"] = row[4]
    pokemon["attack"] = row[5]
    pokemon["defense"] = row[6]
    pokemon["speed"] = row[7]
    pokemon["sp_attack"] = row[8]
    pokemon["sp_defense"] = row[9]
    pokemon["abilities"] = row[10]


pokemonColl.insert_many(pokemon_data)


cursor.close()
connection.close()
mongoClient.close()