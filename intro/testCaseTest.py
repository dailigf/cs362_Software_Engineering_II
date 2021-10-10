import unittest
from unit_testing import avgList

class TestAvgList(unittest.TestCase):
    def test1(self):
        list = [1,2,3]
        expected = 3
        string = ' '.join(f"{x}" for x in list)
        self.assertEqual(avgList(list), expected, msg=f"avgList{string}")

    def test2(self):
        list=[0,0,0]
        expected = 0
        self.assertEqual(avgList(list), expected, msg=f"avgList{list}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
