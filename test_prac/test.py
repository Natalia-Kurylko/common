import unittest
from unittest.mock import patch
import homework


class TestHomework(unittest.TestCase):
    def test_two_list(self):
        ex_result = [1, 2, 3, 5, 8, 13]
        self.assertEqual(homework.two_list(), ex_result)

    def test_number_of_times(self):
        given_string = 'I am a good developer. I am also a writer'
        ex_result = 5
        self.assertEqual(homework.number_of_times(given_string), ex_result)

    def test_number_is_power(self):
        self.assertTrue(homework.number_is_power(9))
        self.assertTrue(homework.number_is_power(3))
        self.assertFalse(homework.number_is_power(122))
        self.assertFalse(homework.number_is_power(12))

    def test_add_positive_integer(self):
        self.assertEqual(homework.add_positive_integer(59), 5)
        self.assertEqual(homework.add_positive_integer(63), 9)

    def test_all_zero(self):
        ex_result = [2, 3, 4, 6, 7, 10, 0]
        l = [0, 2, 3, 4, 6, 7, 10]
        self.assertEqual(homework.all_zero(l), ex_result)

    def test_check_a_sequence_numbers(self):
        l = [5, 7, 9, 11]
        diff = 2
        self.assertTrue(homework.check_a_sequence_numbers(), diff)

    def test_find_the_number(self):
        l = [5, 3, 4, 3, 4]
        self.assertEqual(homework.find_the_number(l), 5)

    def test_find_missing_number(self):
        num_list = [1, 2, 3, 4, 6, 7, 8]
        self.assertEqual(homework.find_missing_number(num_list), 5)

    def test_count_of_elements(self):
        self.assertEqual(homework.count_of_elements(), 3)

    def test_some_param(self):
        ex_result = "sredoC dna dlroW olleH"
        self.assertEqual(homework.some_param(), ex_result)

    def test_num_parameter(self):
        self.assertEqual(homework.num_parameter(63), '1:3')

    def test_largest_word(self):
        mystring = 'fun&!! time'
        ex_result = 'time'
        self.assertEqual(homework.largest_word(mystring), ex_result)

    @patch("test_prac.homework.asks_the_users", return_value="Michele is name My")
    def test_asks_the_users(self,asks_the_users):
        self.assertEqual(asks_the_users(), 'Michele is name My')

    @patch("test_prac.homework.fibonacci_number", return_value = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
    def test_fibonacci_number(self,fibonacci_number):
        self.assertEqual(fibonacci_number(), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])

    def test_some_saved_list(self):
        a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        ex_result = [4, 16, 36, 64, 100]
        self.assertEqual(homework.some_saved_list(a), ex_result)

    def test_add_pull_off(self):
        number = 4
        self.assertEqual(homework.add_pull_off(number), 10)

    def test_factorial(self):
        n = 4
        self.assertEqual(homework.factorial(n), 24)

    def test_modify_parameter(self):
        example = 'abcd'
        ex_result = 'bcdE'
        self.assertEqual(homework.modify_parameter(example),ex_result)

    def test_letters_alphabetical_order(self):
        s = 'edcba'
        r = 'abcde'
        self.assertEqual(homework.letters_alphabetical_order(s),r)

    def test_greater(self):
        self.assertTrue(homework.greater(1,2))
        self.assertFalse(homework.greater(2,1))
        self.assertEqual(homework.greater(1,1),'-1')
        

if __name__ == "__main__":
    unittest.main()
