number = int(input("Enter the number: "))
factorial = 1

while number > 0:
    factorial = number * factorial
    number = number - 1

print ("The factorial is", factorial)