"""def swap_without_third_variable(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")

# Test the function
a = 5
b = 10
swap_without_third_variable(a,b)"""
def swap_with_third_variable(a,b):
    """Swap two numbers using a third variable."""
    print(f"Before swapping: a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"After swapping: a = {a}, b = {b}")

# Test the function
a = 5
b = 10
swap_with_third_variable(a,b)