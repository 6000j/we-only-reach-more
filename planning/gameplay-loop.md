# Gameplay Loop

# Board:
- Hex-based
- Size to be determined; may vary by map
- Asymmetric goals; Fog of War heavily involved
- Pre-defined maps

## Board ideas:
### Bank Scene
    - Supervillains have to get to the vault, spend two turns there, and then get out
    - Superheroes have to stop this.
    - Vault is challenging to defend because only one goal location
### Standard Tactical Shooter setup:
    - Multiple goal locations
    - Have to spend two turns to plant
    - Superheroes have to spend only one turn cycle to defuse probably. 

# Gameplay Loop:

## Core Pitch:
- 1v1 PvP game.
- Heroes have to defend, Villains have to attack
- Time limit forces combat, aim to get this to as low a value as is possible without sacrificing gameplay.
- Turn-based information-driven gameplay. Combat is fast once it starts; heavy inspiration from the concepts of tactical shooters like CSGO or Valorant
- Small cape teams, 5v5 or 6v6. Each cape has a collection of abilities they can use.

## Turn Loop:
- Main phase
- Information update
- Reaction phase
- Information update

A `round` consists of one turn for each player.

## Etymology of a turn:

###  Main Phase:

#### Start of Main Phase:
The first thing checked at the start of the `Main Phase` is if a Cape has been standing on a `Goal` tile since the end of the current active player's last turn. If so, they gain one turn of progress towards that `Goal`. Different goals may have different required progress amounts or similar.

Then, all `Durations` on buffs and debuffs currently active are reduced by `1`.

Then, all capes owned by the turn player have their current Action Points set to their `Actions` score. 

#### Main Phase Actions:
The turn player can spend Action Points on their capes as they wish as described in the `Capes` section below. 

**Important**: No actions are actually performed until the turn player has locked in their choices for the main phase. This means movement in the main phase will not give any new information, and attacks will not actually occur. However, ordering still matters (This is a core part of the digital-only space I think is useful to have available). 

#### End of Main Phase:
At the end of a Main Phase, an `Information Update` occurs, and then it is the Turn Player's Reaction Phase.


### Reaction Phase:

#### Start of Reaction Phase:
All capes owned by the turn player have their current Action Points set to their `Reactions` score. Then, "Start of Reaction Phase" effects occur.

#### Reaction Phase Actions:
Then, as in the main phase, Action Points can be spent by the turn player.

#### End of Reaction Phase:
At the end of the Reaction Phase, an `Information Update` occurs, and then the other player's turn starts.



# Capes:

## Basic Stats:
Health: When a cape's health reaches 0, they are defeated for the rest of the game. (Functionally, this is dying. They're no longer involved on the board).
Action/Reactions: `Actions` is the number of Action Points (`AP`) a cape gets during the main phase. `Reactions` is the number of AP the cape gets during the reaction phase.
    - Almost every cape has 1 Reaction.

## Vision:
Each cape can see, by default, **3**(? maybe **2**) hexes in each direction away from them. This is obscured by walls and will not go around corners or similar.

## Abilities:
Capes can have zero or more abilities. Abilities can be `active` or `passive`.

### Active Abilities:
See the section on `Spending AP` below for further information, but tl;dr active abilities are things you do actively.

### Passive Abilities:
Passive abilities of capes may be "always on", or may trigger when a condition is met. As an example, `Aegis` regenerates 1 `Health` at the start of each round.


## Spending AP
You can spend action points to perform actions as listed on the cape
- Move: Almost every cape can spend one action point to move one hex. 
    - Movement will generally be blocked by walls, but some capes may change this. You can move into an area you do not have vision of,.
- Basic Attack: Almost every cape will have some form of basic attack that costs some number of action points. This does damage, and may or may not have range.
- Ability: Capes will often have special abilities that cost some number of action points to use
    - Functionally, Movement and Attacks are just a special type of ability, although things that shut down abilities may not affect movement.
    - Abilities may also have a maximum number of uses per game, or a cooldown.
    - Abilities will almost always have special effects unique to the Cape: e.g, Grue creates an area of darkness that prevents vision by non-Grue capes through it


## Cape Design Goals:
- Most capes will have 1 or 2 health. Most attacks will deal 1 damage. I believe that stat checks are not a particularly interesting gameplay loop in turn-based games, and so the goal is that if you get to actually attack a non-"Fighter" cape, they should probably die instantly.
- The reaction phase is intended to make it not impossible for an attacker to make progress with how information updates work. This is the part I'm least sure about.
- 2-Range attacks are significantly stronger than 1-range attacks.
- Cape abilities are allowed to be busted. Balance can come after designing compelling and flavourful ideas.
- Standard Actions count is 3, standard Reactions count is 1. 
    - This will still hold if I reduce vision distance to 2. I think allowing the player to move into the unknown is interesting. 


