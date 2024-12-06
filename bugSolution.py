def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return b / a
        else:
            return a / b
    except ZeroDivisionError:
        return float('inf')  # Handle division by zero gracefully

result = function_with_uncommon_error(0, 5)
print(result) # Output: inf

result2 = function_with_uncommon_error(5, 0)
print(result2) # Output: inf