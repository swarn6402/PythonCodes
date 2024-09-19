def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name = "Swarn", age = 22, location = "Patna")
print_kwargs(name = "Swarn", age = 22, location = "Patna", gender = "Male")