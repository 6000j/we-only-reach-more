import typing
from typing import List, Set, Dict, Tuple

from enum import Enum, auto

import engine


class GamePhase(Enum):
    """The various phases of a turn. Does not track whose turn it is.
    
    Integer values represent standard parts of the turn.
    Non-integer values represent things like setup or end-of-game.
    
    """


    BEGINNING = 0
    MAIN_PHASE = 1
    REACTION_PHASE = 2
    END_PHASE = 3

    SETUP = 'A'
    GAME_END = 'Z'



class GameTurn():
    """This tracks the current turn and phase within the turn, along with the number of turns that have passed.
    It has various utility functions to enable this."""

    # The phase in the current turn
    phase: GamePhase

    # Turn number data
    turn_count: int
    turn_limit: int

    # The list of players
    players: list[engine.game_player.GamePlayer]


    def __init__(self, players: list[engine.game_player.GamePlayer]) -> None:
        pass

    def next_phase(self) -> bool:
        """Advances to the next phase. Returns True if the game is still going, or False otherwise.
        An information update should be performed after each phase anyways.

        Returns:
            bool: Whether or not there is a next phase to go to.
        """
        pass


