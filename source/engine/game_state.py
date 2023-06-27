import typing
from typing import List, Set, Dict, Tuple

import engine

class GameState:
    """This stores the entire current known gamestate
    It is purely a data storage object, and handles no game logic itself.
    """
    
    # Things to store: 
    
    # Turn progress

    # Map:
    map: engine.game_map.GameMap

    # Turn/phase:
    turn: engine.game_turn.GameTurn

    players: list[engine.game_player.GamePlayer]

    def __init__(self) -> None:
        pass

    