"""
Simple Calculator CLI Application
Performs basic arithmetic operations (+, -, *, /) with input validation.
"""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the division of a by b. Raises ZeroDivisionError if b == 0."""
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    return a / b


def format_number(val: float) -> str:
    """Format float cleanly (e.g., 5.0 -> '5', 5.25 -> '5.25')."""
    if val.is_integer():
        return str(int(val))
    return f"{val:.6g}"


def get_number(prompt: str) -> float:
    """Prompt user for a valid number, repeating until valid input is given."""
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")


def display_menu():
    """Display the operation menu."""
    print("\n" + "=" * 30)
    print("      SIMPLE CALCULATOR       ")
    print("=" * 30)
    print("Select an operation:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Exit")
    print("=" * 30)


def calculate(choice: str, num1: float, num2: float):
    """Perform operation based on choice and print result."""
    operations = {
        "1": ("+", add),
        "+": ("+", add),
        "add": ("+", add),
        "2": ("-", subtract),
        "-": ("-", subtract),
        "sub": ("-", subtract),
        "subtract": ("-", subtract),
        "3": ("*", multiply),
        "*": ("*", multiply),
        "mul": ("*", multiply),
        "multiply": ("*", multiply),
        "4": ("/", divide),
        "/": ("/", divide),
        "div": ("/", divide),
        "divide": ("/", divide),
    }

    key = choice.lower().strip()
    if key not in operations:
        print("Invalid choice! Please choose a valid operation from the menu.")
        return False

    symbol, func = operations[key]

    try:
        result = func(num1, num2)
        print(f"\nResult: {format_number(num1)} {symbol} {format_number(num2)} = {format_number(result)}")
        return True
    except ZeroDivisionError as e:
        print(f"\n{e}")
        return False


def main():
    """Main application loop."""
    print("Welcome to Simple Calculator!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5 or +, -, *, /): ").strip()

        if choice in ("5", "exit", "quit", "q"):
            print("\nThank you for using Simple Calculator. Goodbye!")
            break

        if choice.lower() not in ("1", "+", "add", "2", "-", "sub", "subtract", "3", "*", "mul", "multiply", "4", "/", "div", "divide"):
            print("\nInvalid selection. Please choose an option from 1 to 5.")
            continue

        num1 = get_number("\nEnter the first number: ")
        num2 = get_number("Enter the second number: ")

        calculate(choice, num1, num2)

        # Ask if the user wants to continue
        again = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nThank you for using Simple Calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
