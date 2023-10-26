#!/usr/bin/python3
""" documentation """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ documentation """

    def __init__(self, *args, **kwargs):
        """ documentation """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ documentation """
        new = self.value()
        self.assertEqual(type(new.name), str)
