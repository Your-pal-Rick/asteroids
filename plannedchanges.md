# Refactoring:
    - [x] Decompose main() into game.py:
        - [x] Initialisation:
            - [x] Initialise pygame, create game clock and screen surface
            - [x] Create sprite groups
            - [x] Assign class containers
        - [x] Events and updates:
            - [x] Check for game quit
            - [x] Update game state
            - [x] Handle collisions
            - [x] Render background and objects
            - [x] Update dt/regulate framerate
        - [x] Run game:
            - [x] Call above methods
    - [x] Merge modules
        - [x] asteroid.py + asteroidfield.py
        - [x] player.py + shot.py
        - [x] Update imports accordingly
    - [x] Organise imports
        - [x] main.py
        - [x] game.py
        - [x] circleshape.py
        - [x] player.py
        - [x] asteroid.py
        - [x] constants.py
    - [x] Organise constants
        - [x] Replace unexplained numbers in code
        - [x] Structure constants
            - [x] Pick a method -- Dataclasses look interesting
        - [x] Refactor code to accept new settings structure
    - [x] Update Player class -- Not necessary, singleton passed to Game class
    - [x] Add custom exit messages
        - [x] Ship death message
        - [x] Manual exit message
    - [ ] Could store Player class settings in a dataclass in player module for 
          usability/readability reasons? Look into whether this is useful

# Documentation:
    - [ ] Docstrings
        - [x] main.py
            - [x] module - summary, usage, dependencies, controls
            - [x] func main()
        - [x] game.py
            - [x] class Game
            - [x] methods
        - [x] circleshape.py
            - [x] module
            - [x] class CircleShape
        - [x] player.py
            - [x] module
            - [x] class Player
            - [x] class Shot
        - [ ] asteroid.py
            - [x] module
            - [ ] class Asteroid
            - [ ] class AsteroidField
        - [x] constants.py

# Game feel
    - [ ] Adjust object velocities
        - [x] Player
        - [x] Shots
        - [ ] Asteroids -- Requires moving velocity out to GameSettings
        - [ ] Split asteroids -- As above
    - [x] Adjust shot cooldown -- Fine as it is
    - [x] Adjust object colo(u)rs
        - [x] Player
        - [x] Shots
        - [x] Asteroids (based on radius?)
    - [x] Add colour fills?
        - [x] Player
        - [x] Shots
        - [x] Asteroids
    - [ ] Double-line player ship?

Reassess after above changes made.