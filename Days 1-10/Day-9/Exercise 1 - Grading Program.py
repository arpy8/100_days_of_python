student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for i in student_scores:
    score = student_scores[i]
    if score > 90:
        rslt = "Outstanding"
    elif score > 80:
        rslt = "Exceeds Expectations"
    elif score > 70:
        rslt = "Acceptable"
    elif score <= 70:
        rslt = "Fail"
    else:
        print("error")
    student_grades[i] = rslt 

# 🚨 Don't change the code below 👇

print(student_grades)