#!/usr/bin/env python 
"""These classes are designed to support a simplified version of the
RoboRally game.  Robots are programmed with cards, then the robots
take turns executing their cards.

Author: Nathan Sprague and Matt Bowyer
Version: 1.0

"""

import collections

class Robot(object):
    """Robots have a position and a heading.  The x and y coordinates are
    integer grid positions. The heading is in degrees with four
    possible values:

    0 - Pointing East, toward increasing x
    90 - Poiting North, toward increasing y
    180 - Pointing West, toward decreasing x
    270 - Poiting South, toward decreasing y

    Robots also have set of "registers" (represented as a deque) that
    store a sequence of control cards.

    """
    def __init__(self, name, x, y, heading=90):
        """ Instantiate a Robot """
        self.name = name
        self.x = x
        self.y = y
        self.heading = heading
        self.registers = collections.deque()

    def add_card(self, card):
        """Add a new card to the instructions for this robot.  Cards will be
        executed in the order they are added.

        """
        self.registers.appendleft(card)

    def __str__(self):
        """String representation of the robot"""
        return "<Robot name:{}, x:{}, y:{}, heading:{}>".format(self.name,
                                                                self.x,
                                                                self.y,
                                                                self.heading)
class Card(object):
    """A card defining a single robot action. Priority determines
    which robot moves first on a turn (higher priority wins)

    Possible movement commands are:

    'F' - Forward
    'L' - Turn left 90 degrees
    'R' - Turn Right 90 degrees

    The 'F' command must include an integer distance indicating how
    many steps to move.  The distance value will be ignored for the
    'L' and 'R' commands.

    """

    def __init__(self, priority, command, distance=0):
        """ Instantiate a Card. """
        self.priority = priority
        self.command = command
        self.distance = distance

    def __str__(self):
        """ String representation of a Card."""
        if self.command == "F":
            result = "<Card priority: {} command:{}, distance:{}>"
            return result.format(self.priority, self.command, self.distance)
        else:
            result = "<Card priority: {} command:{}>"
            return result.format(self.priority, self.command)


class RoboRally(object):
    """This class handles the movement and interaction logic for the
    RoboRally game.

    """

    def __init__(self):
        """ Instantiate a game instance with no robots. """
        # UNFINISHED
        self.robots = []  # list of robots in game
        self.robot_cards = {}  # dict maps from robots to their given cards
        pass

    def add_robot(self, robot):
        """ Add a robot to the game. """
        # UNFINISHED
        self.robots.append(robot)
        pass

    def run(self):
        """Play all robot cards.  After this method executes all Robots will
        be in their correct final positions and all 'hands' will be
        empty.  Robots need not begin with the same number of cards.
        If a robot runs out of cards it will remain stationary in
        subsequent rounds (unless it is pushed by another robot).

        """
        # UNFINISHED
        pass
