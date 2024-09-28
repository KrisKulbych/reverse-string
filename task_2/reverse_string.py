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
