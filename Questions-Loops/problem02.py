n = int(input("Enter a number: "))
sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even = sum_even + i

print("the sum of even numbers upto n is:", sum_even)