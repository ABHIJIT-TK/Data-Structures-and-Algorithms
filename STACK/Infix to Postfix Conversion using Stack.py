def infix_to_postfix(expression):
    # Function to return precedence of operators
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        if op == '^':
            return 3
        return 0

    # Initialize an empty stack and an empty output list
    stack = []
    output = []

    for char in expression:
        if char.isalnum():  # If the character is an operand (letter or digit)
            output.append(char)
        elif char == '(':  # If the character is '('
            stack.append(char)
        elif char == ')':  # If the character is ')'
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '('
        else:  # If an operator is encountered
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)

    # Pop all the operators from the stack
    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Example usage
infix_expr = "a+b*(c^d-e)^(f+g*h)-i"
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)  # Output: abcd^e-fgh*+^*+i-
