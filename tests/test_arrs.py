import unittest
from utils import arrs


class TestArrs(unittest.TestCase):
    def setUp(self):
        self.arr = [1, 2, 3, 4, 5]

    def test_get(self):
        # positive index
        self.assertEqual(arrs.get(self.arr, 2), 3)
        self.assertEqual(arrs.get([1, 2], 1), 2)

        # negative index
        self.assertIsNone(arrs.get(self.arr, -2))
        self.assertIsNone(arrs.get([1, 2], -3))

        # default value
        self.assertEqual(arrs.get([1], 0, None), 1)
        self.assertEqual(arrs.get(self.arr, -10, None), None)

        # test with None as default value
        self.assertIsNone(arrs.get(self.arr, -10, None))

    def test_my_slice(self):
        # no args
        self.assertEqual(arrs.my_slice(self.arr), [1, 2, 3, 4, 5])
        self.assertEqual(arrs.my_slice([], None), [])

        # start only
        self.assertEqual(arrs.my_slice(self.arr, start=2), [3, 4, 5])
        self.assertEqual(arrs.my_slice([1], start=0), [1])

        # end only
        self.assertEqual(arrs.my_slice(self.arr, end=3), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1], end=0), [])

        # start and end
        self.assertEqual(arrs.my_slice(self.arr, start=1, end=4), [2, 3, 4])
        self.assertEqual(arrs.my_slice([1], start=0, end=1), [1])

        # negative start and end
        self.assertEqual(arrs.my_slice(self.arr, start=-3), [3, 4, 5])
        self.assertEqual(arrs.my_slice([1, 2, 3]), [1, 2, 3])
        self.assertEqual(arrs.my_slice(self.arr, start=-3, end=-1), [3, 4])

        # start and end out of range
        self.assertEqual(arrs.my_slice(self.arr, start=10), [])
        self.assertEqual(arrs.my_slice(self.arr, end=10), [1, 2, 3, 4, 5])
        self.assertEqual(arrs.my_slice(self.arr, start=3, end=1), [])

        # test with step argument
        self.assertEqual(arrs.my_slice([1, 2, 3, 4]), [1, 2, 3, 4])

        # additional test cases
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1), [3])
        self.assertEqual(arrs.my_slice([], 0), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -5), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -5, 5), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -5, None), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -5, None), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, -1), [2])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2, -1), [2])
