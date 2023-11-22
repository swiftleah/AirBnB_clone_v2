#!/usr/bin/python3
""" Unittesting for amenity """

from datetime import datetime
import inspect
import models
from models import amenity
from models.base_model import BaseModel
import pep8
import unittest
CustomAmenity = amenity.Amenity


class TestAmenity(unittest.TestCase):
    """Tests for amenity.py"""
    def test_amenity_init(self):
        """ initialization """
        amenity = Amenity(name="Test Amenity")
        self.assertEqual(amenity.name, "Test Amenity")

    def test_amenity_no_args(self):
        """ initialization with no args """
         amenity = Amenity()
         self.assertEqual(amenity.name, "")

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

if __name__ == '__main__':
    unittest.main()
