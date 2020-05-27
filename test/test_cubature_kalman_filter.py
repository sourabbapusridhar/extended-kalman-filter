# Implementation of Unit Tests to Test Cubature Kalman Filter

import unittest
import numpy as np

import src.kalman_filter as kf
import src.motion_model as motmod
import src.generate_plots as plot
import src.measurement_model as measmod

class TestCubatureKalmanFilter(unittest.TestCase):
    """
    Class to perform Unit Tests on Cubature Kalman Filter
    
    """    
    def setUp(self):
        print("Setup Called")

    def tearDown(self):
        print("Tear Down Called")

    def test_1(self):
        print("Test 1 Called")

    def test_2(self):
        print("Test 1 Called")

    def test_3(self):
        print("Test 1 Called")