students_result = {
    "Rahul" :94,
    "Aman"  :85,
    "Raj"   :79,
    "Suraj" :89,
    "Piyush":91
}
name = input("Enter the student's name:")
if name in students_result:
    print(f"{name}'s marks: {students_result[name]}")
else:
    print("Student not found")