from itertools import accumulate
import operator
a = [1,2,3,4]
print (list(accumulate(a)))
#accumalating the iteration elements within themselves.
acc = accumulate (a, func = operator.mul)
print(list(acc))
#returns the elements multiplied within themselves after every iteration.
b = [1,9,5,7,3]
print(list(accumulate(b, func = max)))
#when max value is found at a certain iteration, its continued for every other iteration from there on.
