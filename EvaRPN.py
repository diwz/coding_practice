# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operands = []
        for token in tokens:
            if token not in "+-*/":
                operands.append(int(token))
            else:
                op1 = operands.pop()
                op2 = operands.pop()
                if token == "+":
                    operands.append(op1 + op2)
                elif token == "*":
                    operands.append(op1 * op2)
                elif token == "/":
                    operands.append(int(op2 * 1.0 / op1))
                elif token == "-":
                    operands.append(op2 - op1)
        return operands.pop()
