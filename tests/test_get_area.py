import unittest
from .. import persimmon

class PersimmonTest(unittest.TestCase):
    def setUp(self):
        self.field = [[1,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,1]]
    def test_minimum_area(self):
        """
        find the num of trees in a 1x1 property
        """
        self.assertEquals(persimmon.get_area(self.field, (1,1), (0,0)), 1)
        self.assertEquals(persimmon.get_area(self.field, (1,1), (3,3)), 1)
    def test_minimum_empty_area(self):
        """
        num of trees in a 1x1 property in a empty space
        """
        self.assertEquals(persimmon.get_area(self.field, (1,1), (1,0)), 0)
        self.assertEquals(persimmon.get_area(self.field, (1,1), (0,1)), 0)
        self.assertEquals(persimmon.get_area(self.field, (1,1), (1,1)), 0)
    def test_small_area(self):
        """
        num of trees in a 2x2 property with trees
        """
        self.assertEquals(persimmon.get_area(self.field, (2,2), (0,0)), 1)
        self.assertEquals(persimmon.get_area(self.field, (2,2), (2,2)), 2)
        self.assertEquals(persimmon.get_area(self.field, (2,2), (1,1)), 1)
    def test_small_empty_area(self):
        """
        num of trees in a 2x2 property in a empty lot
        """
        self.assertEquals(persimmon.get_area(self.field, (2,2), (1,0)), 0)
        self.assertEquals(persimmon.get_area(self.field, (2,2), (0,1)), 0)
    def test_small_empty_area_with_overlap(self):
        """
        num of trees in a 2x2 property
        """
        self.assertEquals(persimmon.get_area(self.field, (2,2), (3,0)), 0)

