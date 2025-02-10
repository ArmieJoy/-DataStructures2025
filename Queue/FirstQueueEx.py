# First Queue Example
# Initialize the queue
queue = []

# Enqueue flowers onto the queue
queue.append('Rose')
queue.append('Tulip')
queue.append('Lily')
queue.append('Daisy')
queue.append('Orchid')

print("Initial queue:")
print(queue)

# Dequeue a flower from the queue
dequeued_flower = queue.pop(0)
print("\nDequeued flower:", dequeued_flower)

print("\nQueue after dequeuing:")
print(queue)

# Peek at the front flower in the queue (first element of the list)
front_flower = queue[0]
print("\nFront flower in the queue:", front_flower)

# Enqueue another flower onto the queue
queue.append('Sunflower')

print("\nQueue after enqueuing 'Sunflower':")
print(queue)

# Check the size of the queue
queue_size = len(queue)
print("\nSize of the queue:", queue_size)
