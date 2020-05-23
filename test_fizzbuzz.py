import unittest


class TestFizzBuzz(unittest.TestCase):
    def test_get_one_when_input_is_one(self):
        result = fizzbuzz(1)
        assert result == 1

    def test_get_four_when_input_is_four(self):
        result = fizzbuzz(4)
        assert result == 4

    def test_get_fizz_when_input_is_three(self):
        result = fizzbuzz(3)
        assert result == 'fizz'

    def test_get_fizz_when_input_is_six(self):
        result = fizzbuzz(6)
        assert result == 'fizz'


def fizzbuzz(number):
    if number % 3 == 0:
        return 'fizz'

    return number
