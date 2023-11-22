#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest


class test_state(unittest.TestCase):
    """ """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_str(self):
        """ """
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(State()))

    def test_name(self):
        """ """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        if models.switch == 'db':
            self.assertEqual(state.name, None)
        else:
            self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
