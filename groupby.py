from itertools import groupby
def prime_number(x):
    for i in range(2,x):
        if x%i != 0:
            return True
        else:
            return False
a = [2,4,6,8,13,10,12,14,16]
group_obj = groupby(a, key = prime_number)
#alternatively one can also use lambda x: (condtion). but cant be used for complex ones like above.
for key, value in group_obj:
    print(key, list(value))