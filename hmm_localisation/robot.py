import random


class Sensor:
    # Settings for robot sensor.
    def __init__(self, grid):
        self.grid = grid

    L = 0.1
    L_s = 0.05
    L_s2 = 0.025

    def sense_location(self):
        """
        Uses sensor to detect current coordinates.
        :return: Tuple of coordinates based on sensing probabilities.
        """
        rand = random.random()
        if rand <= self.L:
            return self.grid.robot_location
        elif rand <= self.L + self.L_s * 8:
            return self.grid.robot_adj_location()
        elif rand <= self.L + self.L_s * 8 + self.L_s2 * 16:
            return self.grid.robot_adj2_location()
        else:
            return None

    def faces_wall(self):
        """
        :return: Boolean whether or not robot faces a wall.
        """
        return self.grid.robot_faces_wall()


class Robot:
    def __init__(self, sensor):
        self.sensor = sensor
        self.x_guess, self.y_guess = 0, 0

    def guess_move(self):
        print "Robot thinks it's in: ", self.sensor.sense_location()


class Direction:
    NORTH, EAST, SOUTH, WEST = range(4)

    def __init__(self):
        pass

    @classmethod
    def random(cls, exempt_dir=None):
        dirs = [cls.NORTH, cls.EAST, cls.SOUTH, cls.WEST]
        if exempt_dir:
            dirs.remove(exempt_dir)
            return dirs[random.randint(0, 2)]
        else:
            return dirs[random.randint(0, 3)]