#!/usr/bin/python3
""" unittesting soncole.py
"""

import console
import inspect
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """Class for testing documentation of the console"""
    def setUp(self):
        """Set up the PEP8 StyleGuide object for testing"""
        self.pep8s = pep8.StyleGuide(quiet=True)

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """ testing module and HBNB command class docstrings """
        module_doc = console.__doc__
        class_doc = HBNBCommand.__doc__

        self.assertIsNot(module_doc, None,
                         "console.py needs a docstring")
        self.assertTrue(len(module_doc) >= 1,
                        "console.py needs a docstring")

        self.assertIsNot(class_doc, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(class_doc) >= 1,
                        "HBNBCommand class needs a docstring")
