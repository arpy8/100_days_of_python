# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
x = name1 + name2
x = x.lower()
#Write your code below this line 👇
t = x.count("t")
r = x.count("r")
u = x.count("u")
e = x.count("e")
true = t+r+u+e
l = x.count("l")
o = x.count("o")
v = x.count("v")
e = x.count("e")
love = l+o+v+e
rslt = int(str(true)+str(love))
if rslt < 10 or rslt > 90:
    print(f"Your score is {rslt}, you go together like coke and mentos.")
elif rslt > 40 and rslt < 50:
    print(f"Your score is {rslt}, you are alright together.")
else:
    print(f"Your score is {rslt}.")