def f(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2

print(f(2, 3, "+"))   # 5
print(f(2, 3, "%"))   # 2
print(f(2, 3, "**"))  # 8
print(f(2, 3, "*"))   # 6
print(f(2, 3, "-"))   # -1
