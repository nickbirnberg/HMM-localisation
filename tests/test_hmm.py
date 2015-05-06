__author__ = 'nick'

import unittest

import numpy as np

from hmm_localisation.hmm import HMM
from hmm_localisation.robot import Direction


class TestHMM(unittest.TestCase):
    def test_probable_transitions_corner(self):
        model = HMM(8, 8)
        corner = (7, 0, Direction.SOUTH)
        expected = [((7, 1, Direction.SOUTH), 0.7),
                    ((7, 1, Direction.NORTH), 0.1),
                    ((7, 1, Direction.EAST), float(1) / 3),
                    ((7, 1, Direction.WEST), 0.1),
                    ]
        self.assertEqual(sorted(model.probable_transitions(corner)),
                         sorted(expected))

    def test_probable_transitions_wall(self):
        model = HMM(8, 8)
        wall = (3, 7, Direction.EAST)
        expected = [((2, 7, Direction.NORTH), float(1) / 3),
                    ((2, 7, Direction.SOUTH), 0.1),
                    ((2, 7, Direction.EAST), 0.7),
                    ((2, 7, Direction.WEST), 0.1),
                    ]
        self.assertEqual(sorted(model.probable_transitions(wall)),
                         sorted(expected))

    def test_probable_transitions_one_away_from_wall(self):
        model = HMM(8, 8)
        one_away = (7, 6, Direction.SOUTH)
        expected = [((7, 7, Direction.SOUTH), 0.7),
                    ((7, 7, Direction.NORTH), float(1) / 2),
                    ((7, 7, Direction.EAST), float(1) / 2),
                    ((7, 7, Direction.WEST), 0.1),
                    ]
        self.assertEqual(sorted(model.probable_transitions(one_away)),
                         sorted(expected))

    def test_probable_transitions_inner(self):
        model = HMM(8, 8)
        inner = (3, 3, Direction.WEST)
        expected = [((4, 3, Direction.SOUTH), 0.1),
                    ((4, 3, Direction.NORTH), 0.1),
                    ((4, 3, Direction.EAST), 0.1),
                    ((4, 3, Direction.WEST), 0.7),
                    ]
        self.assertEqual(sorted(model.probable_transitions(inner)),
                         sorted(expected))

    def test_probably_transitions_edge(self):
        model = HMM(3, 3)
        edge = (0, 0, Direction.EAST)
        expected = []
        self.assertEqual(model.probable_transitions(edge), expected)

    def test_create_t_matrix(self):
        model = HMM(2, 2)
        self.assertIsInstance(model.t_matrix, np.ndarray)
        self.assertEqual(model.t_matrix.size, 256)

    def test_create_sensor_matrix(self):
        model = HMM(8, 8)
        sensor_matrix = model.create_sensor_matrix((1, 1))
        self.assertEqual(sensor_matrix.size, 65536)
        self.assertEqual(sensor_matrix[0, 1], 0)
        self.assertEqual(sensor_matrix[0, 0], 0.05)
        self.assertEqual(sensor_matrix[36, 36], 0.1)
        self.assertEqual(sensor_matrix[44, 44], 0.025)
        sensor_matrix = model.create_sensor_matrix(None)
        self.assertEqual(sensor_matrix.size, 65536)

    def test_none_matrix(self):
        model = HMM(8, 8)
        none_matrix = model.none_matrix
        self.assertEqual(none_matrix.size, 65536)
        self.assertEqual(none_matrix[0, 0], 0.625)
        self.assertEqual(none_matrix[144, 144], 0.1)
        self.assertEqual(none_matrix[132, 132], 0.225)
        self.assertAlmostEquals(none_matrix[128, 128], 0.425)

    def test_priors(self):
        model = HMM(8, 8)
        self.assertEqual(model.f_matrix[5], float(1) / (8 * 8 * 4))

    def test_forward(self):
        model = HMM(8, 8)
        model.forward_step((4, 4), Direction.NORTH)
        self.assertNotEqual(model.f_matrix[5], float(1) / (8 * 8 * 4))

    def test_most_probable(self):
        model = HMM(8, 8)
        model.forward_step((4, 2), Direction.NORTH)
        self.assertEqual(model.most_probable(), (4, 2))
        model.forward_step((4, 3), Direction.NORTH)
        self.assertEqual(model.most_probable(), (4, 3))
        model.forward_step((4, 6), Direction.NORTH)
        self.assertEqual(model.most_probable(), (4, 4))
        model.forward_step((5, 7), Direction.NORTH)
        self.assertEqual(model.most_probable(), (4, 5))
        model.forward_step((5, 2), Direction.SOUTH)
        self.assertEqual(model.most_probable(), (4, 4))
        model.forward_step((5, 2), Direction.EAST)
        self.assertEqual(model.most_probable(), (5, 4))

    def test_generate_direction_matrices(self):
        model = HMM(8, 8)
        self.assertEqual(model.direction_matrices[0][0], 1)
        self.assertEqual(model.direction_matrices[0][1], 0)
        self.assertEqual(model.direction_matrices[1][1], 1)
        self.assertEqual(model.direction_matrices[1][0], 0)
        self.assertEqual(model.direction_matrices[2][2], 1)
        self.assertEqual(model.direction_matrices[2][1], 0)
        self.assertEqual(model.direction_matrices[3][3], 1)
        self.assertEqual(model.direction_matrices[3][1], 0)

    if __name__ == '__main__':
        unittest.main()