import typing
from typing import List, Set, Dict, Tuple, Any
from enum import Enum, auto

import piece as pc
import cape as cape

import engine.game_state as game_state

import hexutils.rbg_hex_functionality as rhex


# Only active for now
class AbilityType(Enum):
    ACTIVE = auto()
    PASSIVE = auto()

# Abilities are the abilities of things. They're also like, moving and stuff.

class Ability:
    """An ability for a cape to use.
    """
    # Ability fundamental values
    ability_name: str
    action_cost: int
    ability_type: AbilityType # This is only allowed to be ACTIVE for now
    max_charges: int
    current_charges: int

    def __init__(self) -> None:
        pass

    def get_legal_targets(self, gamestate: game_state.GameState, user: cape.Cape) -> List[rhex.Hex]:
        """Returns a list of all legal target hexes for this ability if used by the user Cape
        This is based on the known gamestate. This is double-checked for legality in the engine.

        Args:
            gamestate (game_state.GameState): The current known GameState to use for choosing a target
            user (cape.Cape): The Cape using the ability

        Returns:
            List[rhex.Hex]: The hex locations that we can target.
        """
        pass




