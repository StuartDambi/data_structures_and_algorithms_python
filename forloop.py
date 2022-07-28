def grading_students(grades):
  rounded_grades = []
  for grade in grades:
    if grade < 38:
      rounded_grades.append(grade)
    elif (grade + 2)%5 == 0:
      grade = grade + 2
      rounded_grades.append(grade)
    elif (grade + 1)%5 == 0:
      grade = grade + 1
      rounded_grades.append(grade)
    else:
      rounded_grades.append(grade)
  print(rounded_grades)

grading_students([32, 43, 50, 64, 80])
# 32 45 50 65 80