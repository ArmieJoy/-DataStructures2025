# Second Linked-List Example
# Creating nodes
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Linking nodes
linked_list = [{'data': season, 'next': None} for season in seasons]
for i in range(len(linked_list) - 1):
    linked_list[i]['next'] = linked_list[i + 1]

# Display the linked list
current = linked_list[0]
while current:
    if current['next']:
        print(current['data'], end=" -> ")
    else:
        print(current['data'], end=" -> None")
    current = current['next']
print("\n")

# Search for a value
target = 'Summer'
found = any(node['data'] == target for node in linked_list)
print(f"Found {target}: {found}\n")

# Delete a value
target = 'Autumn'
for i, node in enumerate(linked_list):
    if node['data'] == target:
        if i > 0:
            linked_list[i - 1]['next'] = node['next']
        else:
            linked_list = linked_list[1:]
        break

# Display the linked list after deletion
current = linked_list[0]
while current:
    if current['next']:
        print(current['data'], end=" -> ")
    else:
        print(current['data'], end=" -> None")
    current = current['next']
print("\n")
