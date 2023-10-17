def calculate_grade(subject_marks):
    average_marks = sum(subject_marks) / len(subject_marks)

    if any(mark < 0 for mark in subject_marks):
        return "Unrecognized Marks"
    elif average_marks >= 71:
        return "A"
    elif average_marks >= 51:
        return "B"
    elif average_marks >= 31:
        return "C"
    else:
        return "D"


math_marks = float(input("Enter marks for Math: "))
physics_marks = float(input("Enter marks for Physics: "))
geography_marks = float(input("Enter marks for Geography: "))
chemistry_marks = float(input("Enter marks for Chemistry: "))


subject_marks = [math_marks, physics_marks, geography_marks, chemistry_marks]
grade = calculate_grade(subject_marks)

if grade == "Unrecognized Marks":
    print("Unrecognized Marks. Please enter valid marks.")
else:
    print(f"The average grade is: {grade}")

