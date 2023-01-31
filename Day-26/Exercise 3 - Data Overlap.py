with open("file1.txt") as file1:
    file_1_data =  file1.readlines()
with open("file2.txt") as file2:
    file_2_data =  file2.readlines()
# Write your code above 👆

result = [int(items) for items in file_1_data if items in file_2_data]
print(result)


