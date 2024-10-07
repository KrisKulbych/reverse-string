# Reverse String Application

## Description
This Python application contains a function reverse_string(), that reverses the letters in each word of an input string while preserving the original order of words and the positions of non-letter characters such as symbols or numbers. Additionally, the application includes custom error handling for non-string inputs.

## Features
- Reverses only the alphabetical characters in each word.
- Retains the original positions of non-letter symbols and numbers within the words.
- The order of the words in the string remains unchanged.
- Only latin alphabet is counted in the application.
- Raises a custom exception NonStringInputError, when the input is not a string.

## Requirements
Python 3.x

## Solution
<details>
  <summary>Click For Solution</summary>
  
```  
class NonStringInputError(Exception):
    """Raised when getting non-string input"""


def reverse_string(string: str) -> str:
    """
    The function reverses the letters in all words of input text.
    The order of words preserves.
    All non-letter symbols/numbers stays on the same places.
    """
    string_reversed = []
    if not isinstance(string, str):
        raise NonStringInputError('Error! Invalid input data: expected a string value')

    for word in string.split():
        letter_list = [letter for letter in word if letter.isalpha()]

        word_reversed = []
        for letter in word:
            if letter.isalpha():
                word_reversed.append(letter_list.pop())
            else:
                word_reversed.append(letter)
        string_reversed.append(''.join(word_reversed))

    return ' '.join(string_reversed)
```
</details>
 
## Explanation
1. The function takes one argument, string, which is expected to be of type str (string).
2. The first check ensures that the input is a string. If not, it raises a custom exception *NonStringInputError*. 
3. The *string.split()* method breaks the input string into a list of words based on spaces.
4. The function then iterates over each word in the list.
5. The list comprehension extracts only the alphabetical characters from the word identifying them with *word.isalpha()* method.
6. A new list, *word_reversed*, is created to store the reconstructed word.
7. The for loop iterates over each character of the original word:
   - if the character is alphabetical (checked with *isalpha()*), the function appends the last letter from *letter_list* using *letter_list.pop()*. This reverses the order of the letters;
   - if the character is not alphabetical (e.g., punctuation or numbers), it remains in its original place in the word.
8. Once the word is reconstructed, it is joined into a single string using *''.join(word_reversed)* and added to the *string_reversed* list.
9. After all the words have been processed, the list *string_reversed* contains the reversed versions of the original words.
10. The *join()* method combines these words back into a single string, with spaces between them, preserving the original order of the words.

Examples
```
from reverse_string import reverse_string

cases = ["abcd efgh", "a1bcd efg!h", ""]

for input_text in cases:
    reversed_text = reverse_string(input_text)
    print(reversed_text)
```
Output
```
dcba hgfe
d1cba hgf!e

```

## Test Cases
<details>
  <summary>Test Case 1: checking correct behavior for several cases with subTest</summary>

```
from unittest import TestCase, main

from task_2 import reverse_string, NonStringInputError


class TestReverseString(TestCase):
    def test_reverse_string(self) -> None:
        # Given
        cases = [
            ("abcd efgh", "dcba hgfe"),
            ("a1bcd efg!h", "d1cba hgf!e"),
            ("", ""),
        ]
        # When
        for input_text, expected_result in cases:
            with self.subTest(input_text=input_text):
                # Then
                self.assertEqual(reverse_string(input_text), expected_result)
```
</details>
<details>
  <summary>Test Case 2: checking fail behavior with custom exception</summary>

```
from unittest import TestCase, main

from task_2 import reverse_string, NonStringInputError


class TestReverseString(TestCase):
    def test_non_string_input(self) -> None:
        # Given
        cases = [123, 30.6, None, [], {}, set()]
        # When
        for input_text in cases:
            with self.subTest(input_text=input_text):
                # Then
                with self.assertRaises(NonStringInputError) as error:
                    reverse_string(input_text)
                self.assertEqual(str(error.exception), 'Error! Invalid input data: expected a string value')
```
</details>

## Helpful Links
- [Subtests in Python](https://blog.ganssle.io/articles/2020/04/subtests-in-python.html)
- [Python Basics: Why use __init__.py?](https://sarangsurve.medium.com/python-basics-why-use-init-py-c88589e44c91)
- [Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [Coverage.py](https://coverage.readthedocs.io/en/7.6.1/)
- [Given-When-Then pattern](https://medium.com/@gitaeklee/given-when-then-junit-test-ba49564303e7)
- [Custom Exception in Python](https://martinxpn.medium.com/custom-exceptions-in-python-creating-custom-exceptions-59-100-days-of-python-4f26de8e851d)

tags: `python` `python3` `problem-solving` `programming` `learn-python`
