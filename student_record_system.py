#A Python-based Student Record Management System demonstrating lists, nested lists, dictionaries, tuples, sets, list comprehensions, shallow/deep copy, and exception handling.

import copy

def main():
    try:
        num_students = int(input("Enter the number of students: "))

        names = []
        roll_numbers = []
        marks_list = []

        for i in range(num_students):
            print(f"\nEnter details for student {i+1}:")
            while True:
                name = input("Name: ").strip()
                if not name:
                    print("Name cannot be empty. Please enter again.")
                    continue
                break
            while True:
                try:
                    roll = int(input("Roll Number: "))
                    if roll <= 0:
                        print("Roll number must be positive. Please enter again.")
                        continue
                    break
                except ValueError:
                    print("Invalid roll number. Please enter a positive integer.")
            marks = []
            for j in range(3):
                while True:
                    try:
                        mark = int(input(f"Marks in subject {j+1}: "))
                        if mark < 0 or mark > 100:
                            print("Marks must be between 0 and 100. Please enter again.")
                            continue
                        marks.append(mark)
                        break
                    except ValueError:
                        print("Invalid marks. Please enter a number between 0 and 100.")
            names.append(name)
            roll_numbers.append(roll)
            marks_list.append(marks)

        student_dict = dict(zip(roll_numbers, names))
        print("\nStudent Dictionary (Roll Number: Name):")
        for roll, name in student_dict.items():
            print(f"{roll}: {name}")

        upper_names = [name.upper() for name in names]
        print(f"\nNames in uppercase: {upper_names}")

        long_names = [name for name in names if len(name) > 5]
        print(f"Names longer than 5 characters: {long_names}")

        count_A = sum(1 for name in names if name.upper().startswith('A'))
        print(f"Number of names starting with 'A': {count_A}")

        averages = [sum(marks) / 3 for marks in marks_list]
        high_avg_students = [names[i] for i in range(len(names)) if averages[i] > 75]
        print(f"\nStudents with average marks > 75: {high_avg_students}")

        even_rolls = [roll for roll in roll_numbers if roll % 2 == 0]
        print(f"Even roll numbers: {even_rolls}")

        if marks_list:
            first_marks_tuple = tuple(marks_list[0])
            print(f"\nFirst student's marks as tuple: {first_marks_tuple}")

            all_marks = sum(marks_list, [])
            unique_marks = set(all_marks)
            print(f"Unique marks from all students: {unique_marks}")

            shallow_copy = copy.copy(marks_list)
            deep_copy = copy.deepcopy(marks_list)

            print("\nOriginal marks list:")
            print(marks_list)

            if marks_list[0]:
                original_first = marks_list[0][0]
                marks_list[0][0] = 99 

                print("\nAfter modifying first student's first mark to 99:")
                print("Original:", marks_list)
                print("Shallow copy:", shallow_copy)
                print("Deep copy:", deep_copy)
        else:
            print("No students to process for tuple and set operations.")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

main()