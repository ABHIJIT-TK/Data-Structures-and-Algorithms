def insert_sorted(stack, item):
    if not stack or stack[-1] <= item:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_sorted(stack, item)
        stack.append(temp)

def sort_stack(stack):
    if not stack:
        return
    temp = stack.pop()
    sort_stack(stack)
    insert_sorted(stack, temp)

# Example usage
stack = [4, 2, 5, 1, 3]
sort_stack(stack)
print(stack)
