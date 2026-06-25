# a. Find the largest number in a list
numbers = [10, 25, 8, 45, 30]
print("a. Largest number:", max(numbers))

# b. Remove duplicates from a list
dup_list = [10, 20, 10, 30, 20, 40]
unique_list = list(set(dup_list))
print("\nb. List after removing duplicates:", unique_list)

# c. Count how many even numbers are in a list
num_list = [1, 2, 3, 4, 5, 6, 8]
even_count = 0

for num in num_list:
    if num % 2 == 0:
        even_count += 1

print("\nc. Number of even numbers:", even_count)

# d. Input 5 numbers and store them in a list
input_list = []

for i in range(5):
    num = int(input("Enter a number: "))
    input_list.append(num)

print("\nd. List entered by user:", input_list)

# e. Function to return the average of all numbers in a list
def average(lst):
    return sum(lst) / len(lst)

avg = average(numbers)
print("\ne. Average of the list:", avg)

# f. Convert a string into a list of characters using list()
text = "Python"
char_list = list(text)
print("\nf. List of characters:", char_list)

# g. Join all elements of a list into a single string using join()
words = ["Python", "for", "Data", "Science"]
joined_string = " ".join(words)
print("\ng. Joined String:", joined_string)
