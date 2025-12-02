class RPNEvaluator:
    def evaluate(self, rpn_tokens):
        operand_stack = []

        for token in rpn_tokens:
            if self._is_number(token):
                operand_stack.append(float(token))
            elif self._is_operator(token):
                if len(operand_stack) < 2:
                    raise ValueError("Invalid RPN expression: not enough operands for operator")
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = self._apply_operator(operand1, operand2, token)
                operand_stack.append(result)
            else:
                raise ValueError(f"Unknown token in RPN expression: {token}")

        if len(operand_stack) != 1:
            raise ValueError("Invalid RPN expression: too many operands or operators")

        return operand_stack[0]

    def _is_number(self, token):
        try:
            float(token)
            return True
        except ValueError:
            return False

    def _is_operator(self, token):
        return token in ('+', '-', '*', '/')

    def _apply_operator(self, operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ZeroDivisionError("Division by zero")
            return operand1 / operand2
        else:
            raise ValueError(f"Unknown operator: {operator}")

if __name__ == '__main__':
    evaluator = RPNEvaluator()

    # Test cases in RPN
    rpn_expressions = [
        ['1', '2', '3', '4', '-', '*', '5', '/', '+'], # 1 + 2 * (3 - 4) / 5 = 0.6
        ['10', '2', '/', '3.5', '+'], # 10/2 + 3.5 = 8.5
        ['5', '2', '+', '3', '*'], # (5 + 2) * 3 = 21
        ['123'],
        ['2', '3', '+'], # 2 + 3 = 5
        ['10', '0', '/'], # Division by zero
        ['1', '2', '+', '-'], # Invalid - too many operators
        ['1', '2'], # Invalid - too many operands
    ]

    for rpn_expr in rpn_expressions:
        print(f"Evaluating RPN: {rpn_expr}")
        try:
            result = evaluator.evaluate(rpn_expr)
            print(f"Result: {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        print("-" * 20)
