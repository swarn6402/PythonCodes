def giveSum(*args):
    print("the given arguments are:", args)
    return sum(args)

print("The sum of the given arguments is:", giveSum(1, 2, 3))
print("The sum of the given arguments is:", giveSum(1, 2, 3, 4, 5))