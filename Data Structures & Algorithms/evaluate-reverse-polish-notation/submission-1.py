class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {'*','/','+','-'}
        stack = []
        for k in tokens:
            if k not in operands:
                stack.append(int(k))
            else:
                operandB = stack.pop()
                operandA = stack.pop()
                stack.append(self.applyOperator(k, operandA, operandB))
        if len(stack) > 1:
            return -1
        else:
            return stack[0]

    def applyOperator(self, operator: str, operandA: int, operandB: int) -> int:
        if operator == '*':
            return operandA*operandB
        if operator == '/':
            return int(operandA/operandB)
        if operator == '+':
            return operandA+operandB
        if operator == '-':
            return operandA-operandB


