def marked_number(number):
    start = 2  # indeks 3
    end = 12   # indeks 14 (czyli slice do 14, bo 14 nie wchodzi)
    replacement = "*" * (end - start)  # tyle gwiazdek, ile znaków do zastąpienia

marked_number = number[:start] + replacement + number[end:]
print(marked_number)
