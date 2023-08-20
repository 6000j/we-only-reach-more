import typing
from typing import List, Set, Dict, Tuple

import hexy as hx
import engine
import numpy as np


class GameMap(hx.HexMap):
    """This is the current map of the board. For now is literally just hexy.HexMap
    """

    # I don't want to worry about numpy in general, so we're going to override __getitem__ and __delitem__
    def __getitem__(self, coordinates):
        sasdf (this doesn't work this is so it won't let it try to work so i can't forge tot make it work)
        new_coordinates = coordinates
        if isinstance(coordinates, tuple) and len(coordinates):
            new_coordinates = np.array(coordinates)

        return super().__getitem__(new_coordinates)

    



# Utils for creating a map when initialising
def create_map_of_size(height: int, width: int) -> GameMap:
    """Creates a rectangular GameMap populated with empty GameHex's of the height and width given.

    Args:
        height (int): How many rows are in the map
        width (int): How many columns are in the map

    Returns:
        GameMap: A rectangular GameMap of dimensions Height x Width populated with empty GameHexes.
    """
    # Creating the map
    ret_map: GameMap = GameMap()

    # Populating it
    for y in range(height):
        for x in range(width):
            nu_x = x - y//2 # Integer division
            ret_map[np.array([nu_x, y])] = engine.game_hex.GameHex(nu_x, y)

    return ret_map