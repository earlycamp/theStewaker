# Steps
# Have an input that will ask for numbers
# Store those inputs in the array
# Have a variable for sorting the array
# Have a variable for squaring each number

# Sudo code
# inputs Enter a number
# tuple = tuple(inputs)
# tuple = tuple.sort(hightest to lowest)
# for a in tuple:
#   a * a
# print tuple


# Real code
input1 = int(input("Enter the first number:  "))
input2 = int(input("Enter the second number:  "))
input3 = int(input("Enter the third number:  "))
input4 = int(input("Enter the fourth number:  "))
input5 = int(input("Enter the fifth number:  "))
tuple_num = []
tuple_num.append(input1)
tuple_num.append(input2)
tuple_num.append(input3)
tuple_num.append(input4)
tuple_num.append(input5)
print(tuple_num)
tuple_num.sort()
for a in tuple_num:
    print(a * a)