import typing
from typing import List, Set, Dict, Tuple, Any

from enum import Enum, auto


class PlayerType(Enum):
    """The types of players
    SYSTEM (0): system player. Used for backend stuff. Don't worry about it
    USER (1): User player. Played by a user.
    """
    SYSTEM = 0
    USER = 1

class GamePlayer():
    """A player in the game. Data Collection Class
    """

    player_id: int
    player_tag: str
    
    player_visible_name: str

    player_type: PlayerType # CHANGE TO ENUM

    def __init__(self, id: int, tag: str, vis_name: str, player_type: PlayerType) -> None:
        self.player_id = id
        self.player_tag = tag
        self.player_visible_name = vis_name
        self.player_type = player_type