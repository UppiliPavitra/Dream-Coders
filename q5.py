#Title Name: Dream Coders
def calculate(expression: str) -> float:
    expression = expression.replace(" ", "") 
    stack = []
    num = 0
    sign = '+'
    for i in range(len(expression)):
        char = expression[i]
        if char.isdigit():
            num = num * 10 + int(char)
        if char in '+-*/' or i == len(expression) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] = stack[-1] * num
            elif sign == '/':
                stack[-1] = stack[-1] / num
            sign = char
            num = 0
    return float (round(sum(stack), 2))
expression = input()
result = calculate(expression)
print(result)
