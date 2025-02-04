from functools import reduce

def multiply_tuple_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers)

# Example usage:
numbers_tuple = (2, 3, 4, 5)
result = multiply_tuple_numbers(numbers_tuple)
print("Product of tuple numbers:", result)
