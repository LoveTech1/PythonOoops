class Student:
    # Write your code here.

    all_students = []

    def __init__(self, name, grade):
        # Write your code here.
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    # Write your code here.

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,grade):
        if self._grade < 0 or self._grade > 100:
            raise ValueError()

        self._grade = grade


    @staticmethod
    def calculate_average_grade(students):
        if len(students) < 0:
            return -1

        total = 0

        for student in students:
            total += student.grade

        return total / len(students) 


    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_students)

    @classmethod
    def get_best_student(cls):
        current_best_student = None

        for student in cls.all_students:
            if current_best_student == None or current_best_student.grade < student.grade:
                best_student = student
        return current_best_student


    










