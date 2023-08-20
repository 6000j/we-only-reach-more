import typing
from typing import List, Set, Dict, Tuple, Any

import piece as pc
import ability as ab

import engine.game_state as game_state

import hexutils.rbg_hex_functionality as rhex

## Our capes outline!

class Cape(pc.Piece):
    # Name/Piece info (This is duplicated here for easy of documentation)
    name: str
    # Properties/Tags
    properties: dict[Any]

    # Base Stats
    max_health: int
    main_actions: int
    reaction_actions: int
    view_distance: int

    # Volatile Stats
    current_health: int
    action_points: int
    alive: bool

    # Ability List
    abilities: List[ab.Ability]

    # Current Field of View
    # Unfortunately, figures do probably need to know this :ouagh:
    curr_view: List[rhex.Hex]


    def __init__(self) -> None:
        super().__init__()
        self.current_health = self.max_health
        self.alive = True



    # Line of sight, field of view stuff.
    
    def generate_field_of_view(self, game_state: game_state.GameState) -> List[rhex.Hex]:
        """Returns a list of the Hex locations that this Cape can see from where they currently are

        Args:
            game_state (game_state.GameState): The current GameState.

        Returns:
            List[rhex.Hex]: A list of the rhex.Hex locations that this cape can see.
        """
        return self.generate_field_of_view_from_point(self.location, game_state)
    
    def generate_field_of_view_from_point(self, my_location: rhex.Hex, game_state: game_state.GameState) -> List[rhex.Hex]:
        """Returns a list of the Hex locations that this Cape can see from a given location

        Args:
            my_location (rhex.Hex): The location that field of view will be calculated starting from.
            game_state (game_state.GameState): The current GameState.

        Returns:
            List[rhex.Hex]: A list of the rhex.Hex locations that this cape can see.
        """
        pass

    def can_see_location(self, goal_location: rhex.Hex, game_state: game_state.GameState) -> bool:
        """Checks if we can see a given location from where we currently are
        We do this by checking that we can see through all tiles between the two locations

        Args:
            goal_location (rhex.Hex): The location to check if we can see.
            game_state (game_state.GameState): The current GameState.

        Returns:
            bool: Whether we can see the goal_location.
        """
        return self.can_see_location_from_point(self.location, goal_location, game_state)

    def can_see_location_from_point(self, my_location: rhex.Hex, goal_location: rhex.Hex, game_state: game_state.GameState) -> bool:
        """Checks if we can see a given location from a given location
        We do this by checking that we can see through all tiles between the two locations

        Args:
            my_location (rhex.Hex): Our current location.
            goal_location (rhex.Hex): The location to check if we can see.
            game_state (game_state.GameState): The current GameState.

        Returns:
            bool: Whether we can see the goal_location.
        """
        pass

    # Abilities
    # Returns if the ability could successfully be used?
    
    def use_ability(self, ability: ab.Ability, gamestate: game_state.GameState) -> bool:
        """
        This cape uses ability on the gamestate. Returns False if the ability could not be used for whatever reason, True otherwise

        Args:
            ability (game_components.ability.Ability): The ability object to use. You need to have obtained this already to call this method.
            gamestate (engine.game_state.GameState): The gamestate to use the ability in.

        Returns:
            successful (bool): A bool indicating if the Ability was successfully able to be used or not.
        """
        pass

