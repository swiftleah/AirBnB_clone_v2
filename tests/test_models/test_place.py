#!/usr/bin/python3
""" Unittest """

from datetime import datetime
from models.base_model import BaseModel
import unittest
import os
import json


CustomPlace = custom_place.CustomPlace


class TestPlace(unittest.TestCase):
    """ unittesting for place.py """
    def setUp(self):
        self.value = BaseModel
        self.name = 'BaseModel'
        self.test_file = 'file.json'

    def tearDown(self):
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

    def test_default(self):
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        i = self.value()
        i.save()
        key = f"{self.name}.{i.id}"
        with open(self.test_file, 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        i = self.value()
        self.assertEqual(str(i), f"[{self.name}] ({i.id}) {i.__dict__}")

    def test_todict(self):
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

if __name__ == '__main__':
    unittest.main()
