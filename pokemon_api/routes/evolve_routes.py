from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from data.database import get_db
import utils.sql_queries as check_functions
import utils.get_queries as select_check_functions
import utils.delete_queries as delete_functions
import utils.insert_queries as insert_functions

router = APIRouter()

@router.put('/evolution')
def evolve(trainer_name: str, pokemon_name: str, next_evolution: str, db: Session = Depends(get_db)):
    """
    Evolve the given pokemon of the given trainer.

    Parameters:
    - pokemon_name: name of the pokemon.
    - trainer_name: name of the trainer.
    """
    #Check if pokemon and trainer exist
    if not check_functions.is_pokemon_in_table(db, pokemon_name) and not check_functions.is_trainer_in_table(db, trainer_name):
        raise HTTPException(404, detail="Pokemon/Trainer not found")
    
    #Check if evolution is possible
    if not next_evolution:
        raise HTTPException(403, detail="No evoilution possible")
    old_pokemon = select_check_functions.select_pokemon(db, pokemon_name)
    pokemon = select_check_functions.select_pokemon(db, next_evolution)
    trainer = select_check_functions.select_trainer(db, trainer_name)
    #Check if pokemon is already in the pokedex
    if  check_functions.is_in_pokedex(db, old_pokemon.pokemon_id, trainer.trainer_id) and not check_functions.is_in_pokedex(db, pokemon.pokemon_id, trainer.trainer_id):
        delete_functions.delete_from_pokedex(db,old_pokemon.pokemon_id, trainer.trainer_id )
        insert_functions.insert_into_Pokedex_table(db, pokemon.pokemon_id, trainer.trainer_id)
        return {f"Status code: {status.HTTP_200_OK}","Evolution was successfull"}
    else:
        raise HTTPException(409, detail="Cant evolve this pokemon")