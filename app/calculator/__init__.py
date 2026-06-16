from app.calculation import CalculationFactory


class Calculator:
    """Professional calculator with REPL interface."""

    def __init__(self):
        self.history = []

    def show_help(self):
        print("\nAvailable commands:")
        print("add, subtract, multiply, divide")
        print("history - view calculation history")
        print("help - show commands")
        print("exit - quit calculator\n")

    def show_history(self):
        if not self.history:
            print("No calculations yet.")
            return

        print("\nCalculation History:")
        for item in self.history:
            print(item)

    def run(self):
        print("Welcome to the Professional Calculator!")
        print("Type 'help' for commands.")

        while True:
            command = input("\nEnter operation: ").lower()

            if command == "exit":
                print("Goodbye!")
                break

            if command == "help":
                self.show_help()
                continue

            if command == "history":
                self.show_history()
                continue

            # LBYL (Look Before You Leap)
            valid_operations = [
                "add",
                "subtract",
                "multiply",
                "divide",
            ]

            if command not in valid_operations:
                print("Invalid operation.")
                continue

            try:
                # EAFP (Easier to Ask Forgiveness than Permission)
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                calculation = CalculationFactory.create_calculation(
                    command, a, b
                )

                result = calculation.perform()

                calculation_record = (
                    f"{command}({a}, {b}) = {result}"
                )

                self.history.append(calculation_record)

                print(f"Result: {result}")

            except ValueError as error:
                print(f"Error: {error}")