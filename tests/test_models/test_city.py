#!/usr/bin/python3
"""TestCustomCityDocs classes"""

from datetime import datetime
import inspect
import models
from models import custom_city
from models.base_model import BaseModel
import pep8
import unittest
CustomCity = custom_city.CustomCity


class TestCustomCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of CustomCity class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.custom_city_f = inspect.getmembers(CustomCity, inspect.isfunction)

    def test_pep8_conformance_custom_city(self):
        """Test that models/custom_city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/custom_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_custom_city(self):
        """Test that tests/test_models/test_custom_city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_custom_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_custom_city_module_docstring(self):
        """Test for the custom_city.py module docstring"""
        self.assertIsNot(custom_city.__doc__, None,
                         "custom_city.py needs a docstring")
        self.assertTrue(len(custom_city.__doc__) >= 1,
                        "custom_city.py needs a docstring")

    def test_custom_city_class_docstring(self):
        """Test for the CustomCity class docstring"""
        self.assertIsNot(CustomCity.__doc__, None,
                         "CustomCity class needs a docstring")
        self.assertTrue(len(CustomCity.__doc__) >= 1,
                        "CustomCity class needs a docstring")

    def test_custom_city_func_docstrings(self):
        """Test for the presence of docstrings in CustomCity methods"""
        for func in self.custom_city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCustomCity(unittest.TestCase):
    """Test the CustomCity class"""
    def test_is_subclass(self):
        """Test that CustomCity is a subclass of BaseModel"""
        custom_city = CustomCity()
        self.assertIsInstance(custom_city, BaseModel)
        self.assertTrue(hasattr(custom_city, "id"))
        self.assertTrue(hasattr(custom_city, "created_at"))
        self.assertTrue(hasattr(custom_city, "updated_at"))

    def test_name_attr(self):
        """Test that CustomCity has attribute name, and it's an empty string"""
        custom_city = CustomCity()
        self.assertTrue(hasattr(custom_city, "name"))
        if models.switch == 'db':
            self.assertEqual(custom_city.name, None)
        else:
            self.assertEqual(custom_city.name, "")

    def test_state_id_attr(self):
        """Test that CustomCity has attribute state_id, and it's an empty string"""
        custom_city = CustomCity()
        self.assertTrue(hasattr(custom_city, "state_id"))
        if models.switch == 'db':
            self.assertEqual(custom_city.state_id, None)
        else:
            self.assertEqual(custom_city.state_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        c = CustomCity()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in c.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = CustomCity()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "CustomCity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        custom_city = CustomCity()
        string = "[CustomCity] ({}) {}".format(custom_city.id, custom_city.__dict__)
        self.assertEqual(string, str(custom_city))
