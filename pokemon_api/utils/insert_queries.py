from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.orm import Session
from utils.sql_queries import is_pokemon_in_table, is_type_in_table, is_trainer_in_table, is_in_pokemontype, is_in_pokedex
def insert_into_pokemons_table(db: Session, name: str, height: int, weight: int):
    if not is_pokemon_in_table(db, pokemon_name=name):
        query = text("""
                INSERT INTO `pokemons` 
                (name, height, weight) 
                VALUES 
                (:name, :height, :weight)
            """)
        db.execute(
            query,
            {
                "name": name,
                "height": height,
                "weight": weight,
            }
        )
        db.commit()


def insert_into_types_table(db: Session, types: list):
    for pokemon_type in types:
        if not is_type_in_table(db, pokemon_type):
            query = text("""
                    INSERT INTO `types` 
                    (pokemon_type) 
                    VALUES 
                    (:pokemon_type)
                """)
            db.execute(
                query,
                {
                    "pokemon_type": pokemon_type,
                    
                }
            )
            db.commit()

def insert_into_trainers_table(db: Session, name: str, town: str):
    if not is_trainer_in_table(db, trainer_name=name):
        query = text("""
                INSERT INTO `trainers` 
                (name, town) 
                VALUES 
                (:name, :town)
            """)
        db.execute(
            query,
            {
                "name": name,
                "town": town
            }
        )
        db.commit()

def insert_into_PokemonTypes_table(db: Session, pokemon_id: int, type_id: int):
    if not is_in_pokemontype(db, pokemon_id, type_id):
        query = text("""
                    INSERT INTO `pokemontypes` 
                    (pokemon_id, type_id) 
                    VALUES 
                    (:pokemon_id, :type_id)
                """)
        db.execute(
            query,
            {
                "pokemon_id": pokemon_id,
                "type_id": type_id
            }
        )
        db.commit()

def insert_into_Pokedex_table(db: Session, pokemon_id: int, trainer_id: int):
    if not is_in_pokedex(db, pokemon_id, trainer_id):
        query = text("""
                    INSERT INTO `pokedex` 
                    (pokemon_id, trainer_id) 
                    VALUES 
                    (:pokemon_id, :trainer_id)
                """)
        db.execute(
            query,
            {
                "pokemon_id": pokemon_id,
                "trainer_id": trainer_id
            }
        )
        db.commit()