# Overall Game Structure:

## Seperate modules/structure:
- GUI
- Engine (backend)
- Networking

## Networking model:
- Client-Server model.
- Clients on either end, connect to server
- Server knows the full gamestate, clients only ever know what they need to know.
    - This prevents game logic ever leaking information the player shouldn't know. 
    - Because of this leaking prevention, there's no risk of leaking info with rewinds/etc, which is big.
    - Update both clients at specified times. 
- Use http? This means port forwarding isn't required hopefully. Turn-based, so I'm not concerned about overhead

## Engine Model:
- `Engine` should be "loadable" almost at will.
- `GameState`
    - This has to support both complete and incomplete information.
    - Doesn't contain logic
    - Contains `hexMap`
- `HexMap`
    - Purely an array-like situation. Has tools for defining distances and known information, checking information at points, etc.
    - `get_at` or whatever, keeps track of everything. 
    - Speed again does not matter because of how infrequently we should actually be updating stuff?

### Capes
- `Cape` "interface" implements:
    - `Get_Abilities` (Returns `Iterable[Ability]`)
    - `__init__` (duh)
    - `use_ability`? (Unsure)
    - `take_damage`? (Also unclear. Needs some way for capes to "hit" each other cleanly that won't require adding code for new attacks)
    - `update_position`
    - `get_view`
    - 

## GUI Model:
- Needs to be able to turn a `GameState` into a visualisation
- Needs to be able to recognise player clicks and see available options