# a. Create a tuple with 5 different elements and print it
bikes = ("Honda Shine", "Bajaj Pulsar", "TVS Apache", "Royal Enfield", "Yamaha R15")
print("a. Tuple:", bikes)

# b. Access the first and last elements using indexing
print("\nb. First element:", bikes[0])
print("   Last element:", bikes[-1])

# c. Slice a tuple and print the middle 3 elements
print("\nc. Middle 3 elements:", bikes[1:4])

# d. Concatenate two tuples and print the result
more_bikes = ("KTM Duke", "Hero Splendor")
#S111 KRISHNA SHARMA

combined_bikes = bikes + more_bikes
print("\nd. Concatenated Tuple:", combined_bikes)

# e. Reverse a tuple using slicing
print("\ne. Reversed Tuple:", bikes[::-1])

# f. Count how many times an element appears in a tuple
numbers = (10, 20, 30, 20, 40, 20)
print("\nf. Count of 20:", numbers.count(20))

# g. Find the index of a specific element in a tuple
print("\ng. Index of 'TVS Apache':", bikes.index("TVS Apache"))

# h. Check if an element exists in a tuple
element = "Yamaha R15"
if element in bikes:
    print("\nh.", element, "exists in the tuple.")
else:
    print("\nh.", element, "does not exist in the tuple.")

# i. Convert a list to a tuple
bike_list = ["KTM Duke", "Hero Splendor", "Suzuki Gixxer"]
bike_tuple = tuple(bike_list)
print("\ni. Converted Tuple:", bike_tuple)

# j. Sort a tuple of numbers in ascending order
num_tuple = (50, 10, 40, 20, 30)
sorted_tuple = tuple(sorted(num_tuple))
print("\nj. Sorted Tuple:", sorted_tuple)

# k. Repeat a tuple 3 times using the * operator
print("\nk. Repeated Tuple:", ("Bike",) * 3)

# l. Check the immutability property of tuples
bike = ("Royal Enfield", 101)

try:
    bike[1] = 999
except TypeError as e:
    print("\nl. Tuple is immutable! Error:", e)
