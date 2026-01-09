def f(binary_number):
    for znak in binary_number:
        if znak != '0' and znak != '1':
            return False
    return True


print(f("101101"))       # True
print(f("1311a10100"))   # False
