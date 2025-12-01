from .calculator.calculator import calculate


def main():
    print("Simple Interactive Calculator")
    print("Enter 'quit' to exit.")

    while True:
        try:
            num1_str = input("Enter first number: ")
            if num1_str.lower() == "quit":
                break
            num1 = float(num1_str)

            operator = input("Enter operator (+, -, *, /): ")
            if operator.lower() == "quit":
                break
            if operator not in ["+", "-", "*", "/"]:
                print("Invalid operator. Please enter one of +, -, *, /.")
                continue

            num2_str = input("Enter second number: ")
            if num2_str.lower() == "quit":
                break
            num2 = float(num2_str)

            expression = f"{num1} {operator} {num2}"
            result = calculate(expression)

            print(f"Result: {result}")
            print("-" * 20)

        except ValueError:
            print("Invalid number entered. Please enter a numeric value.")
            print("-" * 20)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("-" * 20)

    print("Exiting calculator. Goodbye!")


if __name__ == "__main__":
    main()
