def sort_students(students):
    return sorted(students, key = lambda d: (d["grade"], -d["marks"]))

students = [
    {"name": "Rahul", "grade": 10, "marks": 85},
    {"name": "Priya", "grade": 9,  "marks": 90},
    {"name": "Aman",  "grade": 10, "marks": 92},
    {"name": "Neha",  "grade": 9,  "marks": 78},
    {"name": "Karan", "grade": 10, "marks": 85},
]

for s in sort_students(students):
    print(s)