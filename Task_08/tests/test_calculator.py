import unittest
from src.calculator.tokenizer import Tokenizer
from src.calculator.shunting_yard import ShuntingYard
from src.calculator.rpn_evaluator import RPNEvaluator
from src.calculator.validator import Validator
from src.calculator.calculator import calculate

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_basic_tokenization(self):
        expression = "1 + 2 * (3 - 4) / 5"
        expected_tokens = [
            ('NUMBER', '1'), ('OPERATOR', '+'), ('NUMBER', '2'), ('OPERATOR', '*'),
            ('LPAREN', '('), ('NUMBER', '3'), ('OPERATOR', '-'), ('NUMBER', '4'), ('RPAREN', ')'),
            ('OPERATOR', '/'), ('NUMBER', '5')
        ]
        self.assertEqual(self.tokenizer.tokenize(expression), expected_tokens)

    def test_whitespace_handling(self):
        expression = "  10   /   2.5  "
        expected_tokens = [
            ('NUMBER', '10'), ('OPERATOR', '/'), ('NUMBER', '2.5')
        ]
        self.assertEqual(self.tokenizer.tokenize(expression), expected_tokens)

    def test_single_number(self):
        expression = "123.45"
        expected_tokens = [('NUMBER', '123.45')]
        self.assertEqual(self.tokenizer.tokenize(expression), expected_tokens)

    def test_invalid_character(self):
        expression = "1 + $2"
        with self.assertRaises(ValueError) as cm:
            self.tokenizer.tokenize(expression)
        self.assertIn("Invalid character", str(cm.exception))

    def test_empty_expression(self):
        expression = ""
        expected_tokens = []
        self.assertEqual(self.tokenizer.tokenize(expression), expected_tokens)

class TestShuntingYard(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()
        self.shunting_yard = ShuntingYard()

    def test_basic_conversion(self):
        tokens = self.tokenizer.tokenize("3 + 4 * 2")
        expected_rpn = ['3', '4', '2', '*', '+']
        self.assertEqual(self.shunting_yard.convert_to_rpn(tokens), expected_rpn)

    def test_precedence_and_parentheses(self):
        tokens = self.tokenizer.tokenize("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3") # Note: ^ is not supported yet, but test parentheses
        tokens = self.tokenizer.tokenize("1 + 2 * (3 - 4) / 5")
        expected_rpn = ['1', '2', '3', '4', '-', '*', '5', '/', '+']
        self.assertEqual(self.shunting_yard.convert_to_rpn(tokens), expected_rpn)

    def test_mismatched_parentheses_left(self):
        tokens = self.tokenizer.tokenize("(1 + 2")
        with self.assertRaises(ValueError) as cm:
            self.shunting_yard.convert_to_rpn(tokens)
        self.assertIn("Mismatched parentheses", str(cm.exception))

    def test_mismatched_parentheses_right(self):
        tokens = self.tokenizer.tokenize("1 + 2)")
        with self.assertRaises(ValueError) as cm:
            self.shunting_yard.convert_to_rpn(tokens)
        self.assertIn("Mismatched parentheses", str(cm.exception))

class TestRPNEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = RPNEvaluator()

    def test_basic_evaluation(self):
        rpn = ['3', '4', '2', '*', '+'] # 3 + 4 * 2 = 11
        self.assertEqual(self.evaluator.evaluate(rpn), 11.0)

    def test_complex_evaluation(self):
        rpn = ['1', '2', '3', '4', '-', '*', '5', '/', '+'] # 1 + 2 * (3 - 4) / 5 = 0.6
        self.assertEqual(self.evaluator.evaluate(rpn), 0.6)

    def test_division_by_zero(self):
        rpn = ['10', '0', '/']
        with self.assertRaises(ZeroDivisionError):
            self.evaluator.evaluate(rpn)

    def test_invalid_rpn_too_many_operators(self):
        rpn = ['1', '2', '+', '-']
        with self.assertRaises(ValueError) as cm:
            self.evaluator.evaluate(rpn)
        self.assertIn("too many operands or operators", str(cm.exception))

    def test_invalid_rpn_not_enough_operands(self):
        rpn = ['+', '1', '2']
        with self.assertRaises(ValueError) as cm:
            self.evaluator.evaluate(rpn)
        self.assertIn("not enough operands", str(cm.exception))

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_valid_expressions(self):
        self.assertTrue(self.validator.validate("1 + 2 * 3"))
        self.assertTrue(self.validator.validate("(10 - 5) / 2"))
        self.assertTrue(self.validator.validate("123.45"))

    def test_empty_expression(self):
        with self.assertRaises(ValueError) as cm:
            self.validator.validate("")
        self.assertIn("Expression cannot be empty", str(cm.exception))

    def test_whitespace_only_expression(self):
        with self.assertRaises(ValueError) as cm:
            self.validator.validate("   ")
        self.assertIn("Expression cannot be empty", str(cm.exception))

    def test_invalid_characters(self):
        with self.assertRaises(ValueError) as cm:
            self.validator.validate("1 + $2")
        self.assertIn("Invalid character '$'", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            self.validator.validate("1 & 2")
        self.assertIn("Invalid character '&'", str(cm.exception))

class TestCalculateFunction(unittest.TestCase):
    def test_valid_calculations(self):
        self.assertEqual(calculate("1 + 2 * (3 - 4) / 5"), 0.6)
        self.assertEqual(calculate("10/2 + 3.5"), 8.5)
        self.assertEqual(calculate("(5 + 2) * 3"), 21.0)
        self.assertEqual(calculate("123"), 123.0)
        self.assertEqual(calculate("2+3"), 5.0)

    def test_division_by_zero_error(self):
        self.assertIn("Division by zero", calculate("10/0"))

    def test_invalid_syntax_error(self):
        self.assertIn("Invalid character", calculate("2+*3"))

    def test_mismatched_parentheses_error(self):
        self.assertIn("Mismatched parentheses", calculate("(1 + 2"))

    def test_empty_expression_error(self):
        self.assertIn("Expression cannot be empty", calculate(""))

    def test_invalid_character_error_in_calculate(self):
        self.assertIn("Invalid character '$'", calculate("1 + $2"))

if __name__ == '__main__':
    unittest.main()
