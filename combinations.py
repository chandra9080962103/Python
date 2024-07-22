from itertools import combinations
a = [1,2,3]
c = combinations(a,3)
print(list(c))
#returns all possible combinations of of the elements in the list upto lenght 3
#there is also an other module combination_with_replacement which allows for combiantion of the number with itself.
