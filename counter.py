from collections import Counter
name = "aaaaabbc"
my_counter = Counter(name)
print(my_counter)
#returns the count as key value pairs

print(my_counter.items())
#returns the key value pairs in list where the induvidual elements are tuples
#also the .keys(), .values() functions returns keys and values in a list.

print(my_counter.most_common(1))
#returns the most common letter and its count as a tuple in a list

print(my_counter.most_common(3))
#returns the 3 most common letters and their respective counts as tuples in a list.

print(my_counter.most_common(1)[0][0])
#used to get the most common letter in that string.

print(list(my_counter.elements()))
#returns the elements of that string.