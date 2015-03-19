from grid import Grid
from robot import Robot, Sensor
from time import sleep


def start_robot(size):
    # create grid that contains world state
    grid = Grid(size.width, size.height)
    # create sensor, which queries the grid
    sensor = Sensor(grid)
    # create robot, which guesses location based on sensor
    robot = Robot(sensor)
    # adds robot to grid to give access to robot's direction
    grid.add_robot(robot)
    while True:
        # move robot
        grid.move_robot()
        print "Robot is in: ", grid.robot_location
        robot.guess_move()
        sleep(1)


if __name__ == '__main__':
    """
    The main function called when localisation.py is run from the command line.

    Example usage:
    > python localisation.py --width 10 --height 10
    First argument defines the width of the grid, second, the height.
    """
    # handle arguments
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--height", type=int, required=True)
    args = parser.parse_args()
    if args.width <= 0 or args.height <= 0:
        raise argparse.ArgumentTypeError("Values must be greater than zero.")
    #
    start_robot(args)