def masked_number(number):
     if len(number) != 16:
        return "Invalid card number"
     
     start = 2  # indeks 3
     end = 12   # indeks 14 (czyli slice do 14, bo 14 nie wchodzi)
     replacement = "*" * (end - start)  # tyle gwiazdek, ile znaków do zastąpienia

     hide = number[:start] + replacement + number[end:]
     return(hide)
