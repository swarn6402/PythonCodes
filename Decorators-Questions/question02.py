# Create a decorator to print the function name and the values of its arguments 
# everytime the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kargs_value = ', '.join(f"{k} : {v}" for k,v in kwargs.items())
        print(f"calling : {func.__name__} with args {args_value} and kwargs {kargs_value}")
        result = func(*args, **kwargs)
        return result
    return wrapper
    

@debug
def greet(name, greeting = "hello"):
    print(f"{greeting}, {name}!")

greet("Swarn", "Namastey")