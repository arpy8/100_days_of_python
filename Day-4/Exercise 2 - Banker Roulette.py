# Import the random module here
from random import*
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print("{0} is going to buy the meal today!".format(choice(names)))