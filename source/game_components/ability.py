import typing
from typing import List, Set, Dict, Tuple
from enum import Enum, auto

# Only active for now
class AbilityType(Enum):
    ACTIVE = auto()
    STATIC = auto()

# Abilities are the abilities of things. They're also like, moving and stuff.

class Ability:
    # Ability fundamental values
    ability_name: str
    action_cost: int
    ability_type: AbilityType # This is only allowed to be ACTIVE for now
    max_charges: int
    current_charges: int




