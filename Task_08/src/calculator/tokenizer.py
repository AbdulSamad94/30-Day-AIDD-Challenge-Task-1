import re

class Tokenizer:
    def __init__(self):
        self.tokens = []
        self.current_token_index = 0
        self.token_patterns = {
            'NUMBER': r'\d+(\.\d*)?',
            'OPERATOR': r'[\+\-\*/]',
            'LPAREN': r'\\(',
            'RPAREN': r'\\)',
            'WHITESPACE': r'\s+'
        }
        self.token_regex = self._compile_token_regex()

    def _compile_token_regex(self):
        # Sort patterns by length in reverse to match longer patterns first (e.g., multi-char operators if any)
        # For now, all our patterns are single character or number patterns, so order doesn't strictly matter
        # but it's good practice for future extensions.
        patterns = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_patterns.items())
        return re.compile(patterns)

    def tokenize(self, expression):
        self.tokens = []
        self.current_token_index = 0
        pos = 0
        while pos < len(expression):
            match = self.token_regex.match(expression, pos)
            if not match:
                raise ValueError(f"Invalid character at position {pos}: {expression[pos]}")

            token_type = match.lastgroup
            token_value = match.group(token_type)

            if token_type != 'WHITESPACE':
                self.tokens.append((token_type, token_value))

            pos = match.end(0)
        return self.tokens

    def peek(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None

    def consume(self):
        if self.current_token_index < len(self.tokens):
            token = self.tokens[self.current_token_index]
            self.current_token_index += 1
            return token
        return None

if __name__ == '__main__':
    tokenizer = Tokenizer()

    # Test cases
    expressions = [
        "1 + 2 * (3 - 4) / 5",
        "10/2 + 3.5",
        "(5 + 2) * 3",
        "123",
        "  1 +   2 ",
        "2+3",
        "10/0"
    ]

    for expr in expressions:
        print(f"Tokenizing: '{expr}'")
        try:
            tokens = tokenizer.tokenize(expr)
            print(f"Tokens: {tokens}")
        except ValueError as e:
            print(f"Error: {e}")
        print("-" * 20)
