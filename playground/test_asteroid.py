import json
import unittest
from unittest.mock import patch

from asteroid import Asteroid


class TestAsteroid(unittest.TestCase):
    def setUp(self):
        self.asteroid = Asteroid(2099942)

    def mocked_get_data(self):
        with open('apophis_fixture.txt') as f:
            return json.loads(f.read())

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_name(self):
        self.assertEqual(self.asteroid.name, '99942 Apophis (2004 MN4)')

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_diameter(self):
        self.assertEqual(self.asteroid.diameter, 682)


"""(venv) >python -m unittest test_asteroid.py
Name: 99942 Apophis (2004 MN4)
Diameter: 682m
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
"""
