# ```
# test-soc01h-cc-daniella-dsouza.py
# ```
# Author : Daniella D'Souza
# Created : August 9th , 2018
# 1MWTT Week 1 Hackathon
#
# Add Unit Tests
# Last Updated - 08/09/18
# Dimension Continents Location Time (seconds)
# 11x11       1         8,8     0.015623807907104492
# 172x172     359       98,98   50.818121910095215
# 270x270     838       3,3     313.4123659133911

import unittest
import random
import time

from soc01h_cc_daniella_dsouza import Civilization

class TestCivilization(unittest.TestCase):
    """Tests for the class Civilization"""
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("{}: {}".format(self.id(), t))

    def test_11_by_11_continent(self):
        my_civilization = Civilization(11)
        print("Civilization dimensions 11 x 11")
        return_value = my_civilization.find_random_location()
        self.assertEqual(True, return_value)

    def test_n_by_n_continent(self):
        dimension = random.randrange(0, 300)
        print("\nCivilization dimension {} x {}".format(dimension, dimension))
        my_civilization = Civilization(dimension)
        return_value = my_civilization.find_random_location()
        self.assertEqual(True, return_value)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCivilization)
    unittest.TextTestRunner(verbosity=1).run(suite)
              

              


