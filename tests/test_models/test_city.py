#!/usr/bin/python3
""" """
import unittest
from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, class_mapper
from models.base_model import Base
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(unittest.TestCase):
    """ test cases for city.py """

    def test_table_name(self):
        """ test to see if __tablename__ is 'cities' """
        self.assertEqual(City.__tablename__, 'cities')

    @classmethod
    def teardownclass(cls):
        """ tests that session closes and all tables are dropped """
        cls.session.close_all()
        Base.metadata.drop_all(cls.engine)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ testing that state_id is of type String """
        state_id = class_mapper(City).mapped_table.columns['state_id']
        self.assertIsInstance(state_id.type, String)

    def test_name(self):
        """ tests that name is of type String """
        name = class_mapper(City).mapped_table.columns['name']
        self.assertIsInstance(name.type, String)

    def test_attributes(self):
        """ tests attributes for city """
        city = City(state_id='state_id_1', name='Canada')
        self.assertEqual(city.state_id, 'state_id_1')
        self.assertEqual(city.name, 'Canada')


if __name__ == '__main__':
    unittest.main()
