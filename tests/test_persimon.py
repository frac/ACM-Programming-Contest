import unittest
from .. import persimmon

class PersimmonTest(unittest.TestCase):
    def test_linear_prop(self):
        """
        test to find a 2x1 property in a single line
        """
        field = [[0],[0],[0],[0]]
        self.assertEquals(persimmon.property_finder(field, (2,1)), 0)
        field = [[1],[0],[0],[0]]
        self.assertEquals(persimmon.property_finder(field, (2,1)), 1)
        field = [[1],[1],[0],[0]]
        self.assertEquals(persimmon.property_finder(field, (2,1)), 2)
        

    def test_min_property_empty(self):
        """
        how many trees in for a 1x1 property in a 1x1 empty field 
        """
        field = [[0]]
        self.assertEquals(persimmon.property_finder(field, (1,1)), 0)

    def test_min_property_single_tree(self):
        """
        how many trees in for a 1x1 property in a 1x1 single tree 
        """
        field = [[1]]
        self.assertEquals(persimmon.property_finder(field, (1,1)), 1)

    def test_min_property_size_in_a_line(self):
        """
        test to find a 1x1 property in a single line with a single tree
        """
        field = [[1],[0],[0]]
        self.assertEquals(persimmon.property_finder(field, (1,1)), 1)

    def test_min_property_size_in_a_col(self):
        """
        test to find a 1x1 property in a single line with a single tree
        """
        field = [[1,0,0]]
        self.assertEquals(persimmon.property_finder(field, (1,1)), 1)
