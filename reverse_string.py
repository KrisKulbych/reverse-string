def reversed_func(text: str) -> str:

    reversed_text = []
    letter_list = [letter for word in reversed(text.split()) for letter in word if letter.isalpha()]

    for letter in text:
        if letter.isalpha():
            reversed_text.append(letter_list.pop())
        else:
            reversed_text.append(letter)

    return ''.join(reversed_text)

cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),
    ]

for input_text, expected_result in cases:
    assert reversed_func(input_text) == expected_result
