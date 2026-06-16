import pytest
from app.operation import Operation


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 8),
        (10, 2, 12),
        (-1, 1, 0),
    ]
)
def test_add(a, b, expected):
    assert Operation.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 5, 5),
        (8, 2, 6),
        (0, 5, -5),
    ]
)
def test_subtract(a, b, expected):
    assert Operation.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (5, 0, 0),
        (-2, 4, -8),
    ]
)
def test_multiply(a, b, expected):
    assert Operation.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (-8, 2, -4),
    ]
)
def test_divide(a, b, expected):
    assert Operation.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operation.divide(5, 0)