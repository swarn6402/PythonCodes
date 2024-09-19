import sys
score = 101

if score >= 101:
    print("Invalid input. Enter your grade again")
    sys.exit(1)

if score >= 90:
    grade = "A"

elif score >= 80:
    grade = "B"

elif score >= 70:
    grade = "C"

elif score >= 60:
    grade = "D"

else:
    grade = "F"

print("The Grade is: ", grade)