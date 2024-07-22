from collections import deque
d = deque()
#use all the list functions to add/remove elements from both sides of the list
d.append(2)
d.append(10)
d.appendleft(9)
d.remove(2)
d.rotate(1)
#rotates all the elements one index to the right
print(d)