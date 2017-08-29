"""
CS6476: Assignment 1 Experiment file

This script contains a series of function calls that run your ps2 implementation
and output images so you can verify your results.
"""


import cv2

import ps2


def draw_tl_center(image_in, center, state):
    """ Marks the center of a traffic light image and adds coordinates with the
    state of the current image

    Use OpenCV drawing functions to place a marker that represents the traffic
    light center. Additionally, place text using OpenCV tools that show the
    numerical and string values of the traffic light center and state. Use the
    following format:

        ((x-coordinate, y-coordinate), 'color')

    See OpenCV's drawing functions:
    http://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html

    Make sure the font size is large enough so that the text in the output image
    is legible.
    Args:
        image_in (numpy.array): input image.
        center (tuple): center numeric values.
        state (str): traffic light state values can be: 'red', 'yellow', 'green'.

    Returns:
        numpy.array: output image showing a marker representing the traffic
        light center and text that presents the numerical coordinates with
        the traffic light state.
    """
    pass


def mark_traffic_signs(signs_dict):
    """Marks the center of a traffic sign adding

    Args:
        signs_dict (dict): dictionary containing the coordinates of each sign
        found in a scene.

    Returns:
        numpy.array: output image showing markers on each traffic sign.

    """
    pass


def part_1a():

    # Start by loading a simple image with one traffic sign on a white
    # background.
    simple_tl = cv2.imread("input_images/simple_tl.png")

    # Define a radii range, you may define a smaller range based on your observations.
    radii_range = range(20, 40, 1)

    coords, state = ps2.traffic_light_detection(simple_tl, radii_range)

    simple_tl_output = draw_tl_center(simple_tl, coords, state)

    # Now let's save the output image. Use it to verify your results
    cv2.imwrite("output/simple_tl.png", simple_tl_output)


def part_1b():

    # Scene 1
    # Load a more complex scene
    scene_tl_1 = cv2.imread("input_images/scene_tl_1.png")

    # Radii range used by the autograder
    radii_range = range(20, 40, 1)

    coords, state = ps2.traffic_light_detection(scene_tl_1, radii_range)

    scene_tl_1_output = draw_tl_center(scene_tl_1, coords, state)

    cv2.imwrite("output/scene_tl_1.png", scene_tl_1_output)

    # Scene 2
    scene_tl_2 = cv2.imread("input_images/scene_tl_2.png")

    radii_range = range(20, 40, 1)

    coords, state = ps2.traffic_light_detection(scene_tl_2, radii_range)

    scene_tl_2_output = draw_tl_center(scene_tl_2, coords, state)

    cv2.imwrite("output/scene_tl_2.png", scene_tl_2_output)


def part_2a():

    scene_some_signs = cv2.imread("input_images/scene_some_signs.png")

    signs = ps2.traffic_sign_detection(scene_some_signs)

    scene_some_signs_output = mark_traffic_signs(signs)

    cv2.imwrite("output/scene_some_signs.png", scene_some_signs_output)


def part_2b():
    scene_all_signs = cv2.imread("input_images/scene_all_signs.png")

    signs = ps2.traffic_sign_detection(scene_all_signs)

    scene_all_signs_output = mark_traffic_signs(signs)

    cv2.imwrite("output/scene_all_signs.png", scene_all_signs_output)


def part_3():
    noisy_scene_all_signs = cv2.imread("input_images/noisy_scene_all_signs.png")

    signs = ps2.traffic_sign_detection(noisy_scene_all_signs)

    noisy_scene_all_signs_output = mark_traffic_signs(signs)

    cv2.imwrite("output/noisy_scene_all_signs.png", noisy_scene_all_signs_output)
