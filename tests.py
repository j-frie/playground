import unittest
from orchard import Orchard


class TestOrchard(unittest.TestCase):

    def test_get_number_of_fruits(self):
        orch = Orchard(max_fruits=4)
        self.assertEqual(orch.get_number_of_fruits_left(), len(orch.colors) * 4)

    def test_roll_die(self):
        orch = Orchard(max_fruits=4, num_raven_steps=6)
        die_result = orch.roll_die()
        self.assertIn(die_result, orch.die)

    def test_roll_die_statistics(self):
        orch = Orchard(max_fruits=4, num_raven_steps=6)
        num_rolls = 1000
        die_results = [orch.roll_die() for i in range(num_rolls)]
        red_percentage = len([x for x in die_results if x == 'red'])/num_rolls
        self.assertAlmostEqual(red_percentage, 1/6, delta=0.02)

    def test_move(self):
        orch = Orchard(max_fruits=4, num_raven_steps=6)
        self.assertEqual(orch.raven_position, -6)
        orch.move('raven')
        self.assertEqual(orch.raven_position, -5)
        self.assertEqual(orch.trees['red'], 4)
        self.assertEqual(orch.trees['yellow'], 4)
        orch.move('red')
        self.assertEqual(orch.trees['red'], 3)
        self.assertEqual(orch.trees['yellow'], 4)
        orch.move('basket')
        # 2 fruits were already harvested (1 red, 1 random)
        self.assertEqual(orch.get_number_of_fruits_left(), 14)

