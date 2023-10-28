#craeting an empty
b = set()
print(type(b))

# adding value to an empty sett
b.add(4)
b.add(4)
b.add(4)
b.add(5)
b.add(5)
b.add((5, 5, 6))  # you can print tuple in sets
# b.add({4:5})  # cannot add list or dictionary to sets

# print(b)
# b.remove(5)  # removes 5 from set.
# print(len(b)) #prints the length of the sett
# print(b)


print(b.pop())
print(b)