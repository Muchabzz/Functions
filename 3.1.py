# To use the functions available in an external module,
# you must include that module in your program.
import math

# pierwiastek kwadratowy
square_root = math.sqrt(7)
print('A square root of 7 is', square_root)

# logarytm naturalny
natural_log = math.log(5)
print('Natural logarithm of 5 is', natural_log)

# sinus kąta 90 stopni
# math.sin() przyjmuje radiany, więc zamieniamy stopnie na radiany
radians_90 = math.radians(90)  # zamiana stopni na radiany
sine_90 = math.sin(radians_90)
print('Sine of 90 degrees is', sine_90)
