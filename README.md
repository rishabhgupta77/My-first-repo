# 📘 Student Enrollment & Result Portal

## 📝 Overview
The **Student Enrollment & Result Portal** is a simple Python program designed to manage student data, including their marks, average score, and grade.  
It also identifies the **class topper** based on the highest average marks.

This project demonstrates the use of:
- Dictionaries for structured data storage  
- Functions for modular programming  
- Conditional logic for grade calculation  

---

## 🚀 Features
✅ Add new students with marks in multiple subjects  
✅ Automatically calculate **average marks** and **grade**  
✅ Display all student records neatly  
✅ Identify and display the **topper** of the class  

---

## 💻 Code Explanation

### 1. Data Structure
```python
students = {}
```
- Stores data in the format:
  ```python
  students = {
      roll_number: {'name': student_name, 'marks': {'Math': 90, 'Sci': 85, 'Eng': 80}}
  }
  ```

---

### 2. Functions

#### ➤ `add_student(roll, name, marks)`
Adds a new student to the database and prints details with average, grade, and topper.

#### ➤ `calc_average(marks)`
Calculates the average marks:
```python
avg = sum(marks.values()) / len(marks)
```

#### ➤ `calc_grade(avg)`
Returns grade based on average:
| Average | Grade |
|----------|--------|
| ≥ 85     | A |
| ≥ 70     | B |
| ≥ 50     | C |
| < 50     | D |

#### ➤ `find_topper()`
Finds the roll number of the student with the highest average.

#### ➤ `show_all_students()`
Displays all student records along with their marks, average, and grade.

---

## 🧩 Sample Output
```python
Saved 101 | Avg=83.33 | Grade B | Topper=101
Saved 102 | Avg=88.00 | Grade A | Topper=102

Student Records
Roll: 101, Name: Asha, Marks: {'Math': 90, 'Sci': 82, 'Eng': 78}, Avg: 83.33, Grade: B
Roll: 102, Name: Ravi, Marks: {'Math': 88, 'Sci': 91, 'Eng': 85}, Avg: 88.00, Grade: A
Topper Roll: 102
```

---

## 🧠 How It Works
1. Add student data using `add_student()`.  
2. Each time a student is added, the program:
   - Calculates average marks  
   - Determines grade  
   - Updates topper information  
3. Use `show_all_students()` to view all records.

---

## 🧰 Requirements
- Python 3.6 or above  
(No external libraries required)

---

## 🏁 How to Run
1. Copy the code into a file named `student_portal.py`
2. Run the script in your terminal or IDE:
   ```bash
   python student_portal.py
   ```
3. Observe the output in the console.

---

## 🧑‍💻 Example Code
```python
add_student(101, 'Asha', {'Math': 90, 'Sci': 82, 'Eng': 78})
add_student(102, 'Ravi', {'Math': 88, 'Sci': 91, 'Eng': 85})
show_all_students()
```

---

## 🏆 Future Improvements
- Add update and delete student options  
- Store data in a file (JSON or CSV)  
- Add a GUI or web interface  
