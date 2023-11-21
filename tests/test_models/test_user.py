#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, class_mapper
from models.base_model import Base


class test_User(unittest.TestCase):
    """ """

    def test_attributes(self):
        """ tests attributes of user """
        user = User(email='test@example.com', password='pswd123')
        user.first_name = 'John'
        user.last_name = 'Smith'
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'pswd123')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Smith')

    def test_table_name(self):
        """ tests that __tablename__ is 'users' """
        self.assertEqual(User.__tablename__, 'users')

    def test_nullable(self):
        """ tests that user names are nullable """
        user = User(email='johnsmith@gmail.com', password='12345')
        self.assertIsNone(user.first_name)
        self.assertIsNone(user.last_name)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ tests that attribute first_name is of type String """
        first_name = class_mapper(User).mapped_table.columns['first_name']
        self.assertIsInstance(first_name.type, String)

    def test_last_name(self):
        """ tests that attribute last_name is of type String """
        last_name = class_mapper(User).mapped_table.columns['last_name']
        self.assertIsInstance(last_name.type, String)

    def test_email(self):
        """ """
        email_column = class_mapper(User).mapped_table.columns['email']
        self.assertIsInstance(email_column.type, String)

    def test_password(self):
        """ tests the password attribute is type String """
        password_column = class_mapper(User).mapped_table.columns['password']
        self.assertIsInstance(password_column.type, String)


if __name__ == '__main__':
    unittest.main()
