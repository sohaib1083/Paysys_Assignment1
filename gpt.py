def process_numbers(a, b):
    if a <= 0 or b <= 0:
        return "Error"
    sum_ab = a + b
    if sum_ab > 100:
        return sum_ab
    elif sum_ab == 100:
        return a * b
    else:
        return abs(a - b)

# Example usage
print(process_numbers(60, 50))  # Output: 110
print(process_numbers(50, 50))  # Output: 2500
print(process_numbers(30, 40))  # Output: 10
print(process_numbers(-10, 20))  # Output: "Error"
