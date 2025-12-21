<<<<<<< HEAD
    # Calculates the sum of the digits in a number
def sum_digits(number):
    number = abs(number)        # bierzemy wartość bezwzględną
    total = 0
    for digit in str(number):   # zamieniamy liczbę na napis i przechodzimy po każdej cyfrze
        total += int(digit)     # dodajemy cyfrę do sumy
    return total

# wczytanie liczby od użytkownika
any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)

# wypisanie wyniku
print(f'The sum of the digits in the number {any_number} is {result}')
=======
def sum_digits(number):
    # Zmieniamy liczbę na bezwzględną i zamieniamy na ciąg
    number = abs(number)
    total = 0
    # Iterujemy po cyfrach liczby
    for digit in str(number):
        total += int(digit)
    return total

# Testowanie funkcji
any_number = int(input('Wpisz liczbę: '))
print('Suma cyfr liczby:', sum_digits(any_number))
>>>>>>> b4770c5f2e0d0ca7ff2ce14518d1262a0494f257
