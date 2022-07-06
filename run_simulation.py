#!/usr/bin/env/python
from orchard import Orchard
num_games = 1000
results = []
for i in range(num_games):
    game = Orchard()
    results.append(game.play_game())

raven_percentage = len([x for x in results if x])/num_games
print(f'Raven won {raven_percentage*100:.2f}% of the games')