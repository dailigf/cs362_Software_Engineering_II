import random
import string
import unittest


class TestCase(unittest.TestCase):
    def test1(self):
        tests_to_generate = 100

        for i in range(tests_to_generate):
            expected = True
            # List of edge case lengths
            edge_cases = [7, 8, 9, 20, 21]
            # 50% chance of generating an edge case
            odds = random.randint(0, 1)
            if odds == 1:
                length = random.choice(edge_cases)
            else:
                # Random Length
                length = random.randint(0, 30)
            # Random number of lower case
            low = random.randint(0, length)
            # Random number of upper case
            up = random.randint(0, length - low)
            # Random number of numbers
            dig = random.randint(0, length - low - up)
            # Random number of symbols
            sym = random.randint(0, length - low - up - dig)
            # Determine final length of the string
            length = low + up + dig + sym
            # Set expected result based on specification
            if length < 8 or length > 20:
                expected = False
            if low < 1 or up < 1 or dig < 1 or sym < 1:
                expected = False
            # Generate password
            pwd = self.gen_pass(length, low, up, dig, sym)
            # Generate failure message if check_pwd doesn't match expection
            if check_pwd(pwd) != expected:
                print('Failure: {} should be {}'.format(pwd, expected))
        
    def gen_pass(self, length=8, low=1, up=1, dig=1, sym=1, spa=False):
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_upperacse
        digits = string.digits
        symbols = '~`!@#$%^&*()_+-='
        all_pos = lower_case + upper_case + digits + symbols

        pwd = ''
        pwd = pwd + ''.join(random.choice(lower_case) for i in range(low))
        pwd = pwd + ''.join(random.choice(upper_case) for i in range(up))
        pwd = pwd + ''.join(random.choice(digits) for i in range(dig))
        pwd = pwd + ''.join(random.choice(symbols) for i in range(sym))
        pwd = pwd + ''.join(random.choice(all_pos)
                            for i in range(length - len(pwd)))

        return ''.join(random.sample(pwd, len(pwd)))

    if __name__ == '__main__':
        unittest.main()
