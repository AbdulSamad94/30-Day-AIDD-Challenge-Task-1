from .calculator.calculator import calculate


def main():
    print("Simple Interactive Calculator")
    print("Enter 'quit' to exit.")

    while True:
        try:
            expression = input("Enter expression: ")
            if expression.lower() == "quit":
                break

            result = calculate(expression)

            print(f"Result: {result}")
            print("-" * 20)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("-" * 20)

    print("Exiting calculator. Goodbye!")


if __name__ == "__main__":
    main()
