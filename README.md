# Game-of-Life
Cellular automation programmed in python. The game is governed by a set of simple rules that dictate the state of each cell in the world depending on its current state and state of its neighbours.


## `test_gameoflife_glider.py`
Opens an animated simulation of universe with a pattern of live cells. The universe is evolved by applying the rules below.
Note: Algorithm relies on the use of initial class called `conway.py`, and is required to run the simulation.

### The Rules
```
- Underpopulation: A live cell that has < 2 live neighbouring cells will die
- Survival: A live cell that has 2-3 live neighbouring cells will remain alive
- Overpopulation: A live cell with more than 3 live neighbours will die
- Reproduction: A dead cell with exactly 3 live neighbours will become alive
```

### Usage Description
Initial patterns can be changed from `blinker`, `glider`or `glider gun` using `life.insertBlinker((0,0))`, `life.insertGlider((0,0))`, `life.insertGliderGun((0,0))` 
Else, cell states can be imported via `input.txt` directly. See example file above.
 
  
   
   

# Langton's Ant
Cellular automation that is Turing complete and displays chaotic behaviour. A single ant roams a space consisting of 64x64 space on a set rule.

## `langton.py`
Opens an animated simulation of an universe with an ant. The ant moves erratically according to the following rules:

### The Rules
```
- If on a white square, toggle the colour of the square and move to the square on the right.
- If on a black square, toggle the colour of the square and move to the square on the left.
```

### Usage Description
Compile and run the `langton.py` file to simulate Langton's ants. The program will automatically stop after 11000 steps. See the PNG image file above to preview the behaviour exhibited by the ant after 11000 steps.



