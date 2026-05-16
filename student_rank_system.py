
#Object-Oriented Python application for managing student rank lists using inheritance, abstraction, polymorphism, operator overloading, and multiple inheritance.

from abc import ABC, abstractmethod


class Evaluation(ABC):
    @abstractmethod
    def calculate_grade(self):
        pass


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Student(Person, Evaluation):
    _student_count = 0

    def __init__(self, name, age, roll, marks):
        super().__init__(name, age)
        self.roll = roll
        self.marks = marks
        Student._student_count += 1

    @staticmethod
    def validate_marks(mark):
        return isinstance(mark, int) and 0 <= mark <= 100

    @classmethod
    def student_count(cls):
        return cls._student_count

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def calculate_grade(self):
        avg = self.average_marks()
        if avg >= 90:
            return "A+"
        if avg >= 80:
            return "A"
        if avg >= 70:
            return "B"
        if avg >= 60:
            return "C"
        return "D"

    def display_details(self):
        print(f"Name         : {self.get_name()}")
        print(f"Age          : {self.get_age()}")
        print(f"Roll Number  : {self.roll}")
        print(f"Marks        : {self.marks}")
        print(f"Total Marks  : {self.total_marks()}")
        print(f"Average      : {self.average_marks():.2f}")
        print(f"Grade        : {self.calculate_grade()}")

    def __lt__(self, other):
        return self.total_marks() < other.total_marks()

    def __repr__(self):
        return f"{self.get_name()}(Roll {self.roll})"


class Sports:
    def __init__(self, sports_score = 0):
        self.sports_score = sports_score

    def display_sports_score(self):
        print(f"Sports Score : {self.sports_score}")

    def sports_bonus(self):
        return self.sports_score * 0.2


class Result(Student, Sports):
    def __init__(self, name, age, roll, marks, sports_score = 0):
        Student.__init__(self, name, age, roll, marks)
        Sports.__init__(self, sports_score)

    def overall_score(self):
        return self.total_marks() + self.sports_bonus()

    def display_details(self):
        super().display_details()
        self.display_sports_score()
        print(f"Overall Score: {self.overall_score():.2f}")


def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def read_marks(subject_index):
    while True:
        try:
            mark = int(input(f"Marks for subject {subject_index}: "))
            if Student.validate_marks(mark):
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer mark.")


def main():
    print("Student Rank List Management System")
    print("-----------------------------------")
    student_count = read_positive_int("Enter the number of students: ")

    results = []

    for index in range(1, student_count + 1):
        print(f"\nEnter details for student {index}:")
        name = input("Name: ").strip() or "Unknown"
        age = read_positive_int("Age: ")
        roll = read_positive_int("Roll Number: ")

        marks = [read_marks(i) for i in range(1, 4)]
        sports_score = read_positive_int("Sports score (0-100): ")
        if sports_score > 100:
            print("Sports score capped at 100.")
            sports_score = 100

        results.append(Result(name, age, roll, marks, sports_score))

    print("\nStudent Details and Results")
    print("===========================")
    for student in results:
        student.display_details()
        print("---------------------------")

    ranked_results = sorted(results, reverse=True)

    print("\nRank List Based on Total Marks")
    print("==============================")
    for rank, student in enumerate(ranked_results, 1):
        print(f"Rank {rank}: {student.get_name()} (Roll {student.roll}) - Total {student.total_marks()}")

    print("\nOptional Ranking with Sports Bonus")
    print("====================================")
    ranked_with_sports = sorted(results, key=lambda r: r.overall_score(), reverse=True)
    for rank, student in enumerate(ranked_with_sports, 1):
        print(f"Rank {rank}: {student.get_name()} (Roll {student.roll}) - Overall {student.overall_score():.2f}")

    print(f"\nTotal number of students: {Student.student_count()}")



main()
