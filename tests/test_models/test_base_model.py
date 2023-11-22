#!/usr/bin/python3
""" Unittests """

from datetime import datetime
import inspect
import models
import pep8 as pycodestyle
import time
import unittest
from unittest import mock
CustomModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


class TestBaseModel(unittest.TestCase):
    """ unittests for base_model.py """
    def setUp(self):
        """ setting values for tests """
        self.base_model = BaseModel()
        self.name = 'BaseModel'
        self.test_file = 'file.json'

    def test_default(self):
        """ """
        i = self.base_model()
        self.assertEqual(type(i), self.base_model)

    def test_kwargs(self):
        """ """
        i = self.base_model()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_str(self):
        """ """
        i = self.base_model()
        self.assertEqual(str(i), f"[{self.name}] ({i.id}) {i.__dict__}")

    def test_todict(self):
        """ """
        i = self.base_model()
        self.assertEqual(type(i), self.base_model)

    def test_base_model_init(self):
        """ """
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertIsNotNone(self.base_model.id)

     def test_base_model_to_dict(self):
         """ """
         base_dict = self.base_model.to_dict()
         self.assertIsInstance(base_dict, dict)
         self.assertIn('__class__', base_dict)
         self.assertEqual(base_dict['__class__'], 'BaseModel')
         self.assertNotIn('_sa_instance_state', base_dict)
         self.assertIn('id', base_dict)
         self.assertIn('created_at', base_dict)
         self.assertIn('updated_at', base_dict)

if __name__ == '__main__':
    unittest.main()
