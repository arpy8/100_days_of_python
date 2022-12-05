# 🚨 Don't change the code below 👇
studentHeights = input("Input a list of student heights ").split()
for n in range(0, len(studentHeights)):
    studentHeights[n] = int(studentHeights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
totalHeight = 0
for height in studentHeights:
    totalHeight += height

numberOfStudents = 0
for student in studentHeights:
    numberOfStudents += 1

print(round(totalHeight/numberOfStudents))