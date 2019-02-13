class Student:
    def __init__(self, name, school):
        self.name = name 
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    
    @classmethod
    def go_to_school(cls):
        print("I'm going to school")
        print("I'm a {}".format(cls))
    
dude = Student("dude","MIT")
dude.marks.append(99)
dude.marks.append(55)
dude2 = Student('Dude', "MIT")
dude2.go_to_school()
print(dude.average())
