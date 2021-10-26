import unittest
from credit_card_validator import credit_card_validator


class TestCreditCard(unittest.TestCase):
    def test1(self):
        """
        Test an empty string.
        Expected Result: False
        Bug 1/6
        """
        card_number = ""
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Empty String Expected False."
        )

    def test2(self):
        """
        This will test a string of length 14.
        AMEX/Mastercard/Visa have length >= 15
        Expected Result: False
        """
        card_number = "12345678901234"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid Length: {}, expecting Flase".format(len(card_number)),
        )

    def test3(self):
        """
        This will test a string of length 17.
        Boundary conditions, AMEX/Mastercard/Visa have length < 17
        Expected Result: False
        """
        card_number = "12345678901234567"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid Length: {}, expecting Flase".format(len(card_number)),
        )

    def test4(self):
        """
        This will test a credit card number with a non-number in it.
        It will be of length 15
        Expected Result: False
        """
        card_number = "12345678901234F"
        with self.assertRaises(Exception):
            credit_card_validator(card_number)

    def test5(self):
        """
        This will test a credit card number that is not a string literal.
        Expected Result: False
        """
        card_number = 123456789012345
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Integer provided. Expecting False"
        )

    def test6(self):
        """
        This will test a valid Visa Card Number.
        {Prefix: 4, Length: 16, Number: All, Type: String, Luhn: valid}
        Expected Result: True
        """
        card_number = "4123456789012349"
        self.assertTrue(
            credit_card_validator(card_number),
            msg="Valid Visa. Length: {}".format(len(card_number))
        )

    def test7(self):
        """
        This will test an invalid Visa Card Number.
        {Prefix: 4, Length: 16, Number: All, Type: String, Luhn: invalid}
        Expected Result: False
        """
        card_number = "4123456789012340"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Visa Prefix with Length 15. Expecting False",
        )

    def test8(self):
        """
        This will test an invalid Visa Card Number.
        Valid Luhn, invalid Length
        {Prefix: 4, Length: 15, Number: All, Type: String, Luhn: valid}
        Expected Result: False
        """
        card_number = "412345678901233"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Visa Prefix with Length 15. Expecting False",
        )

    def test9(self):
        """
        This will test an invalid Visa Card Number.
        Invalid Length, Invalid Luhn
        {Prefix: 4, Length: 15, Number: All, Type: String, Luhn: invalid}
        Expected Result: False
        """
        card_number = "412345678901235"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Visa Prefix, Invalid Length,\
                    Invalid Luhn. Expecting False",
        )

    def test10(self):
        """
        This will test an invalid Visa Card Number.
        Invalid Length, Valid Luhn
        {Prefix: 4, Length: 17, Number: All, Type: String, Luhn: valid}
        Expected Result: False
        """
        card_number = "41234567890123565"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid Visa.\
                    Too Long: {}.\
                    Valid Luhn: {}\
                    ".format(len(card_number), card_number[-1]),
        )

    def test11(self):
        """
        This will test an invalid Visa Card Number.
        Invalid Length, Invalid Luhn
        {Prefix: 4, Length: 17, Number: All, Type: String, Luhn: valid}
        Expected Result: False
        """
        card_number = "41234567890123560"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid Visa.\
                    Too Long: {}.\
                    Invalid Luhn: {}\
                    ".format(len(card_number), card_number[-1]),
        )

    def test12(self):
        """
        This will test a valid Mastercard number
        Valid Length, Valid Prefix, Valid Luhn
        {Prefix: 55, Length: 16, Number: All, Type: String, Luhn: valid}
        Expected Result: True
        """
        card_number = "5512345678901231"
        self.assertTrue(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Valid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefis: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test13(self):
        """
        This will test an invalid Mastercard number
        Valid Length, Valid Prefix, invalid Luhn
        {Prefix: 55, Length: 16, Number: All, Type: String, Luhn: invalid}
        Expected Result: False
        """
        card_number = "5512345678901234"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid Mastercard.\
                    Valid Length: {}.\
                    Invalid Luhn: {}\
                    Valid Prefis: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test14(self):
        """
        This will test an invalid Mastercard number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 55, Length: 15, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "551234567890122"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid Mastercard.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test15(self):
        """
        This will test an invalid Mastercard number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 55, Length: 17, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "55123456789012341"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid Mastercard.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test16(self):
        """
        This will test a valid Mastercard number
        Valid Length, Valid Prefix, Valid Luhn
        {Prefix: 51, Length: 16, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "5112345678901235"
        self.assertTrue(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Valid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test17(self):
        """
        This will test an invalid Mastercard number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 51, Length: 15, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "511234567891236"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test18(self):
        """
        This will test an invalid Mastercard number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 51, Length: 17, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "51123456789112348"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test19(self):
        """
        This will test a valid Mastercard number
        Valid Length, Valid Prefix, Valid Luhn
        {Prefix: 53, Length: 16, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "5312345678901233"
        self.assertTrue(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Valid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test20(self):
        """
        This will test an invalid Mastercard number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 53, Length: 15, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "531234567891281"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test21(self):
        """
        This will test an invalid Mastercard number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 53, Length: 17, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "53123456789123473"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test22(self):
        """
        This will test invalid Mastercard number
        Valid Length, Valid Prefix, Invalid Luhn
        {Prefix: 53, Length: 16, Number: All, Type: String, Luhn: Invalid}
        Expected Result: False
        """
        card_number = "5312345678901231"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Valid Length: {}.\
                    Invalid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test23(self):
        """
        This will test invalid Mastercard number
        Valid Length, Invalid Prefix, Valid Luhn
        {Prefix: 50, Length: 16, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "5012345678901236"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid Mastercard.\
                    Valid Length: {}.\
                    Valid Luhn: {}\
                    Invalid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test24(self):
        """
        This will test invalid Mastercard number
        Valid Length, Invalid Prefix, Valid Luhn
        {Prefix: 56, Length: 16, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "5612345678911239"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid Mastercard.\
                    Valid Length: {}.\
                    Valid Luhn: {}\
                    Invalid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test25(self):
        """
        This will test a valid Mastercard number
        Valid Length, Valid Prefix, Valid Luhn
        {Prefix: 2221, Length: 16, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "2221123456789014"
        self.assertTrue(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Valid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test26(self):
        """
        This will test an invalid Mastercard number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 2221, Length: 15, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "222112345678903"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test27(self):
        """
        This will test an invalid Mastercard number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 2221, Length: 17, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "22211234567890334"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test28(self):
        """
        This will test a valid Mastercard number
        Valid Length, Valid Prefix, Valid Luhn
        {Prefix: 2720, Length: 16, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "2720123456789002"
        self.assertTrue(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Valid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test29(self):
        """
        This will test an invalid Mastercard number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 2221, Length: 15, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "272012345678904"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test30(self):
        """
        This will test an invalid Mastercard number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 2221, Length: 17, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "27201234567890335"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test31(self):
        """
        This will test a valid Mastercard number
        Valid Length, Valid Prefix, Valid Luhn
        {Prefix: 2500, Length: 16, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "2500123456789016"
        self.assertTrue(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Valid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test32(self):
        """
        This will test an invalid Mastercard number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 2500, Length: 15, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "250012345678918"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test33(self):
        """
        This will test an invalid Mastercard number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 2500, Length: 17, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "25001234567890331"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test34(self):
        """
        This will test an invalid Mastercard number
        Valid Length, Invalid Prefix, Valid Luhn
        {Prefix: 2721, Length: 16, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "2721123456789019"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid Mastercard.\
                    Valid Length: {}.\
                    Valid Luhn: {}\
                    Invalid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test35(self):
        """
        This will test an invalid Mastercard number
        Valid Length, Invalid Prefix, Valid Luhn
        {Prefix: 2220, Length: 16, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "2220123456789015"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid Mastercard.\
                    Valid Length: {}.\
                    Valid Luhn: {}\
                    Invalid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test36(self):
        """
        This will test an invalid Mastercard number
        Valid Length, Valid Prefix, Invalid Luhn
        {Prefix: 2500, Length: 16, Number: All, Type: String, Luhn: Invalid}
        Expected Result: False
        """
        card_number = "2500123456789015"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Valid Length: {}.\
                    Invalid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test37(self):
        """
        This will test an invalid Mastercard number
        Valid Length, Valid Prefix, Invalid Luhn
        {Prefix: 2720, Length: 16, Number: All, Type: String, Luhn: Invalid}
        Expected Result: False
        """
        card_number = "2720123456789004"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Valid Length: {}.\
                    Invalid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test38(self):
        """
        This will test invalid Mastercard number
        Valid Length, Valid Prefix,Invalid Valid Luhn
        {Prefix: 2221, Length: 16, Number: All, Type: String, Luhn: Invalid}
        Expected Result: False
        """
        card_number = "2221123456789018"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Valid Length: {}.\
                    Invalid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:5]),
        )

    def test39(self):
        """
        This will test an invalid Mastercard number
        Valid Length, Valid Prefix, Invalid Luhn
        {Prefix: 53, Length: 16, Number: All, Type: String, Luhn: Invalid}
        Expected Result: False
        """
        card_number = "5312345678901236"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Valid Length: {}.\
                    Invalid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test40(self):
        """
        This will test an invalid Mastercard number
        Valid Length, Valid Prefix, Invalid Luhn
        {Prefix: 55, Length: 16, Number: All, Type: String, Luhn: Invalid}
        Expected Result: False
        """
        card_number = "5512345678901232"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Valid Mastercard.\
                    Valid Length: {}.\
                    Invalid Luhn: {}\
                    Valid Prefis: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test41(self):
        """
        This will test a valid AMEX number
        Valid Length, Valid Prefix, Valid Luhn
        {Prefix: 34, Length: 15, Number: All, Type: String, Luhn: Valid}
        Expected Result: True
        """
        card_number = "341234567890127"
        self.assertTrue(
            credit_card_validator(card_number),
            msg="Valid AMEX.\
                    Valid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test42(self):
        """
        This will test an invalid AMEX number
        Valid Length, Valid Prefix, Invalid Luhn
        {Prefix: 34, Length: 15, Number: All, Type: String, Luhn: Invalid}
        Expected Result: False
        """
        card_number = "341234567890122"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid AMEX.\
                    Valid Length: {}.\
                    Invalid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test43(self):
        """
        This will test an invalid AMEX number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 34, Length: 14, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "34123456789015"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid AMEX.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )

    def test44(self):
        """
        This will test an invalid AMEX number
        Invalid Length, Valid Prefix, Valid Luhn
        {Prefix: 34, Length: 16, Number: All, Type: String, Luhn: Valid}
        Expected Result: False
        """
        card_number = "3412345678901237"
        self.assertFalse(
            credit_card_validator(card_number),
            msg="Invalid AMEX.\
                    Invalid Length: {}.\
                    Valid Luhn: {}\
                    Valid Prefix: {}\
                    ".format(len(card_number), card_number[-1],
                             card_number[0:2]),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
