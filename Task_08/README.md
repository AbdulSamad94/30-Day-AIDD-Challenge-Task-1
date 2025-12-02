# Simple Calculator

A simple command-line calculator built with Python, capable of evaluating arithmetic expressions with basic operations, operator precedence, and parentheses.

## Features

- Addition, Subtraction, Multiplication, Division
- Operator Precedence (PEMDAS/BODMAS)
- Parentheses for grouping operations
- Robust error handling for invalid expressions and division by zero

## Installation

1.  **Clone the repository** (if applicable):

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Navigate to the project directory**:

    ```bash
    cd path/to/this/project
    ```

3.  **Install dependencies** (if any - none for this simple calculator):

    ```bash
    # No external dependencies for core functionality
    ```

## Usage

### Running the Command-Line Application

To run the interactive calculator from the command line, navigate to the project's root directory and execute:

```bash
python -m src.main
```

The application will then prompt you to enter numbers and operations.

### `calculate(expression: str)` function

You can also import and use the `calculate` function directly in your Python code:

```python
from src.calculator.calculator import calculate

# Example usage in your Python script
result = calculate("10 + 5")
print(result)
```


-   **Parameters**:
    -   `expression` (str): The arithmetic expression to evaluate (e.g., "1 + 2 * (3 - 4) / 5").

-   **Returns**:
    -   `float`: The numerical result of the calculation if the expression is valid.
    -   `str`: An error message if the expression is invalid or encounters an error (e.g., "Division by zero", "Invalid character").

### Example

```python
from src.calculator.calculator import calculate

# Valid expressions
print(f"Result of '1 + 2 * (3 - 4) / 5': {calculate('1 + 2 * (3 - 4) / 5')}") # Expected: 0.6
print(f"Result of '10/2 + 3.5': {calculate('10/2 + 3.5')}")             # Expected: 8.5
print(f"Result of '(5 + 2) * 3': {calculate('(5 + 2) * 3')}")             # Expected: 21.0

# Invalid expressions
print(f"Result of '10/0': {calculate('10/0')}")                         # Expected: Division by zero
print(f"Result of '2+*3': {calculate('2+*3')}")                         # Expected: Invalid character / syntax error
print(f"Result of '(1 + 2': {calculate('(1 + 2')}")                     # Expected: Mismatched parentheses
```

## Running Tests

To run the unit tests, navigate to the project's root directory and execute:

```bash
python -m unittest tests/test_calculator.py
```
