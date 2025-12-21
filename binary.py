def f(binary_numbers):
    for char in binary_numbers:
        if char not in "01":
            return False
    return True