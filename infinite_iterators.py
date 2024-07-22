from itertools import count, cycle, repeat
for i in count(7):
    if i>7:
        break
    print(i)
a = [1,2,3]
for i in cycle(a):
    print(i)
    break
#similarly repeat function repeats the iteration u want infintiely. one can also control the number of times they want to repeat the iteration by using repeat(iteration, count).

