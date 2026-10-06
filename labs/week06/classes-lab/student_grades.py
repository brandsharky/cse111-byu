class StudentGrades:
    """
    Tracks students' names and grades in a dictionary.
    >>> grades = StudentGrades()
    >>> grades.add_student("Maya")
    Added student: Maya
    >>> grades.record_grade("Maya", 88)
    Recorded grade 88 for Maya
    >>> grades.record_grade("Maya", 92)
    Recorded grade 92 for Maya
    >>> grades.get_average("Maya")
    Maya's average grade is 90.00
    >>> grades.add_student("Leo")
    Added student: Leo
    >>> grades.get_average("Leo")
    Leo has no grades recorded.
    >>> grades.record_grade("Leo", 75)
    Recorded grade 75 for Leo
    """
    def __init__(self):
        self.students = {}


    def add_student(self, name):
        if name in name.students:
            print(f"{name} is already in the system.")
        else:
            self.students[name] = []
            print(f"Added student: {name}")


    def record_grade(self, name, grade):
        if name not in self.students:
            print(f"{name} is not in the system. Add them first.")
        else:
            self.students[name].append(grade)
            print(f"Recorded grade {grade} for {name}")


    def get_average(self, name):
        if name not in self.students:
            print(f"{name} is not in the system.")
        elif not self.students[name]:
            print(f"{name} has no grades recorded.")
        else:
            scores = self.students[name]
            avg = sum(scores) / len(scores)
            print(f"{name}'s average grade is {avg:.2f}")