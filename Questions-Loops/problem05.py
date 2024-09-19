input_string = str(input("Enter your string: "))

for char in input_string:
    if input_string.count(char) == 1:
        print(char)
        break

print("The first non-repeated character is:", char)