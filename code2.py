#S111 KRISHNA SHARMA

# Original nested tuple of bikes
nested_tuple = (
    ("Honda Shine", 103),
    ("Royal Enfield Classic 350", 101),
    ("Bajaj Pulsar", 102)
)

# Sorting the nested tuple by bike code (index 1)
sorted_bikes = sorted(nested_tuple, key=lambda x: x[1])

# Display the sorted result
print("Sorted Bikes (by bike code):", sorted_bikes)
