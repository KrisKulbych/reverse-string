from string import punctuation, digits

def reversed_func(text):
    """
    The function reverses the letters in all words of input text.
    The order of words preserves.
    All non-letter symbols/numbers stays on the same places.
    """
    PRESERVED_CHARS = punctuation + digits
    reversed_text = []

    for word in text.split():
        char_list = []
        reversed_word = ''
        for char in word:
            if char not in PRESERVED_CHARS:
                char_list.append(char)

        for char in word:
            if char in PRESERVED_CHARS:
                reversed_word += char
            else:
                reversed_word += char_list.pop()

        reversed_text.append(reversed_word)

    return ' '.join(reversed_text)


if __name__ == "__main__":
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", "")
    ]

    for input_text, expected_result in cases:
        assert reversed_func(input_text) == expected_result


