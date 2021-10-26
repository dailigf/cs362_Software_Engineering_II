#!/bin/env/python3
import argparse


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
    This will get a valid Luhn digit
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

    return str(10 - checksum % 10)


def main():
    """
    This is the main function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    
    print(get_luhn_digit(args.input))

if __name__ == "__main__":
    main()
#digit = get_luhn_digit("7992739871")
#print(digit)
