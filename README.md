# Pokedex

## Setup
To setup environment: 
1. make sure you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) installed
2. Run ```make create_env```

## Description

### Motivation
This application is specifically developed for Pokemon X, as the game does not fill up it's pokedex with all available information.
In game, the only added information is on types of caught pokemon, and the battle data of effectiveness of moves on different pokemon is not logged.

If this data is reasonable to store, it should be possible to learn types of uncaught pokemon by inference on the battle information, which is the goal of this project.

### Current state
Currently, only the terminal app level for logging different types of interactions is developed, it is accesible through 
```make run```.

The GUI is under development, and will be linked with it to simplify the process.

### Future plans and milestones
✅ Terminal level application for logging
- GUI development
- GUI and terminal app connection
- Pokemon type inference
- Containerised app?
- Automatisation of the app using Computer Vision
