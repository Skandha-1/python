def check_odd_even(n):
    """Check if a number is odd or even."""
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

# Test the function
num = 29
result = check_odd_even(num)
print(f"{num}is{result}")