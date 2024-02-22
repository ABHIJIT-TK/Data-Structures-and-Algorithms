def remove_middle(stack, n, current=0):
    if current == n // 2:
        stack.pop()
        return
    temp = stack.pop()
    remove_middle(stack, n, current + 1)
    stack.append(temp)

def remove_middle_element(stack):
    n = len(stack)
    if n == 0:
        return
    remove_middle(stack, n)

# Example usage
stack = [1, 2, 3, 4, 5]
remove_middle_element(stack)
print(stack)
