set_a = {"one","two","three"}
set_a.add("four")

print(set_a)

set_a.update(["five","six","seven"])

print(set_a)

set_a.remove("six")
print(set_a)

# if you try and remove item called six again, the program would creat an error, so use discard instead, 
# it would still not be able to remove the value "six", but would not create an error

set_a.discard("six")
print(set_a)

# pop below removes the first element in the set, but as they are not ordered in a set, you cannot be sure 
# which one is being removed, so it is dangerous to use pop in a set
set_a.pop()

print(set_a)


# frozenset changes the set to a frozen set with unmutable values, so you cannot then .update, .remove etc.
f_set_a = frozenset(set_a)

print(set_a)

set_a.pop()
print(set_a)