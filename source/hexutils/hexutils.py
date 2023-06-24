import math
import collections
import numpy as np
import hexy as hx
import rbg_hex_functionality as rhf

import typing
from typing import List, Set, Dict, Tuple

## Most of this stuff will be from https://github.com/RedFT/Hexy, or https://www.redblobgames.com/grids/hexagons/codegen/output/lib.py,
#  but I want an implementation of supercover, so I have to do a bunch of work :( :( :(

# We create mask functions for the get_hex_line and cube_round functions from Hexy that support what we wish to do.
## This is an implementation of multiple hex line functionalities.
def get_hex_line(hex_start, hex_end, supercover=False):
    """
    Get hexes on line from hex_start to hex_end.
    :param hex_start: The hex where the line starts.
    :param hex_end: The hex where the line ends.
    :param supercover=False: If supercover is true, we include both hexes if the straight line would pass directly between two.
    :return: A set of hexes along a straight line from hex_start to hex_end. This is returned in list form, because it's my code and I feel far more confident in being able to correctly handle those than to correctly handle np arrays.
    """
    if supercover: # We create supercover by nudging our hexes in both directions, combining our outputs, and then removing duplicates
        a = rhf.Hex(hex_start[0].item(), hex_start[1].item(), hex_start[2].item())
        b = rhf.Hex(hex_end[0].item(), hex_end[1].item(), hex_end[2].item())
        N = rhf.hex_distance(a, b)

        
        # Nudging to one side
        a_nudge = rhf.Hex(a.q + 1e-06, a.r + 1e-06, a.s - 2e-06)
        b_nudge = rhf.Hex(b.q + 1e-06, b.r + 1e-06, b.s - 2e-06)
        results = []
        
        step = 1.0 / max(N, 1)
        # print(N)
        for i in range(0, N + 1):
            results.append(rhf.hex_round(rhf.hex_lerp(a_nudge, b_nudge, step * i)))
        # Nudging to the other!
        a_nudge = rhf.Hex(a.q - 1e-06, a.r - 1e-06, a.s + 2e-06)
        b_nudge = rhf.Hex(b.q - 1e-06, b.r - 1e-06, b.s + 2e-06)
        for i in range(0, N + 1):
            results.append(rhf.hex_round(rhf.hex_lerp(a_nudge, b_nudge, step * i)))

        # Removing duplicates
        results = list(set(results))
        # Returning as the np array we expect
        return results
    else: # However we 
        return hexarr_to_hextup(hx.get_hex_line(hex_start, hex_end))
    

# Converts hex tuples to hex arrays. don't worry about this <3
def hextup_to_hexarr(hex):
    return np.array((hex.q, hex.r, hex.s))

# Converts hex arrays to hex tuples. don't worry about this <3
def hexarr_to_hextup(hexes):
    oup = []
    for hex in hexes:
        oup.append(rhf.Hex(hex[0], hex[1], hex[2]))
    return oup
    