import random


class Orchard():
    """ Orchard simulation (game for little children by Ravensburger).

    There are four trees with four fruits each in an orchard.
    Each tree has fruits with a different color.
    At the beginning, the raven sits six steps away from the orchard.
    The goal is to harvest all fruits before the raven reaches the orchard.
    A six-sided die is rolled. If it shows "raven", the raven moves one
    step forward. If it shows a basket, a fruit can be chosen from any tree.
    If it shows a color, one fruit with this color can be harvested.
    """
    def __init__(self, max_fruits=4, num_raven_steps=6):
        """Initialize Orchard game.

        Args:
            max_fruits (int): maximum number of fruits per tree
            num_raven_steps (int): number of steps needed for raven to win
        """
        # the number of colors corresponds to the number of trees
        self.colors = ['yellow', 'green', 'red', 'blue']
        self.trees = {k: max_fruits for k in self.colors}
        self.raven_position = -num_raven_steps
        self.die = ['raven', 'basket'] + self.colors

    def get_number_of_fruits_left(self) -> int:
        """Return total number of fruits left."""
        return sum([v for k,v in self.trees.items()])

    def roll_die(self) -> str:
        """Return result of die roll."""
        return random.choice(self.die)

    def move(self, die_result):
        """Change number of fruits and raven position according to result of die roll.

        Args:
            die_result (str): one (legitimate) result of a die roll
        """
        if die_result == 'raven':
            self.raven_position += 1
        else:
            if die_result == 'basket':
                # here we assume that small children pick a color at random
                die_result = random.choice(self.colors)
            if self.trees[die_result] >= 1:
                self.trees[die_result] -= 1

    def play_game(self, verbose=False) -> bool:
        """Play game until all fruits are harvested or raven wins.

        Args:
            verbose (bool): if True, some information is printed for every move in the game
        Returns:
            bool: True, if raven wins. False otherwise.
        """
        raven_wins = False
        while (self.raven_position < 0) and (self.get_number_of_fruits_left() > 0):
            die_result = self.roll_die()
            self.move(die_result)
            if self.raven_position == 0:
                raven_wins = True
            if verbose:
                print(die_result, 'raven: ', self.raven_position,
                      'nr of fruits: ', self.get_number_of_fruits_left(),
                      'trees: ', self.trees)
        return raven_wins
