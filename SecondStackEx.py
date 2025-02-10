# Second Stack Example
# Initialize the stack
stack = []

# Push elements onto the stack
stack.append('Rock')
stack.append('Jazz')
stack.append('Classical')
stack.append('Pop')
stack.append('Hip-Hop')

print("Initial stack:")
print(stack)

# Pop a musical genre from the stack
popped_genre = stack.pop()
print("\nPopped genre:", popped_genre)

print("\nStack after popping:")
print(stack)

# Peek at the top genre in the stack (last element of the list)
top_genre = stack[-1]
print("\nTop genre in the stack:", top_genre)

# Push another genre onto the stack
stack.append('Electronic')

print("\nStack after pushing 'Electronic':")
print(stack)

# Check the size of the stack
stack_size = len(stack)
print("\nSize of the stack:", stack_size)
