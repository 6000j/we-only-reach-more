import typing
from typing import List, Set, Dict, Tuple, Any


import numpy as np
import hexy as hx

import hexutils as hu
import game_components as gc


class GameHex(hx.HexTile):
    
    # Coordinates
    axial_coordinates: np.array
    cube_coordinates: np.array
    rhex_coordinates: hu.rhex.Hex

    # Things on this hex currently
    ground_objects: List[gc.piece.Piece] # This includes both walls and other stuff like GrueSmog. May change later
    cape_occupants: List[gc.cape.Cape] # This is a list by technicality, mostly



    # I'm mostly just like. really hopeful ig
    # Not even sure if this is actually useful I won't lie.
    def __init__(self, axial_coordinates) -> None:
        self.axial_coordinates = np.array([axial_coordinates])
        self.cube_coordinates = hx.axial_to_cube(self.axial_coordinates)
        self.rhex_coordinates = hu.hexutils.hexarr_to_hextup(self.cube_coordinates)

    

    # def get_draw_position(self):
    #     """
    #     Get the location to draw this hex so that the center of the hex is at `self.position`.
    #     :return: The location to draw this hex so that the center of the hex is at `self.position`.
    #     """
    #     draw_position = self.position[0] - [self.image.get_width() / 2, self.image.get_height() / 2]
    #     return draw_position

    # def get_position(self):
    #     """
    #     Retrieves the location of the center of the hex.
    #     :return: The location of the center of the hex.
    #     """
    #     return self.position[0]


