import typing
from typing import List, Set, Dict, Tuple

import engine
import game_components as gc


class GameState:
    """This stores the entire current known gamestate
    It is purely a data storage object, and handles no game logic itself.
    """
    
    # Things to store: 
    
    # Turn progress

    # Map:
    map: engine.game_map.GameMap
    # These two are here instead of being tracked in the game_map, because it means we don't have to send over
    # the game_map when we serialise the game_state for networking
    map_height: int 
    map_width: int


    # Turn/phase:
    turn: engine.game_turn.GameTurn

    # By tracking players and pieces, we can "spin up" a new map whenever we need it.
    players: list[engine.game_player.GamePlayer]
    pieces: list[gc.piece.Piece]

    def __init__(self) -> None:
        pass

    


    def create_map(self) -> engine.game_map.GameMap:
        """Returns a GameMap corresponding to the current pieces here
        At a technical level, it is creating a new GameMap each time, rather than updating the current one.

        Returns:
            engine.game_engine.GameMap: The GameMap corresponding to the pieces we know about
        """
        # Create the map
        temp_map: engine.game_map.GameMap = engine.game_map.create_map_of_size(self.map_height, self.map_width)

        for pc in self.pieces:
            temp_map[]
        

    def update_map(self) -> None:
        """Updates our current map to the one that would be created
        """
        self.map = self.create_map()