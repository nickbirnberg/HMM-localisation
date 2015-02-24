import random


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.robotLocation = self.random_location()

    def get_adj_location(self, location_id):
        """

        :param location_id: Corresponds to specific locations adjacent to robot:
        [0:8]: {(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)}
        [9:25]:  {(x-2, y-2), (x-2, y-1), (x-2, y), (x-2, y+1), (x-2, y+2), (x-1, y-2), (x-1, y+2), (x, y-2), (x, y+2),
                  (x+1, y-2), (x+1, y+2), (x+2, y-2), (x+2, y-1), (x+2, y), (x+2, y+1), (x+2, y+2)}
        :return: coords of location
        """
        pass

    def random_location(self):
        """
        Gives a random valid location on grid.
        :return: tuple containing (x, y) of grid
        """
        return random.randint(0, self.width), random.randint(0, self.height)
