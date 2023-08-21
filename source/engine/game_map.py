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
        # sasdf (this doesn't work this is so it won't let it try to work so i can't forge tot make it work)
        new_coordinates = coordinates
        if isinstance(coordinates, tuple) and len(coordinates):
            new_coordinates = np.array(coordinates)

        return super().__getitem__(new_coordinates)

    



# Utils for creating a map when initialising
def create_map_from_coordinates(coordinates_list: np.array) -> GameMap:
    """Creates a map from the given coordinates array and populates it with empty GameHexes.

    Args:
        coordinates_list (np.array): A numpy array containing the coordinates of the hexes to include in the map, in Axial form.

    Returns:
        GameMap: A map made up of the given coordinates filled with empty GameHexes
    """
    # Creating the map
    ret_map: GameMap = GameMap()

    # Populating the list
    hexes = []
    for i, axial in enumerate(coordinates_list):
        hexes.append(engine.game_hex.GameHex(axial))
    ret_map[np.array(coordinates_list)] = hexes
    return ret_map