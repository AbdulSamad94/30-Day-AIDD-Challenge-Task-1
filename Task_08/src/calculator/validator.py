import re

class Validator:
    def validate(self, expression):
        if not expression or not expression.strip():
            raise ValueError("Expression cannot be empty")

        # Check for invalid characters (anything not a digit, operator, parenthesis, or whitespace)
        # The tokenizer will handle specific syntax errors, this is for initial broad checks
        # Using the same token patterns as tokenizer, but for inverse checking
        valid_chars_pattern = r"^[\d\.\+\-\*/\(\)\s]+$"
        if not re.match(valid_chars_pattern, expression):
            # Find the first invalid character for a more specific error message
            invalid_char_match = re.search(r"[^\d\.\+\-\*/\(\)\s]", expression)
            if invalid_char_match:
                invalid_char = invalid_char_match.group(0)
                pos = invalid_char_match.start()
                raise ValueError(f"Invalid character '{invalid_char}' at position {pos}")
            else:
                raise ValueError("Expression contains invalid characters")
        return True

if __name__ == '__main__':
    validator = Validator()

    test_expressions = [
        "1 + 2 * 3",
        "(10 - 5) / 2",
        "123.45",
        "", # Empty
        "   ", # Whitespace only
        "1 + abc", # Invalid character
        "1 & 2"
    ]

    for expr in test_expressions:
        print(f"Validating: '{expr}'")
        try:
            validator.validate(expr)
            print("Validation: Passed")
        except ValueError as e:
            print(f"Validation: Failed - {e}")
        print("-" * 20)
