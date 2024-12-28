def function_with_uncommon_error(x):
    try:
        result = 1 / x
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None  # or raise a more specific exception
    except TypeError:
        print("Error: Invalid input type. Please enter a number.")
        return None
    else:
        return result

# Example Usage
print(function_with_uncommon_error(10))
print(function_with_uncommon_error(0))
print(function_with_uncommon_error("abc"))
print(function_with_uncommon_error(5.5))