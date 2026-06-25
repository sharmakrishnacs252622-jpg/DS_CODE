#S111 KRISHNA SHARMA

# 1. Create nested tuple with subjects 
a = ("Andheri","Ram mandir","goregaon")
b = ("Nallasopara","vasai","virar")
c = ("Dahisar","miraroad","bhyandar")
d = (a,b,c)
print("nasted Tuple is",d)

# 2. Indexing 
print("First tuple is :",d[0])
print("In Frist tuple first station :",d[0][0])

# 3. Negative indexing 
print("The Last tuple negative index is :",d[-1])
print("Name of last tuple is :",d[-1][0])

print("\nAll tuple")

# 4. Loop through the nested tuple 
for e in d:
    print(f"tuple name :{e[0]},Code:{e[1]}")

# 5. Reverse the tuple
print("\nreverse Tuple :",d[::-1])

#6.slice the tuple(first two station)
print("Sliced tuple(first two station):",d[0:2])


#7. Concatenate another subject tuple
f = ("jogeshwari","dadar")
x = d+f
print("After  Concatenation:", x) 

# 8. Demonstrate immutability
try: 
 d[0][1] = 200 # Trying to change subject code 
except TypeError as y: 
 print("\nTuple Immutability Test: Error occurred ->", y)
