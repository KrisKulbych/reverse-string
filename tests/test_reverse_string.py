from unittest import TestCase, main
from task_2.reverse_string import reverse_string, NonStringInputError


class TestReverseString(TestCase):
    def test_reverse_string(self):
        cases = [
            ("abcd efgh", "dcba hgfe"),
            ("a1bcd efg!h", "d1cba hgf!e"),
            ("", ""),
        ]
        for input_text, expected_result in cases:
            with self.subTest(input_text=input_text):
                self.assertEqual(reverse_string(input_text), expected_result)

    def test_NonStringInputError(self):
        cases = [123, 30.6, None, [], {}, set()]
        for input_text in cases:
            with self.subTest(input_text=input_text):
                with self.assertRaises(NonStringInputError) as error:
                    reverse_string(input_text)
                self.assertEqual(str(error.exception), 'Error! Invalid input data: expected a string value')


if __name__ == '__main__':
    main()
