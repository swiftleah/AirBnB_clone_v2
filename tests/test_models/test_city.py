#!/usr/bin/python3
"""TestCustomCityDocs classes"""

from datetime import datetime
import inspect
import models
from models import custom_city
from models.base_model import BaseModel
import unittest

class TestCustomCity(unittest.TestCase):
    """Test the CustomCity class"""
    def test_city_init(self):
        """ tests initialization """
        city = City(state_id="state_1", name="Test City")
        self.assertEqual(city.state_id, "state_1")
        self.assertEqual(city.name, "Test City")

    def test_city_defaults(self):
        """ tests initialization with no args """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_relationship(self):
        """ tests relationship with 'places' """
        place = City().places.filter_by(some_property="some_value").first()
        self.assertIsNone(place)

    def test_str(self):
        """test that the str method has the correct output"""
        custom_city = CustomCity()
        string = "[CustomCity] ({}) {}".format(custom_city.id, custom_city.__dict__)
        self.assertEqual(string, str(custom_city))

if __name__ == '__main__':
    unittest.main()
