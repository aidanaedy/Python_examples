x = 1
# list, tuple, dictionary, frozenset, set

age = 'two'
print (type(age))

number = float(1)
print (type(number))

number_and_age = (number, age)
print(number_and_age)

our_list = ["a", "b", "c", 1.5]
print (our_list)

our_tuple = ("a","b","c")
print (our_tuple)

our_dictionary = {"name": "Derrick", "Height": "6.0"}
print (our_dictionary)

our_set = {"one", "two", "three", "two"}
print(our_set)

our_frozenset = frozenset(our_set)
print(our_frozenset)