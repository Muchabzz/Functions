def f(number, even):
    suma = 0                     # tutaj będziemy dodawać cyfry
    number = abs(number)         # zabezpieczenie na wypadek liczby ujemnej

    for znak in str(number):     # przechodzimy po każdej cyfrze
        cyfra = int(znak)

        if even and cyfra % 2 == 0:      # gdy chcemy sumę cyfr parzystych
            suma += cyfra
        elif not even and cyfra % 2 == 1:  # gdy chcemy sumę cyfr nieparzystych
            suma += cyfra

    return suma
