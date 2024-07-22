class student:
    def __init__ (self, name, major, cg): 
        self.name = name
        self.major = major
        self.cg = cg

    def honors(self):
        if self.cg >= 8.5:
            return True
        else:
            return False
 
student_1 = student ("suriya", "BT", 8.5)
print(student_1.name)
print(student_1.major)
print(student_1.honors())
    