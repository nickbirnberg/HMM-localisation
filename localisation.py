from grid import Grid
from robot import Robot


def start_robot(size):
    # create grid that contains world state
    grid = Grid(size.width, size.height)
    # create robot, which queries the grid
    robot = Robot(grid)
    while True:
        print "Robot thinks it's in: ", robot.get_location()
        print "Robot is actually in: ", grid.robotLocation
        if robot.get_location() == grid.robotLocation():
            "Robot is correct!"
        robot.move()


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