from range_checker import in_range

number = int(input("A number: "))
x = 2
y = 15

if in_range(number, x, y):
    answer = "yes"
else:
    answer = "no"

print(f"Number {number} in the range <{x},{y}>: {answer}")
