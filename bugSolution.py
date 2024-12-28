def improved_function(x):
    if not isinstance(x,(int,float)):
        raise TypeError("Invalid input type. Please enter a number.")
    if x == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return 1/x

# Example Usage:
print(improved_function(10))
#print(improved_function(0)) # This will raise ZeroDivisionError
#print(improved_function("abc")) # This will raise TypeError
print(improved_function(5.5))