#!/usr/bin/python3
""" Unittesting """


import unittest
from models.review import review


class TestReview(unittest.TestCase):
    """ unittests for review.py """
    def setUp(self):
        self.review = Review()
        self.name = "User"
        self.value = User

    def test_review_init(self):
        """ """
        self.assertIsInstance(self.review, Review)

    def test_review_attributes(self):
        """ """
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

     def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)
