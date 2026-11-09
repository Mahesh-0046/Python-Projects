students = {
    "rahul" : {
        "Python" : 85,
        "SQL" : 90,
        "Maths" : 78,
        "English" : 80,
        "Computer_Science" : 88
    },

    "mahesh" : {
        "Python" : 92,
        "SQL" : 85,
        "Maths" : 89,
        "English" : 75,
        "Computer_Science" : 95 
    },

    "priya" : {
        "Python" : 78,
        "SQL" : 88,
        "Maths" : 92,
        "English" : 90,
        "Computer_Science" : 84
    },

    "arjun" : {
            "Python" : 65,
            "SQL" : 70,
            "Maths" : 72,
            "English" : 80,
            "Computer_Science" : 74
    }
}

def calculate_total(students):
    
    total_marks = {}
    for name, details in students.items():
        total = 0
        for subject, marks in details.items():
            total += marks

        total_marks[name] = total

    return total_marks

#total_marks = calculate_total(students)
#print("Students Total Marks:", total_marks)


def calculate_average(students, total_marks):
    
    average = {}

    for name, total in total_marks.items():

        avg = total / len(students[name])

        average[name] = avg

    return average

#average = calculate_average(students, total_marks)
#print("Students Average:", average)


def find_topper(students, total_marks):

    topper = ""
    highest_marks = 0

    for name, marks in total_marks.items():
        if marks > highest_marks:
            highest_marks = marks
            topper = name

    return topper, highest_marks 

#print("Topper:", find_topper(students, total_marks))


def find_low_marks(students, total_marks):
    
    low_marks_person = ""
    lowest_total = float("inf")

    for name, marks in total_marks.items():
        if marks < lowest_total:
            lowest_total = marks
            low_marks_person = name

    return low_marks_person, lowest_total

#print("Lowest Scorer:", find_low_marks(students, total_marks))

def calculate_grade(average):
    
    grades = {}
    for name, avg in average.items():
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
            grade = "F"

        grades[name] = grade

    return grades

#grade = calculate_grade(average)
#print("Students Grade:", grade)


def student_report(students, total_marks, average, grade):
    
    print("=" * 30)
    print("       STUDENT REPORT")
    print("=" * 30)

    for name, details in students.items():
        print("\nStudent Name:", name.capitalize())

        student_total = total_marks[name]

        student_average = average[name]

        student_grade = grade[name]
        

        print("=" * 30)
        

        for subjects, marks in details.items():
 
            print(f"{subjects:<20}  {marks:>5}")
            
        print("-" * 30)
        print(f"Total Marks : {student_total} / 500")
        print(f"Average     : {student_average:.2f}")
        print(f"Grade       : {student_grade}")
        print("=" * 30)
    

#student_report(students, total_marks, average, grade)

def main():
    total_marks = calculate_total(students)
    average = calculate_average(students, total_marks)
    grade = calculate_grade(average)
    topper_name, topper_marks = find_topper(students, total_marks)
    lowest_scorer_name, lowest_scorer_marks = find_low_marks(students, total_marks)
    
    student_report(students, total_marks, average, grade)

    print("Topper:", topper_name.capitalize(), topper_marks)
    print("Lowest Scorer:", lowest_scorer_name.capitalize(), lowest_scorer_marks)

main()