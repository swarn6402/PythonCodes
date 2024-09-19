input_string = str(input("Enter your string:"))
reversed_string = " "

for char in input_string:
    reversed_string = char + reversed_string

print("Your reversed string is:", reversed_string)