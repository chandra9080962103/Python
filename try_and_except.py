try:
    print ("hello" + 1)
except:
    print("world must be written in string")

try:
    print("hello" + 2)
except Exception as a:
    print(a)

try:
    print(5 + "a")
    print(3/0)
except TypeError:
    print("hello")
except ZeroDivisionError:
    print("hi")

else:
    print("no exceptions")
finally:
    print("cleaning up..")
#finally clause even if there is an exception.
    

