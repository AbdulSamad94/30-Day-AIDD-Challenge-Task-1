from .tokenizer import Tokenizer

class ShuntingYard:
    def __init__(self):
        self.operator_precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }
        self.operator_associativity = {
            '+': 'left',
            '-': 'left',
            '*': 'left',
            '/': 'left'
        }

    def convert_to_rpn(self, tokens):
        output_queue = []
        operator_stack = []

        for token_type, token_value in tokens:
            if token_type == 'NUMBER':
                output_queue.append(token_value)
            elif token_type == 'OPERATOR':
                while operator_stack and operator_stack[-1][0] == 'OPERATOR' and \
                        ((self.operator_associativity[token_value] == 'left' and \
                          self.operator_precedence[token_value] <= self.operator_precedence[operator_stack[-1][1]]) or \
                         (self.operator_associativity[token_value] == 'right' and \
                          self.operator_precedence[token_value] < self.operator_precedence[operator_stack[-1][1]])):
                    output_queue.append(operator_stack.pop()[1])
                operator_stack.append((token_type, token_value))
            elif token_type == 'LPAREN':
                operator_stack.append((token_type, token_value))
            elif token_type == 'RPAREN':
                while operator_stack and operator_stack[-1][0] != 'LPAREN':
                    output_queue.append(operator_stack.pop()[1])
                if not operator_stack:
                    raise ValueError("Mismatched parentheses: No matching left parenthesis")
                operator_stack.pop() # Pop the left parenthesis

        while operator_stack:
            if operator_stack[-1][0] == 'LPAREN':
                raise ValueError("Mismatched parentheses: No matching right parenthesis")
            output_queue.append(operator_stack.pop()[1])

        return output_queue

if __name__ == 'main':
    tokenizer = Tokenizer()
    shunting_yard = ShuntingYard()

    expressions = [
        "1 + 2 * (3 - 4) / 5",
        "10/2 + 3.5",
        "(5 + 2) * 3",
        "123",
        "2+3",
        "(1 + 2", # Invalid
        "1 + 2)" # Invalid
    ]

    for expr in expressions:
        print(f"Processing: '{expr}'")
        try:
            tokens = tokenizer.tokenize(expr)
            rpn_tokens = shunting_yard.convert_to_rpn(tokens)
            print(f"RPN: {rpn_tokens}")
        except ValueError as e:
            print(f"Error: {e}")
        print("-" * 20)
