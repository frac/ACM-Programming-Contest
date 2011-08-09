import unittest
from .. import persimmon

class FieldTest(unittest.TestCase):
    def test_create_empty_field(self):
        square_field = ["2 2"]
        self.assertEquals(persimmon.create_field(0, square_field), [ [0,0], [0,0] ])

        long_field = ["3 1"]
        self.assertEquals(persimmon.create_field(0, long_field), [ [0], [0], [0] ])

        tall_field = ["1 3"]
        self.assertEquals(persimmon.create_field(0,tall_field), [ [0,0,0] ])


    def test_create_field_with_trees(self):
        square_empty_field = ['2 2']
        self.assertEquals(persimmon.create_field(0,square_empty_field), [ [0,0], [0,0] ])
        square_field_1 = ['2 2','1 1']
        self.assertEquals(persimmon.create_field(1,square_field_1), [ [1,0], [0,0] ])
        square_field_2 = ['2 2','2 2']
        self.assertEquals(persimmon.create_field(1,square_field_2), [ [0,0], [0,1] ])


        square_field_column = ['2 2','1 1','1 2']
        self.assertEquals(persimmon.create_field(2,square_field_column), [ [1,1], [0,0] ])

