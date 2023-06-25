import typing
from typing import List, Set, Dict, Tuple, Any

import engine.game_state as game_state

import hexutils.rbg_hex_functionality as rhex

## superclass for "Gamepieces"
## Doesn't actually need that many things I don't think?
## This does literally nothing for now lmao
class Piece:
    
    # Name
    name: str

    # Properties/Tags
    properties: dict[Any]

    # Owner is a string to allow for weird stuff
    owner: str


    def __init__(self) -> None:
        # Initialising variables
        self.properties = {}
        

    



    # Timing hooks
    def start_of_turn(gamestate: game_state.GameState) -> None:
        """This is run at the start of each turn.

        Args:
            gamestate (game_state.GameState): _description_
        """
        pass

    def start_of_main(gamestate: game_state.GameState) -> None:
        pass

    def end_of_main(gamestate: game_state.GameState) -> None:
        pass

    def start_of_reaction(gamestate: game_state.GameState) -> None:
        pass

    def end_of_reaction(gamestate: game_state.GameState) -> None:
        pass

    def end_of_turn(gamestate: game_state.GameState) -> None:
        pass