import typing

import engine
from typing import List, Set, Dict, Tuple


## Tools for converting a GameState to/from jsopn

def export_gamestate(gamestate: engine.game_state.GameState) -> str:
    """Outputs the json representation of the input gamestate

    Args:
        gamestate (engine.game_state.GameState): The gamestate to convert to json

    Returns:
        str: The JSON representation of the gamestate
    """
    pass


def import_gamestate(input: str) -> engine.game_state.GameState:
    """Converts a JSON representation of a GameState into GameState form

    Args:
        input (str): A JSON representation of a GameState

    Returns:
        engine.game_state.GameState: The GameState represented by the JSON
    """
    pass