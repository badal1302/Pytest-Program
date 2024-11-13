# test_calculator.py

from calculator import add

# Basic positive and negative number tests
def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(10, 20) == 30

def test_add_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-10, -20) == -30

# Mixed positive and negative numbers
def test_add_mixed_numbers():
    assert add(-5, 5) == 0
    assert add(-10, 20) == 10

# Zero test cases
def test_add_with_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(-5, 0) == -5

# Float test cases
def test_add_floats():
    assert add(0.1, 0.2) == 0.3  # This may fail due to floating-point precision
    assert add(1.5, 2.5) == 4.0

# Edge case tests
def test_add_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000
    assert add(-1_000_000, -2_000_000) == -3_000_000

# Invalid inputs test cases (e.g., strings, None)
def test_add_invalid_inputs():
    try:
        add("a", "b")
    except TypeError:
        assert True
    else:
        assert False, "Expected TypeError for string inputs"

    try:
        add(None, None)
    except TypeError:
        assert True
    else:
        assert False, "Expected TypeError for None inputs"
