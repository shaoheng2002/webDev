"""
CS6476 Assignment 1 imports. Only Numpy and cv2 are allowed.
"""
import cv2
import numpy as np


def traffic_light_detection(img_in, radii_range):
    """Finds the coordinates of a traffic light image given a radii range.

    Use the radii range to find the circles in the traffic light and identify which of them represents the yellow light.

    Analyze the states of all three lights and determine whether the traffic light is red, yellow, or green. This will
    be referred to as the 'state'.

    It is recommended you use Hough tools to find these circles in the image.

    The input image may be just the traffic light with a white background or a larger image of a scene containing a
    traffic light.

    Args:
        img_in (numpy.array): image containing a traffic light.
        radii_range (list): range of radii values to search for.

    Returns:
        tuple: 2-element tuple containing:
               coordinates (tuple): traffic light center using the (x, y) convention.
               state (str): traffic light state. A value in {'red', 'yellow', 'green'}
    """

    raise NotImplementedError


def traffic_sign_detection(img_in):
    """Finds all traffic signs in a given image.

    The image may contain at least one of the following:
    - traffic_light
    - no_entry
    - stop
    - warning
    - yield
    - construction

    Use these names for your output. See the instructions document for a visual definition of each sign.

    Args:
        img_in (numpy.array): input image containing at least one traffic sign.

    Returns:
        dict: dictionary containing only the signs present in the image along with their respective coordinates as
              tuples. For example: {'stop': [(1, 3)], 'yield': (4, 11)} These are just example values and may not
              represent a valid scene.
    """

    raise NotImplementedError
