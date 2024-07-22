#lambda argument: expression (#short form of functions).
#it has many applications like sorting.
a = [(1,2,3), (5,-5,10), (9,9,9), (2,10,5)]
a_sorted = sorted (a)
print(a_sorted)
#by default it sorts based on the x values.
a_sorted = sorted (a, key = lambda x: x[2])
print(a_sorted)

#list comphrehesnion
b = [1,2,3,4,5,6]
c = [x*2 for x in b]
print (c)

#map function.
d = map(lambda x: x*2, b)
print (d)

#filter function.
e = filter(lambda x: x%2 == 0, b)
print (list(e))
#can also be done with list comphrehension.

#reduce function, always takes in 2 arguments
from functools import reduce
add = reduce(lambda x,y: x+y, b)
print (add)

