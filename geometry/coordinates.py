# -*- coding: utf-8 -*-
"""Coordinates Direction and Orientation.

Manages coordinates definition (geometrically).

Attributes:
    None

TODO:

"""
from enum import unique, Enum, auto


@unique
class CoordinatesDirection(Enum):
    """
    How are coordinates on the screen?
    """
    SCREEN_DIRECTION = auto() # Y grows from top to bottom
    ANTI_SCREEN_DIRECTION = auto() # Y grows from bottom to top
