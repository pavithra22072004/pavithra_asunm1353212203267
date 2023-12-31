class Student:
  def __init__(self,name, roll_number,cgpa):
    self.name = name
    self.roll_number= roll_number
    self.cgpa =cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students

students =[
  Student("hari","A123",6.9),
  Student("srikanth","A124",8.9),
  Student("mahidhar","A125",7.9),
  Student("varsha","A126",5.9),
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("Name: {},roll number:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))