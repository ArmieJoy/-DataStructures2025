# First Linked-List Example
# Creating nodes
node1 = {'data': 27, 'next': None}
node2 = {'data': 18, 'next': None}
node3 = {'data': 9, 'next': None}

# Linking nodes
node1['next'] = node2
node2['next'] = node3

# Display the linked list
current = node1
while current:
    print(current['data'], end=" -> ")
    current = current['next']
print("None\n")

# Search for a value
target = 18
current = node1
found = False
while current:
    if current['data'] == target:
        found = True
        break
    current = current['next']
print(f"Found {target}: {found}\n")

# Delete a value
target = 18
current = node1
previous = None
while current:
    if current['data'] == target:
        if previous:
            previous['next'] = current['next']
        else:
            node1 = current['next']
        break
    previous = current
    current = current['next']

# Display the linked list after deletion
current = node1
while current:
    print(current['data'], end=" -> ")
    current = current['next']
print("None")
