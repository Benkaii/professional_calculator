import pytest

from app.calculation import (
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    CalculationFactory,
)


@pytest.mark.parametrize(
    "calculation, expected",
    [
        (AddCalculation(5, 3), 8),
        (SubtractCalculation(5, 3), 2),
        (MultiplyCalculation(5, 3), 15),
        (DivideCalculation(6, 3), 2),
    ],
)
def test_calculation_perform(calculation, expected):
    assert calculation.perform() == expected


@pytest.mark.parametrize(
    "operation, a, b, expected_class",
    [
        ("add", 5, 3, AddCalculation),
        ("subtract", 5, 3, SubtractCalculation),
        ("multiply", 5, 3, MultiplyCalculation),
        ("divide", 6, 3, DivideCalculation),
    ],
)
def test_calculation_factory(operation, a, b, expected_class):
    calculation = CalculationFactory.create_calculation(operation, a, b)
    assert isinstance(calculation, expected_class)


def test_calculation_factory_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation"):
        CalculationFactory.create_calculation("power", 2, 3)


def test_divide_calculation_by_zero():
    calculation = DivideCalculation(10, 0)

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation.perform()