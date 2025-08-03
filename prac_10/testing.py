def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_as_sentence(phrase):
    """
    Format a phrase as a sentence starting with capital and ending with full stop.
    >>> format_as_sentence("hello")
    'Hello.'
    >>> format_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_as_sentence("this is a test")
    'This is a test.'
    """
    if not phrase:
        return phrase
    phrase = phrase.capitalize()
    if phrase[-1] != '.':
        phrase += '.'
    return phrase


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    test_car_default = Car()
    assert test_car_default.fuel == 0, "Car default fuel not set correctly"

    test_car_with_fuel = Car(fuel=10)
    assert test_car_with_fuel.fuel == 10, "Car fuel not set correctly from parameter"


run_tests()
doctest.testmod()