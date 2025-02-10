# First Array Example
# Initializing an array of Japanese places
japanese_places = ["Tokyo", "Kyoto", "Osaka", "Hokkaido", "Nara"]

# Accessing elements in the array
print("\nFirst place:", japanese_places[0])
print("\nLast place:", japanese_places[-1])

# Updating elements in the array
japanese_places[1] = "Hiroshima"
print("\nUpdated places:", japanese_places)

# Adding elements to the array
japanese_places.append("Nagoya")
print("\nArray after adding a place:", japanese_places)

# Removing elements from the array
japanese_places.remove("Osaka")
print("\nArray after removing a place:", japanese_places)
