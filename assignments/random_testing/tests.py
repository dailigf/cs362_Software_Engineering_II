import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    pass


def get_digits(number):
    """
    This will create a list of numbers
    :param number: number
    :type number: string
    :return: list of numbers
    :rtype: list of ints
    """
    arr = [int(d) for d in str(number)]
    return arr


def get_luhn_digit(number):
    """
    This function will calculate the luhn number
    :param number: credit card number
    :type number: string
    :return: luhn digit
    :rtype: string
    """
    odd_digits = number[-1::-2]
    even_digits = number[-2::-2]
    even_digits = [int(digit) for digit in even_digits]

    checksum = 0
    for digit in odd_digits:
        tmp = int(digit) * 2
        checksum += sum(get_digits(str(tmp)))

    checksum = checksum + sum(even_digits)

    if checksum % 10 > 0:
        return str(10 - checksum % 10)
    else:
        return 0


def get_expected(card):
    """
    This will return what the expected result of the function
    :param card: credit card number
    :type card: string
    :return: True/False
    :rtype: boolean
    """
    mc_1 = [str(i) for i in range(51, 56)]
    mc_2 = [str(i) for i in range(2221, 2721)]
    visa = ["4"]
    amex = ["34", "37"]

    if type(card) == int:
        return False
    if len(card) == 0:
        return False
    luhn = get_luhn_digit(card[0:-1])
    length = len(card)
    if card[0] in visa and length == 16 and card[-1] == luhn:
        return True
    elif card[0:2] in amex and length == 15 and card[-1] == luhn:
        return True
    elif card[0:4] in mc_1 and length == 16 and card[-1] == luhn:
        return True
    elif card[0:2] in mc_2 and length == 16 and card[-1] == luhn:
        return True
    else:
        return False


def build_test_func(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result,
                         message.format(test_case, expected, result))
    return test


def generate_testcases(tests_to_generate=110000):
    for i in range(0, tests_to_generate):
        cards = {
            "visa": {
                "prefix": ["4"],
                "edge_prefix": ["3", "4", "5"],
                "length": 16,
                "edge_length": [0, 15, 16, 17]
            },
            "mc": {
                "prefix": ["51", "55", "2221", "2720"],
                "edge_prefix": ["50", "51", "52", "54", "55", "56", "2220",
                                "2221", "2222", "2719", "2720", "2721"],
                "length": 16,
                "edge_length": [0, 15, 16, 17]
            },
            "amex": {
                "prefix": ["34", "37"],
                "edge_prefix": ["33", "34", "35", "36", "37", "38"],
                "length": 15,
                "edge_length": [0, 14, 15, 16]
            }
        }

        credit_card = ""
        selection = ""
        randErr = ""
        # 50% chance of selecting a truly random card or a valid one
        odds = random.randint(0, 1)
        if odds == 1:
            length = random.randint(0, 30)
            credit_card = "".join(
                str(random.randint(0, 9))
                for i in range(length))
        else:
            selection = random.choice(list(cards.keys()))
            odds = random.randint(0, 1)
            if odds == 1:
                randErr = True
            else:
                randErr = False
                prefix = random.choice(cards[selection]["prefix"])
                length = cards[selection]["length"]
                mid = "".join(
                    str(random.randint(0, 9))
                    for i in range(length - len(prefix) - 1))
                odds = random.randint(0, 1)
                if odds == 1:
                    luhn = random.randint(0, 9)
                else:
                    luhn = get_luhn_digit(prefix + mid)
                credit_card = prefix + mid + str(luhn)

        if randErr:
            odds = random.randint(0, 1)
            if odds == 1:
                length = random.randint(0, 30)
            else:
                length = random.choice(cards[selection]["edge_length"])
            prefix = random.choice(cards[selection]["edge_prefix"])

            if length == 0:
                credit_card = ""
            elif length == 1:
                credit_card = str(random.randint(0, 9))
            else:
                if len(prefix) > length:
                    credit_card = "".join(
                        str(random.randint(0, 9))
                        for i in range(length - 1))
                else:
                    mid = "".join(
                        str(random.randint(0, 9))
                        for i in range(length - 1))
                    credit_card = prefix + mid

                # 50% chance to generate the correct luhn
                odds = random.randint(0, 1)
                if odds == 1:
                    luhn = random.randint(0, 9)
                else:
                    luhn = get_luhn_digit(credit_card)
                credit_card = credit_card + str(luhn)

        expected = get_expected(credit_card)

        message = "Test Case: {}, Expected: {}, Result: {}"
        new_test = build_test_func(
            expected, credit_card, credit_card_validator, message)
        setattr(TestCase, 'test_{}'.format(credit_card), new_test)


if __name__ == "__main__":
    generate_testcases()
    unittest.main()
