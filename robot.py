import random


class Robot:
    # Settings for robot sensor.
    L = 0.1
    L_s = 0.05
    L_s2 = 0.025
    detects_nothing = 0.1

    # Settings for robot direction.
    # P( h_t+1 = h_t | not encountering a wall) = 0.7
    # P( h_t+1 != h_t | not encountering a wall) = 0.3
    dir_no_wall = 0.3
    # P( h_t+1 = h_t | encountering a wall) = 0.0
    # P( h_t+1 != h_t | encountering a wall) = 1.0
    dir_wall = 1.0

    def __init__(self, grid):
        self.grid = grid
        self.x, self.y = self.get_location()
        self.dir = self.random_dir()

    def get_location(self):
        if random.random() >= self.detects_nothing:
            if random.random() < self.L:
                return self.grid.robotLocation

            first_surrounding = []
            for i in range(0, 8):
                if random.random() <= self.L_s:
                    first_surrounding.append(self.grid.get_adj_location(i))
                else:
                    first_surrounding.append((-1, -1))
            second_surrounding = []
            for i in range(9, 25):
                if random.random() <= self.L_s2:
                    first_surrounding.append(self.grid.get_adj_location(i))
                else:
                    first_surrounding.append((-1, -1))
            return self.guess_location(first_surrounding, second_surrounding)

        else:
            return self.guess_location()

    def random_dir(self):
        """
        :return: new random direction different from current
        """
        rand_dir = random.randint(1, 4)
        while rand_dir == self.dir:
            rand_dir = random.randint(1, 4)
        return dir

    def move(self):
        pass

    def guess_location(self, first_surrounding=None, second_surrounding=None):
        """

        :param first_surrounding: list of locations immediately adjacent
               second_surrounding: list of locations two away
        :return: robot's best guessed location
        """
        # Case if nothing is detected.
        if first_surrounding is None or second_surrounding is None:
            if self.x and self.y:
                if self.dir == Direction.NORTH:
                    return self.x, self.y + 1
                elif self.dir == Direction.EAST:
                    return self.x + 1, self.y
                elif self.dir == Direction.SOUTH:
                    return self.x, self.y - 1
                elif self.dir == Direction.WEST:
                    return self.x - 1, self.y
            else:
                return self.grid.random_location()
        return self.grid.random_location()


class Direction(object):
    NORTH, EAST, SOUTH, WEST = range(1, 4)