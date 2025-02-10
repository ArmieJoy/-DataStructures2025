# Initialize the queue
queue = []

# Enqueue names onto the queue
queue.append('Armin')
queue.append('Levi')
queue.append('Eren')

# Print the initial queue
print("Initial queue:")
print(queue)

# Dequeue a name from the queue
dequeued_name = queue.pop(0)
print("\nDequeued name:", dequeued_name)

# Enqueue another name onto the queue
queue.append('Jenny')

# Print the queue after dequeuing and enqueuing
print("\nQueue after dequeuing and enqueuing 'Jenny':")
print(queue)
