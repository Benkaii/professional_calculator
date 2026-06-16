from abc import ABC, abstractmethod
from app.operation import Operation


class Calculation(ABC):
    """Abstract base class for calculations."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def perform(self):
        pass  # pragma: no cover


class AddCalculation(Calculation):
    def perform(self):
        return Operation.add(self.a, self.b)


class SubtractCalculation(Calculation):
    def perform(self):
        return Operation.subtract(self.a, self.b)


class MultiplyCalculation(Calculation):
    def perform(self):
        return Operation.multiply(self.a, self.b)


class DivideCalculation(Calculation):
    def perform(self):
        return Operation.divide(self.a, self.b)


class CalculationFactory:
    """Creates calculation objects."""

    @staticmethod
    def create_calculation(operation, a, b):
        operations = {
            "add": AddCalculation,
            "subtract": SubtractCalculation,
            "multiply": MultiplyCalculation,
            "divide": DivideCalculation
        }

        if operation not in operations:
            raise ValueError("Invalid operation")

        return operations[operation](a, b)