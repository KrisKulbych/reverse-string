def reverse_string(string: str) -> str:
    """
    The function reverses the letters in all words of input text.
    The order of words preserves.
    All non-letter symbols/numbers stays on the same places.
    """
    string_reversed = []
    letter_list = [letter for word in reversed(string.split()) for letter in word if letter.isalpha()]

    for letter in string:
        if letter.isalpha():
            string_reversed.append(letter_list.pop())
        else:
            string_reversed.append(letter)

    return ''.join(string_reversed)


if __name__ == "__main__":
    cases = [
            ("abcd efgh", "dcba hgfe"),
            ("a1bcd efg!h", "d1cba hgf!e"),
            ("", ""),
        ]
    for input_text, expected_result in cases:
        assert reverse_string(input_text) == expected_result
