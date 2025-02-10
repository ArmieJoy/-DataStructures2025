# Second Array Example
# Initializing an array of animals
animals = ["Lion", "Tiger", "Elephant", "Giraffe", "Zebra"]

# Accessing elements in the array
print("\nFirst animal:", animals[0])
print("\nLast animal:", animals[-1])

# Updating elements in the array
animals[1] = "Panther"
print("\nUpdated animals:", animals)

# Adding elements to the array
animals.append("Kangaroo")
print("\nArray after adding an animal:", animals)

# Removing elements from the array
animals.remove("Elephant")
print("\nArray after removing an animal:", animals)

# Iterating through the array using a loop
print("\nIterating through animals:")
for animal in animals:
    print(animal)

# Slicing the array
top_three_animals = animals[:3]
print("\nTop three animals:", top_three_animals)

# Reversing the array
reversed_animals = animals[::-1]
print("\nReversed array of animals:", reversed_animals)

# Length of the array
array_length = len(animals)
print("\nLength of the array:", array_length)
