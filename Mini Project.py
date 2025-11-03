# Student Enrollment & Result Portal
students = {}
def add_student(roll, name, marks):
    students[roll] = {'name': name, 'marks': marks}
    avg = calc_average(marks)
    grade = calc_grade(avg)
    topper = find_topper()
    print(f"Saved {roll} | Avg={avg:.2f} | Grade {grade} | Topper={topper}")

def calc_average(marks):
    return sum(marks.values()) / len(marks)
def calc_grade(avg):
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'D'
def find_topper():
    if not students:
        return None
    highest_avg = 0
    topper_roll = None
    for roll, info in students.items():
        avg = calc_average(info['marks'])
        if avg > highest_avg:
            highest_avg = avg
            topper_roll = roll
    return topper_roll
def show_all_students():
    print("\nStudent Records")
    for roll, info in students.items():
        avg = calc_average(info['marks'])
        grade = calc_grade(avg)
        print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}, Avg: {avg:.2f}, Grade: {grade}")
    print(f"Topper Roll: {find_topper()}\n")
add_student(101, 'Asha', {'Math': 90, 'Sci': 82, 'Eng': 78})
add_student(102, 'Ravi', {'Math': 88, 'Sci': 91, 'Eng': 85})
show_all_students()
