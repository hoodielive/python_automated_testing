class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs)


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary


zhavia = WorkingStudent('Zhavia', 'Oxford', 39.00, "Software Developer")
print(zhavia.salary)
friend = WorkingStudent.friend(zhavia, 'hoodie', 99.00, job_title="Software Developer")
print(friend.name)
print(friend.school)
