import typing
from typing import List, Set, Dict, Tuple, Any
from enum import Enum, auto



class VisibilityEnum(Enum):
    """The different levels of visibility for an object. These are then stored for various values of OWNER/OTHER in a Visibility thing
    NONE means never visible
    LOCAL means visible if a character has it in their FoV
    GLOBAL means always visible
    """
    NONE = auto()
    LOCAL = auto()
    GLOBAL = auto()


class VisibilitySettings():
    """The owner and global visibility settings of an object
    """

    owner_visibility: VisibilityEnum
    global_visibility: VisibilityEnum

    def __init__(self, owner_vis: VisibilityEnum, global_vis: VisibilityEnum) -> None:
        self.owner_visibility = owner_vis
        self.global_visibility = global_vis

    