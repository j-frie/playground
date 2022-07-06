# playground

This is a repository for toy projects - have fun :-)



## Simulation of the game "Orchard" ("Obstgarten") by Ravensburger.

The game is for small children and the rules of the game are pretty simple:
There are four trees with fruits in an orchard, each tree has fruits with a different color.
At the beginning, the raven sits several steps away from the orchard.
The goal is to harvest all fruits before the raven reaches the orchard.

A six-sided die is rolled. If it shows a raven, the raven moves one
step forward. If it shows a basket, a fruit can be chosen from any tree.
If it shows a color, one fruit with this color can be harvested.


## Run a simulation
The class `Orchard` can be used to estimate the winning chances of the raven.
```from orchard import Orchard
num_games = 1000
results = []
for i in range(num_games):
    game = Orchard(max_fruits=4, num_raven_steps=6)
    results.append(game.play_game())

raven_percentage = len([x for x in results if x])/num_games
print(f'Raven won {raven_percentage*100:.2f}% of the games')
```

## Run the tests
```python - m unittest tests.py```
