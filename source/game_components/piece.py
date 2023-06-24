import typing
from typing import List, Set, Dict, Tuple

## superclass for "Gamepieces"
## Doesn't actually need that many things I don't think?
## This does literally nothing for now lmao
class Piece:
    
    # Name
    name: str

    # Tags, for a bunch of uses
    tags: List[str]


    def __init__(self) -> None:
        pass