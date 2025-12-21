# Program for testing built-in functions

# największa liczba
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

# najmniejsza liczba
min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

# długość napisu
str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

# wczytanie litery z klawiatury
letter = input("Enter a letter: ")
print("You entered the letter:", letter)

# liczba reprezentująca napis "20303"
number_from_string = int("20303")
print('Integer representing the string "20303" is', number_from_string)

# binarny napis reprezentujący 304
binary_string = bin(304)
print('Binary string representing 304 is', binary_string)

# szesnastkowy napis reprezentujący 304
hex_string = hex(304)
print('Hexadecimal string representing 304 is', hex_string)

# liczba całkowita reprezentująca kod Unicode znaku €
unicode_number = ord('€')
print('Integer representing the Unicode code of € is', unicode_number)

# wartość bezwzględna
absolute_value = abs(-17)
print('Absolute value of -17 is', absolute_value)
