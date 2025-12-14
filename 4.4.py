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
