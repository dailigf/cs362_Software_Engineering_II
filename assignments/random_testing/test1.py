import random
import string

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

def generate_testcases(tests_to_generate=100):
    edge_mc = [str(i) for i in range(50, 57)] + [str(i) for i in range(2220, 2722)]
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
    print("length: {}".format(length))
    # 50% chance of generating an edge case with 
    odds == random.randint(0, 1)
    if odds == 1:
        prefix = random.choice(prefix_edge_cases)
    else:
        prefix = str(random.randint(0, 3000))
    print("prefix: {}".format(prefix))
    # Generate random numbers for the middle numbers
    mid = "".join(str(random.randint(0, 9)) for i in range(length - len(prefix) - 1))
    # 50% chance of generating the correct luhn 
    print("mid: {}".format(mid))
    credit_card = prefix + mid
    print("credit_card: {}".format(credit_card))
    print("length of credit card: {}".format(len(credit_card)))
    odds = random.randint(0,1)
    if odds == 1:
        luhn = get_luhn_digit(credit_card)
    else:
        print("random luhn")
        luhn = random.randint(0, 9)
    print("luhn nmber: {}".format(luhn))

generate_testcases()
