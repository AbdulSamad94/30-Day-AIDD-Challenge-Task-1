from .tokenizer import Tokenizer
from .shunting_yard import ShuntingYard
from .rpn_evaluator import RPNEvaluator
from .validator import Validator


def calculate(expression: str):
    try:
        validator = Validator()
        validator.validate(expression)

        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize(expression)

        shunting_yard = ShuntingYard()
        rpn_tokens = shunting_yard.convert_to_rpn(tokens)

        evaluator = RPNEvaluator()
        result = evaluator.evaluate(rpn_tokens)

        return result
    except (ValueError, ZeroDivisionError) as e:
        return str(e)


if __name__ == "__main__":
    # Test cases
    expressions = [
        "1 + 2 * (3 - 4) / 5",  # Expected: 0.6
        "10/2 + 3.5",  # Expected: 8.5
        "(5 + 2) * 3",  # Expected: 21.0
        "123",  # Expected: 123.0
        "2+3",  # Expected: 5.0
        "10/0",  # Expected: Division by zero
        "2+*3",  # Expected: Invalid character / syntax error
        "(1 + 2",  # Expected: Mismatched parentheses
        "",  # Expected: Expression cannot be empty
        "abc + 1",
    ]

    for expr in expressions:
        print(f"Calculating '{expr}'")
        result = calculate(expr)
        print(f"Result: {result}")
        print("-" * 20)
