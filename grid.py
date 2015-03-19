import random

from robot import Direction


class Grid:
    robot = None

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.robot_location = random.randint(0, width - 1), random.randint(0, height - 1)
        self.robot_dir = Direction.random()

    def robot_adj_location(self):
        x, y = self.robot_location

        l_s = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
               (x + 1, y + 1)]

        adj = l_s[random.randint(0, 7)]

        # wall check
        if adj[0] >= self.width or adj[1] >= self.height or adj[0] < 0 or adj[1] < 0:
            return None
        else:
            return adj

    def robot_adj2_location(self):
        x, y = self.robot_location

        ls_2 = [(x - 2, y - 2), (x - 2, y - 1), (x - 2, y), (x - 2, y + 1), (x - 2, y + 2), (x - 1, y - 2),
                (x - 1, y + 2), (x, y - 2), (x, y + 2), (x + 1, y - 2), (x + 1, y + 2), (x + 2, y - 2), (x + 2, y - 1),
                (x + 2, y), (x + 2, y + 1), (x + 2, y + 2)]

        adj = ls_2[random.randint(0, 15)]

        # wall check
        if adj[0] >= self.width or adj[1] >= self.height or adj[0] < 0 or adj[1] < 0:
            return None
        else:
            return adj

    def robot_faces_wall(self):
        x, y = self.robot_location

        # NORTH, EAST, SOUTH, WEST
        next_locations = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        next_coord = next_locations[self.robot_dir]
        if next_coord[0] >= self.width or next_coord[1] >= self.height or next_coord[0] < 0 or next_coord[1] < 0:
            return True
        else:
            return False

    def move_robot(self):
        rand = random.random()

        if rand <= 0.3:
            self.robot_dir = Direction.random(self.robot_dir)
        while self.robot_faces_wall():
            self.robot_dir = Direction.random(self.robot_dir)

        x, y = self.robot_location

        # NORTH, EAST, SOUTH, WEST
        next_locations = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        self.robot_location = next_locations[self.robot_dir]