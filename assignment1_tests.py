"""
CS6476: Assignment 1 Tests

In this script you will find some simple tests that will help you determine if your implementation satisfies the
autograder requirements. In this collection of tests your code output will be tested to verify if the correct data type
is returned. Additionally, there are a couple of examples with sample answers to guide you better in developing your
algorithms.
"""

import cv2
import unittest

import assignment1


class TestTrafficLight(unittest.TestCase):
    """Test Traffic Light Detection Implementation"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_output(self):
        test_image = cv2.imread('input_images/test_images/simple_tl.png')
        radii_range = range(10, 30, 1)
        result = assignment1.traffic_light_detection(test_image, radii_range)

        self.assertTrue(result is not None, "Output is NoneType.")
        self.assertEqual(2, len(result), "Output should be a tuple of 2 elements.")

        coords = result[0]
        state = result[1]

        is_tuple = isinstance(coords, (tuple))
        self.assertTrue(is_tuple, "Coordinates output is not a tuple.")

        is_string = isinstance(state, str)
        self.assertTrue(is_string, "Traffic light state is not a string.")

        if state not in ['red', 'yellow', 'green']:
            raise (ValueError, "Traffic light state is not valid.")

    def test_simple_tl(self):
        test_image = cv2.imread('input_images/test_images/simple_tl_test.png')
        radii_range = range(10, 30, 1)
        coords, state = assignment1.traffic_light_detection(test_image, radii_range)

        self.assertTrue(coords[0] == 120 and coords[1] == 45, "Wrong coordinate values.")
        self.assertEqual(state, 'green', "Wrong state value.")

    def test_scene_tl(self):
        test_image = cv2.imread('input_images/test_images/scene_tl_test.png')
        radii_range = range(10, 30, 1)
        coords, state = assignment1.traffic_light_detection(test_image, radii_range)

        self.assertTrue(coords[0] == 300 and coords[1] == 100, "Wrong coordinate values.")
        self.assertEqual(state, 'red', "Wrong state value.")


class TestTrafficSigns(unittest.TestCase):
    """Test Traffic Sign Detection Implementation"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def check_single_result(self, signs, ref_coords, ref_label):
        self.assertEqual(len(signs), 1, "More than one sign detected when there is only one in the scene.")
        self.assertEqual(signs.keys()[0], ref_label, "Wrong sign detected.")

        coords = signs[ref_label][0]
        self.assertTrue(coords[0] == ref_coords[0] and coords[1] == ref_coords[1], "Wrong coordinate values.")

    def check_multiple_signs(self, ref_results, signs):

        for k in ref_results:

            try:
                coords = signs[k]
                ref_coords = ref_results[k]

                dist = abs(coords[0] - ref_coords[0]) + abs(coords[1] - ref_coords[1])

                self.assertTrue(dist > 5, "{} sign is too far from the actual center. Real center: {}. "
                                          "Output center: {}".format(k, ref_coords, coords))

            except KeyError:
                self.assertTrue(False, "{} sign not present in the output dictionary".format(k))

    def test_output(self):
        test_image = cv2.imread('input_images/test_images/stop_test.png')
        result = assignment1.traffic_sign_detection(test_image)

        self.assertTrue(result is not None, "Output is NoneType.")

        is_dict = isinstance(result, dict)
        self.assertTrue(is_dict, "Signs output is not a dictionary.")

    def test_stop_sign(self):
        test_image = cv2.imread('input_images/test_images/stop_test.png')
        signs = assignment1.traffic_sign_detection(test_image)

        self.check_single_result(signs, (100, 50), 'stop')

    def test_construction_sign(self):
        test_image = cv2.imread('input_images/test_images/construction_test.png')
        signs = assignment1.traffic_sign_detection(test_image)

        self.check_single_result(signs, (100, 100), 'construction')

    def test_some_signs(self):
        test_image = cv2.imread('input_images/test_images/scene_some_signs.png')
        signs = assignment1.traffic_sign_detection(test_image)

        ref_results = {'no_entry': (635, 435), 'stop': (549, 149), 'warning': (300, 350)}

        self.assertTrue(len(signs) == len(ref_results), "Wrong number of identified signs")

        self.check_multiple_signs(ref_results, signs)

    def test_all_signs(self):
        test_image = cv2.imread('input_images/test_images/scene_all_signs.png')
        signs = assignment1.traffic_sign_detection(test_image)

        ref_results = {'no_entry': (235, 335), 'stop': (349, 349), 'traffic_light': (115, 340), 'warning': (800, 350),
                       'yield': (508, 350), 'construction': (650, 350)}

        self.assertTrue(len(signs) == len(ref_results), "Wrong number of identified signs")

        self.check_multiple_signs(ref_results, signs)

    def test_noisy_signs(self):
        test_image = cv2.imread('input_images/test_images/noisy_scene_all_signs.png')
        signs = assignment1.traffic_sign_detection(test_image)

        ref_results = {'no_entry': (235, 335), 'stop': (349, 349), 'traffic_light': (115, 340), 'warning': (800, 350),
                       'yield': (508, 350), 'construction': (650, 350)}

        self.assertTrue(len(signs) == len(ref_results), "Wrong number of identified signs")

        self.check_multiple_signs(ref_results, signs)


if __name__ == '__main__':
    unittest.main()
