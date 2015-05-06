from time import sleep

from grid import Grid
from hmm import HMM
from robot import Robot, Sensor


def start_robot(size):
    """
    Sets up the world and robot and enters endless loop of guessing.
    :param size:
    """
    # create grid that contains world state
    grid = Grid(size.width, size.height)
    # create sensor, which queries the grid
    sensor = Sensor(grid)
    # create robot, which guesses location based on sensor
    hmm = HMM(size.width, size.height)
    robot = Robot(sensor, hmm)

    moves = 0
    guessed_right = 0
    while True:
        # move robot
        grid.move_robot()
        moves += 1
        print "\nRobot is in: ", grid.robot_location
        guessed_move, probability = robot.guess_move()
        if guessed_move == grid.robot_location:
            guessed_right += 1
        man_distance = abs(guessed_move[0] - grid.robot_location[0]) + abs(guessed_move[1] - grid.robot_location[1])
        print "Manhattan distance: ", man_distance
        print "Robot has been correct:", float(guessed_right) / moves, "of the time."
        if probability == 1.0:
            print "Took robot", moves, " moves to be 100% accurate."
            break
        sleep(1)

if __name__ == '__main__':
    """
    The main function called when main.py is run from the command line.

    Example usage:
    > python main.py --width 10 --height 10
    First argument defines the width of the grid, second, the height.
    """
    # handle arguments
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--height", type=int, required=True)
    args = parser.parse_args()
    if args.width <= 1 or args.height <= 1:
        raise argparse.ArgumentTypeError("Values must be greater than one.")
    #
    start_robot(args)