#!/usr/bin/python3
""" document documt """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ documentation """

    def __init__(self, *args, **kwargs):
        """ documentation """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ documentation """
        new = self.value()
        self.assertEqual(type(new.name), str)
