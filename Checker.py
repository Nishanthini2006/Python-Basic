marks = [45, 82, 91, 33, 78]
print("--- Marksheet ---")
for mark in marks: 
   if mark >= 90:
        grade = "A+"
    else:
        if mark >= 75:
            grade = "A"
        else:
            if mark >= 60:
                grade = "B"
            else:
                if mark >= 40:
                    grade = "C"
                else:
                    grade = "F"
  print("Mark:", mark, "Grade:", grade)
  print("-----------------")
