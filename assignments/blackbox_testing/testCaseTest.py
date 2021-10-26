import unittest
from credit_card_validator import credit_card_validator

class TestCreditCard(unittest.TestCase):
    def test1(self):
        """
        Test an empty string.
        Expected Result: False
        """
        card_number = ""
        expected = False
        self.assertFalse(credit_card_validator(card_number), expected, msg="Empty String Expected False.")

    def test2(self):
        list=[0,0,0]
        expected = 0
        self.assertEqual(avgList(list), expected, msg=f"avgList{list}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
