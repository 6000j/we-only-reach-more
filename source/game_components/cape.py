import typing
from typing import List, Set, Dict, Tuple

import piece as pc
import ability as ab

import engine.game_state as game_state

import 

## Our capes outline!

class Cape(pc.Piece):

    # Name (This is duplicated here for easy of documentation)
    name: str

    # Base Stats
    max_health: int
    main_actions: int
    reaction_actions: int
    view_distance: int

    # Volatile Stats
    current_health: int
    action_points: int
    alive: bool

    # Ability List
    abilities: List[ab.Ability]


    def __init__(self) -> None:
        super().__init__()
        self.current_health = self.max_health
        self.alive = True



    def get_field_of_view(game_state):
        pass


    