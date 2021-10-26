import unittest
from contrived_func import contrived_func


class Test(unittest.TestCase):
    def test1(self):
        val = 101
        self.assertTrue(contrived_func(val), msg="val: {}".format(val))

    def test2(self):
        val = 6
        self.assertFalse(contrived_func(val), msg="val: {}".format(val))

    def test3(self):
        val = 5
        self.assertTrue(contrived_func(val), msg="val: {}".format(val))

    def test4(self):
        val = 70
        self.assertTrue(contrived_func(val), msg="val: {}".format(val))

    def test5(self):
        val = 80
        self.assertTrue(contrived_func(val), msg="val: {}".format(val))

    def test6(self):
        val = 69
        self.assertFalse(contrived_func(val), msg="val: {}".format(val))

    def test7(self):
        val = 157
        self.assertFalse(contrived_func(val), msg="val: {}".format(val))


if __name__ == "__main__":
    unittest.main(verbosity=2)
