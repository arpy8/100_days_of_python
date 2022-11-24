# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

if (year % 400 == 0) and (year % 100 == 0):
    print("Leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print("Leap year.")
else:
    print("Not leap year.")