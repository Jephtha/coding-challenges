# Python Input and Output Exercises from this website: https://pynative.com/python-input-and-output-exercise/


# Exercise 1
# Write a program to accept two numbers from the user and calculate multiplication
# x, y = input("Enter two numbers: ").split()
# print(int(x)*int(y))

# Exercise 2
# print('Name', 'Is', 'James') as Name**Is**James
# print('Name', 'Is', 'James', sep='**')

# Exercise 3
# Convert Decimal number to octal using print() output formatting
# print("%o" % 8)

# Exercise 4
# Display float number with 2 decimal places using print()
# print("{:.2f}".format(458.541315))


# Exercise 5
# Accept a list of 5 float numbers as an input from the user
# 3 different solutions

# print([float(x) for x in input("Enter 5 float numbers: ").split()])
# print(input("Enter 5 float numbers: ").split()) # this returns a list of 5 strings not float values
# print(list(map(float, input("Enter 5 float numbers: ").split())))


# Exercise 6
# Write all content of a given file into a new file by skipping line number 5
# with open("test.txt", 'r') as file:
#     lines = file.readlines()
# with open("new_file.txt", 'w') as file:
#     for i in range(len(lines)):
#         if i == 4: pass
#         else: file.write(lines[i])


# Exercise 7

