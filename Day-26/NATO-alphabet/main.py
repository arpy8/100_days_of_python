from pandas import *

data = read_csv("nato_phonetic.csv")
student_data = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
output_list = [student_data[letter] for letter in word]
print(output_list)