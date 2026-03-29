import pytest
from calculator import get_number, double_number


def test_valid_input():
    assert get_number("10") == 10


def test_invalid_input():
    with pytest.raises(ValueError):
        get_number("hello")