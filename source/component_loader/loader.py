import typing
from typing import List, Set, Dict, Tuple

import game_components.cape as cape
import game_components.ability as ability

# This will load stuff in the future; for now it's just a file.


def load_cape_folder(path: str) -> cape.Cape:
    """Loads a Cape Folder, complete with abilities

    Args:
        path (str): the path to the folder to load from.

    Returns:
        cape.Cape: An object representing the given cape.
    """
    pass

def load_cape(path: str) -> cape.Cape:
    """Loads a cape from a python class file

    Args:
        path (str): the path to the file.

    Returns:
        cape.Cape: the Cape.
    """
    pass

def load_ability(path: str) -> ability.Ability:
    """Loads an Ability from a file

    Args:
        path (str): the path to the file.

    Returns:
        ability.Ability: the loaded Ability.
    """
    pass