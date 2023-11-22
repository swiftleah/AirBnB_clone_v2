#!/usr/bin/python3
"""TestCustomPlaceDocs classes"""

from datetime import datetime
import inspect
import models
from models import custom_place
from models.base_model import BaseModel
import pep8
import unittest
CustomPlace = custom_place.CustomPlace


class TestCustomPlaceDocs(unittest.TestCase):
    """Tests to check the documentation and style of CustomPlace class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.custom_place_f = inspect.getmembers(CustomPlace, inspect.isfunction)

    def test_pep8_conformance_custom_place(self):
        """Test that models/custom_place.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/custom_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_custom_place(self):
        """Test that tests/test_models/test_custom_place.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_custom_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_custom_place_module_docstring(self):
        """Test for the custom_place.py module docstring"""
        self.assertIsNot(custom_place.__doc__, None,
                         "custom_place.py needs a docstring")
        self.assertTrue(len(custom_place.__doc__) >= 1,
                        "custom_place.py needs a docstring")

    def test_custom_place_class_docstring(self):
        """Test for the CustomPlace class docstring"""
        self.assertIsNot(CustomPlace.__doc__, None,
                         "CustomPlace class needs a docstring")
        self.assertTrue(len(CustomPlace.__doc__) >= 1,
                        "CustomPlace class needs a docstring")

    def test_custom_place_func_docstrings(self):
        """Test for the presence of docstrings in CustomPlace methods"""
        for func in self.custom_place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCustomPlace(unittest.TestCase):
    """Test the CustomPlace class"""
    def test_is_subclass(self):
        """Test that CustomPlace is a subclass of BaseModel"""
        custom_place = CustomPlace()
        self.assertIsInstance(custom_place, BaseModel)
        self.assertTrue(hasattr(custom_place, "id"))
        self.assertTrue(hasattr(custom_place, "created_at"))
        self.assertTrue(hasattr(custom_place, "updated_at"))

    def test_city_id_attr(self):
        """Test CustomPlace has attr city_id, and it's an empty string"""
        custom_place = CustomPlace()
        self.assertTrue(hasattr(custom_place, "city_id"))
        if models.switch == 'db':
            self.assertEqual(custom_place.city_id, None)
        else:
            self.assertEqual(custom_place.city_id, "")

    def test_user_id_attr(self):
        """Test CustomPlace has attr user_id, and it's an empty string"""
        custom_place = CustomPlace()
        self.assertTrue(hasattr(custom_place, "user_id"))
        if models.switch == 'db':
            self.assertEqual(custom_place.user_id, None)
        else:
            self.assertEqual(custom_place.user_id, "")

    def test_name_attr(self):
        """Test CustomPlace has attr name, and it's an empty string"""
        custom_place = CustomPlace()
        self.assertTrue(hasattr(custom_place, "name"))
        if models.switch == 'db':
            self.assertEqual(custom_place.name, None)
        else:
            self.assertEqual(custom_place.name, "")

    def test_description_attr(self):
        """Test CustomPlace has attr description, and it's an empty string"""
        custom_place = CustomPlace()
        self.assertTrue(hasattr(custom_place, "description"))
        if models.switch == 'db':
            self.assertEqual(custom_place.description, None)
        else:
            self.assertEqual(custom_place.description, "")

    def test_number_rooms_attr(self):
        """Test CustomPlace has attr number_rooms, and it's an int == 0"""
        custom_place = CustomPlace()
        self.assertTrue(hasattr(custom_place, "number_rooms"))
        if models.switch == 'db':
            self.assertEqual(custom_place.number_rooms, None)
        else:
            self.assertEqual(type(custom_place.number_rooms), int)
            self.assertEqual(custom_place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test CustomPlace has attr number_bathrooms, and it's an int == 0"""
        custom_place = CustomPlace()
        self.assertTrue(hasattr(custom_place, "number_bathrooms"))
        if models.switch == 'db':
            self.assertEqual(custom_place.number_bathrooms, None)
        else:
            self.assertEqual(type(custom_place.number_bathrooms), int)
            self.assertEqual(custom_place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test CustomPlace has attr max_guest, and it's an int == 0"""
        custom_place = CustomPlace()
        self.assertTrue(hasattr(custom_place, "max_guest"))
        if models.switch == 'db':
            self.assertEqual(custom_place.max_guest, None)
        else:
            self.assertEqual(type(custom_place.max_guest), int)
            self.assertEqual(custom_place.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test CustomPlace has attr price_by_night, and it's an int == 0"""
        custom_place = CustomPlace()
        self.assertTrue(hasattr(custom_place, "price_by_night"))
        if models.switch == 'db':
            self.assertEqual(custom_place.price_by_night, None)
        else:
            self.assertEqual(type(custom_place.price_by_night), int)
            self.assertEqual(custom_place.price_by_night, 0)

    def test_latitude_attr(self):
        """Test CustomPlace has attr latitude, and it's a float == 0.0"""
        custom_place = CustomPlace()
        self.assertTrue(hasattr(custom_place, "latitude"))
        if models.switch == 'db':
            self.assertEqual(custom_place.latitude, None)
        else:
            self.assertEqual(type(custom_place.latitude), float)
            self.assertEqual(custom_place.latitude, 0.0)

    def test_longitude_attr(self):
        """Test CustomPlace has attr longitude, and it's a float == 0.0"""
        custom_place = CustomPlace()
        self.assertTrue(hasattr(custom_place, "longitude"))
        if models.switch == 'db':
            self.assertEqual(custom_place.longitude, None)
        else:
            self.assertEqual(type(custom_place.longitude), float)
            self.assertEqual(custom_place.longitude, 0.0)

    @unittest.skipIf(models.switch == 'db', "not testing File Storage")
    def test_amenity_ids_attr(self):
        """Test CustomPlace has attr amenity_ids, and it's an empty list"""
        custom_place = CustomPlace()
        self.assertTrue(hasattr(custom_place, "amenity_ids"))
        self.assertEqual(type(custom_place.amenity_ids), list)
        self.assertEqual(len(custom_place.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        p = CustomPlace()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = CustomPlace()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "CustomPlace")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        custom_place = CustomPlace()
        string = "[CustomPlace] ({}) {}".format(custom_place.id, custom_place.__dict__)
        self.assertEqual(string, str(custom_place))
