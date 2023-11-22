#!/usr/bin/python3
"""TestCustomClassDocs classes"""

from datetime import datetime
import inspect
import models
from models import amenity
from models.base_model import BaseModel
import pep8
import unittest
CustomAmenity = amenity.Amenity


class TestCustomAmenityDocs(unittest.TestCase):
    """Tests to check the documentation and style of CustomAmenity class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.custom_amenity_f = inspect.getmembers(CustomAmenity, inspect.isfunction)

    def test_pep8_conformance_custom_amenity(self):
        """Test that models/amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_custom_amenity(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_custom_amenity_module_docstring(self):
        """Test for the amenity.py module docstring"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_custom_amenity_class_docstring(self):
        """Test for the CustomAmenity class docstring"""
        self.assertIsNot(CustomAmenity.__doc__, None,
                         "CustomAmenity class needs a docstring")
        self.assertTrue(len(CustomAmenity.__doc__) >= 1,
                        "CustomAmenity class needs a docstring")

    def test_custom_amenity_func_docstrings(self):
        """Test for the presence of docstrings in CustomAmenity methods"""
        for func in self.custom_amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCustomAmenity(unittest.TestCase):
    """Test the CustomAmenity class"""
    def test_is_subclass(self):
        """Test that CustomAmenity is a subclass of BaseModel"""
        custom_amenity = CustomAmenity()
        self.assertIsInstance(custom_amenity, BaseModel)
        self.assertTrue(hasattr(custom_amenity, "id"))
        self.assertTrue(hasattr(custom_amenity, "created_at"))
        self.assertTrue(hasattr(custom_amenity, "updated_at"))

    def test_custom_name_attr(self):
        """Test that CustomAmenity has attribute custom_name, and it's as an empty string"""
        custom_amenity = CustomAmenity()
        self.assertTrue(hasattr(custom_amenity, "custom_name"))
        if models.switch == 'db':
            self.assertEqual(custom_amenity.custom_name, None)
        else:
            self.assertEqual(custom_amenity.custom_name, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        custom_amenity = CustomAmenity()
        print(custom_amenity.__dict__)
        new_d = custom_amenity.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in custom_amenity.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        custom_amenity = CustomAmenity()
        new_d = custom_amenity.to_dict()
        self.assertEqual(new_d["__class__"], "CustomAmenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], custom_amenity.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], custom_amenity.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        custom_amenity = CustomAmenity()
        string = "[CustomAmenity] ({}) {}".format(custom_amenity.id, custom_amenity.__dict__)
        self.assertEqual(string, str(custom_amenity))
