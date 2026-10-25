"""Student report card.

AFTER: the same program, refactored for readability and reuse.
It prints each student's total, average and grade, then the class
average and the topper.
"""

from dataclasses import dataclass

# Grade boundaries: (minimum average, grade), checked from highest to lowest.
GRADE_BOUNDARIES = [(90, "A"), (75, "B"), (60, "C"), (40, "D")]
LOWEST_GRADE = "F"


@dataclass
class Student:
    name: str
    marks: list

    @property
    def total(self):
        return sum(self.marks)

    @property
    def average(self):
        return self.total / len(self.marks)


def get_grade(average):
    """Return the letter grade for an average score."""
    for minimum, grade in GRADE_BOUNDARIES:
        if average >= minimum:
            return grade
    return LOWEST_GRADE


def class_average(students):
    """Return the average of all students' averages."""
    return sum(s.average for s in students) / len(students)


def find_topper(students):
    """Return the student with the highest average."""
    return max(students, key=lambda s: s.average)


def print_report(students):
    """Print a report for every student, then class statistics."""
    for s in students:
        print(f"{s.name:<8} total={s.total:<4} average={s.average:6.2f}  grade={get_grade(s.average)}")

    topper = find_topper(students)
    print(f"\nClass average: {class_average(students):.2f}")
    print(f"Topper: {topper.name} ({topper.average:.2f})")


def main():
    students = [
        Student("Riya", [78, 85, 92]),
        Student("Aman", [45, 50, 38]),
        Student("Sara", [88, 91, 95]),
        Student("Karan", [60, 72, 58]),
    ]
    print_report(students)


if __name__ == "__main__":
    main()
