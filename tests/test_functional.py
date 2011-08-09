import unittest
from .. import persimmon

class FunctionalTest(unittest.TestCase):
    def test_first_example(self):
        """
        the first example in the page
        """
        field = persimmon.create_field(16, ['10 8','2 2','2 5','2 7',
                                            '3 3','3 8','4 2','4 5',
                                            '4 8','6 4','6 7','7 5',
                                            '7 8','8 1','8 4','9 6','10 3'])
        self.assertEquals(persimmon.property_finder(field, (4,3)), 4)

    def test_second_example(self):
        """
        the second example in the page
        """
        field = persimmon.create_field(8, ['6 4','1 2','2 1','2 4','3 4',
                                           '4 2','5 3','6 1','6 2','3 2'])
        self.assertEquals(persimmon.property_finder(field, (3,2)), 3)

    def test_block_1(self):
        """
        block in the top 
        """

        field = persimmon.create_field(12, [ '5 5', '1 1', '1 2', '1 3', 
                                                    '2 1', '2 2', '2 3', 
                                                    '3 1', '3 2', '3 3', 
                                                    '4 1', '4 2', '4 3']) 
        self.assertEquals(persimmon.property_finder(field, (4,3)), 12)

    def test_block_2(self):
        """
        block in the top with a offset 
        """

        field = persimmon.create_field(12, [ '5 5', '2 2', '2 3', '2 4', 
                                                    '3 2', '3 3', '3 4', 
                                                    '4 2', '4 3', '4 4', 
                                                    '5 2', '5 3', '5 4']) 
        self.assertEquals(persimmon.property_finder(field, (4,3)), 12)

