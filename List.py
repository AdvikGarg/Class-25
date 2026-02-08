n=[1,7,5,4,9,2]
odd=[a for a in n if a%2!=0]
print("List of odd numbers from original\n:",odd)

f=['apple','banana','orange','strawberry','kiwi']
f2 = [a.capitalize() for a in f]

print("Original:", f)
print("Updated: ", f2)
