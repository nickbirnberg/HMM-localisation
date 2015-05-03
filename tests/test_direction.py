__author__ = 'nick'

import unittest

from hmm_localisation.robot import Direction


class TestDirection(unittest.TestCase):
    def test_opposite_north(self):
        dir = Direction.NORTH
        opp = Direction.opposite(dir)
        self.assertEqual(opp, Direction.SOUTH)

    def test_opposite_east(self):
        dir = Direction.EAST
        opp = Direction.opposite(dir)
        self.assertEqual(opp, Direction.WEST)

    def test_opposite_south(self):
        dir = Direction.SOUTH
        opp = Direction.opposite(dir)
        self.assertEqual(opp, Direction.NORTH)

    def test_opposite_west(self):
        dir = Direction.WEST
        opp = Direction.opposite(dir)
        self.assertEqual(opp, Direction.EAST)


if __name__ == '__main__':
    unittest.main()
