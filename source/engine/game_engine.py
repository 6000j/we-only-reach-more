import typing
from typing import List, Set, Dict, Tuple

import engine

class GameEngine:
    """This runs the game. It handles logic and similar, but does not maintain meaningful state outside of the game_state
    """

    # Game ID
    id: int

    # Current state
    state: engine.game_state.GameState


    def __init__(self) -> None:
        pass

    