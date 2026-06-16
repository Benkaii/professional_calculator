from unittest.mock import patch
from app.calculator import Calculator


def test_show_help(capsys):
    calculator = Calculator()

    calculator.show_help()

    captured = capsys.readouterr()

    assert "Available commands" in captured.out


def test_show_history_empty(capsys):
    calculator = Calculator()

    calculator.show_history()

    captured = capsys.readouterr()

    assert "No calculations yet." in captured.out


def test_show_history_with_items(capsys):
    calculator = Calculator()
    calculator.history.append("add(2, 3) = 5")

    calculator.show_history()

    captured = capsys.readouterr()

    assert "add(2, 3) = 5" in captured.out


@patch(
    "builtins.input",
    side_effect=["add", "5", "3", "exit"]
)
def test_run_add(mock_input, capsys):
    calculator = Calculator()

    calculator.run()

    captured = capsys.readouterr()

    assert "Result: 8.0" in captured.out


@patch(
    "builtins.input",
    side_effect=["help", "exit"]
)
def test_run_help(mock_input, capsys):
    calculator = Calculator()

    calculator.run()

    captured = capsys.readouterr()

    assert "Available commands" in captured.out


@patch(
    "builtins.input",
    side_effect=["history", "exit"]
)
def test_run_history(mock_input, capsys):
    calculator = Calculator()

    calculator.run()

    captured = capsys.readouterr()

    assert "No calculations yet." in captured.out


@patch(
    "builtins.input",
    side_effect=["badcommand", "exit"]
)
def test_run_invalid_operation(
    mock_input, capsys
):
    calculator = Calculator()

    calculator.run()

    captured = capsys.readouterr()

    assert "Invalid operation." in captured.out


@patch(
    "builtins.input",
    side_effect=["divide", "5", "0", "exit"]
)
def test_run_divide_by_zero(
    mock_input, capsys
):
    calculator = Calculator()

    calculator.run()

    captured = capsys.readouterr()

    assert "Cannot divide by zero" in captured.out