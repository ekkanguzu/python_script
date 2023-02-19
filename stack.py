def create_stack():  # Create a stack
    stack = []
    return stack


def check_empty(stack):  # Checking if stack is empty
    return len(stack) == 0


def push(stack, item):  # Add items to stack
    stack.append(item)
    print(f'Pushed item: {item}')


def pop(stack):  # Remove an element from stack
    if check_empty(stack):
        raise 'stack is empty'
    return stack.pop()


try:
    stack = create_stack()
    push(stack, 1)
    push(stack, 2)
    push(stack, 3)
    print()
    print(f'Popped item: {stack.pop()}')
    print(f'Popped item: {stack.pop()}')
    print(f'Popped item: {stack.pop()}')
    print(f'Popped item: {stack.pop()}')
    print()


except:
    print()
    if check_empty(stack):
        print(f'Stack is empty')
    print()
print(f'Stack after popping an element: {str(stack)}')
