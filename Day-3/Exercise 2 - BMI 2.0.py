# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
rslt = round(float(weight)/float(height)**2)

if rslt<18.5:
    print(f"Your BMI is {rslt}, you are underweight")
elif rslt>18.5 and rslt < 25: 
    print(f"Your BMI is {rslt}, you have a normal weight.")
elif rslt>25 and rslt < 30:
    print(f"Your BMI is {rslt}, you are slightly overweight.")
elif rslt>30 and rslt < 35:
    print(f"Your BMI is {rslt}, you are obese.")
elif rslt > 35:
    print(f"Your BMI is {rslt},you are clinically obese.")
else:
    print("error")