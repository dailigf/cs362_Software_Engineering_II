import random
import string
import unittest
#from credit_card_validator import credit_card_validator

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
        return str(10 - checksum %10)
    else:
        return 0

def get_expected(credit_card):
    """
    This will return what the expected result of the function
    :param credit_card: credit card number
    :type credit_card: string
    :return: True/False
    :rtype: boolean
    """
    prefix_mc = [str(i) for i in range(51, 56)] + [str(i) for i in range(2221, 2721)]
    prefix_visa = ["4"]
    prefix_amex = ["34", "37"]
    expected = True
    # Check for valid length
    if len(credit_card) < 15 or len(credit_card) > 16:
        expected = False
        print("Invalid Length: {}".format(len(credit_card)))
        return expected

    # Check for valid prefix
    if(credit_card[0] not in prefix_visa and credit_card[0:4] not in prefix_mc and
            credit_card[0:2] not in prefix_amex):
           expected = False
           print("Invalid Prefix: {}".format(credit_card[0:4]))
           return expected
    else:
        if credit_card[0] in prefix_visa and len(credit_card) != 16:
            expected = False
            print("Visa Prefix: {}, Invalid Length: {}".format(credit_card[0], len(credit_card)))
            return expected
        elif credit_card[0:4] in prefix_mc and len(credit_card) != 16:
            expected = False
            print("MasterCard Prefix: {}, Invalid Length: {}".format(credit_card[0:4], len(credit_card)))
            return expected
        elif credit_card[0:2] in prefix_mc and len(credit_card) != 16:
            expected = False
            print("MasterCard Prefix: {}, Invalid Length: {}".format(credit_card[0:2], len(credit_card)))
            return expected
        elif credit_card[0:2] in prefix_amex and len(credit_card) != 15:
            expected = False
            print("AMEX Prefix: {}, Invalid Length: {}".format(credit_card[0:2], len(credit_card)))
            return expected
        else:
            pass
    # Check for valid luhn
    if get_luhn_digit(credit_card[0:-1]) != int(credit_card[-1]):
        expected = False
        print("Invalid Luhn: {}".format(credit_card[-1]))
        return expected
    print("Valid Credit Card")
    return expected

def build_test_func(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result, message.format(test_case, expected,
            result))
        return test

def generate_testcases(tests_to_generate=10000):
    for i in range(0, tests_to_generate):
        expected = True
        #edge_mc = [str(i) for i in range(50, 57)] + [str(i) for i in range(2220, 2722)]
        edge_mc = ["50", "51", "52", "54", "55", "56", "2220", "2221", "2222", "2719", "2720", "2721"]
        edge_visa = [str(i) for i in range(3, 6)]
        edge_amex = [str(i) for i in range(33, 39)]
        prefix_edge_cases = edge_mc + edge_visa + edge_amex
        previx_mc = [str(i) for i in range(51, 56)] + [str(i) for i in range(2221, 2721)]
        prefix_visa = ["4"]
        prefix_amex = ["34", "37"]
        for i in range(tests_to_generate):
            expected = True
        # List of edge case lengths
        edge_cases = [14, 15, 16, 17]
        # 50% chance of generating an edge case with the lengths
        odds = random.randint(0, 1)
        if odds == 1:
            length = random.choice(edge_cases)
        else:
            #Random Length
            length = random.randint(0, 20)
        # 50% chance of generating an edge case with 
        odds = random.randint(0, 1)
        if odds == 1:
            prefix = random.choice(prefix_edge_cases)
        else:
            prefix = str(random.randint(0, 3000))
        # Generate random numbers for the middle numbers
        mid = "".join(str(random.randint(0, 9)) for i in range(length - len(prefix) - 1))
        # 50% chance of generating the correct luhn 
        odds = random.randint(0,1)
        if odds == 1:
            luhn = get_luhn_digit(prefix + mid)
        else:
            luhn = random.randint(0,10)
        credit_card = prefix + mid + str(luhn)
        print("credit_card: {}".format(credit_card))
        print("length: {}".format(len(credit_card)))
        expected = get_expected(credit_card)

        message = "Test Case: {}, Expected: {}, Result: {}"
        #new_test = build_test_func(expected, credit_card, credit_card, message)

if __name__ == "__main__":
    generate_testcases()
    #unittest.main()

