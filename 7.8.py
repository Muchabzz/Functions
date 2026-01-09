def f(amount_to_pay):
    coins = 0            # licznik wszystkich użytych monet

    coins += amount_to_pay // 5   # ile monet 5 zł się zmieści
    amount_to_pay = amount_to_pay % 5  # ile zł zostaje po monetach 5 zł

    coins += amount_to_pay // 2   # ile monet 2 zł się zmieści z reszty
    amount_to_pay = amount_to_pay % 2  # ile zł zostaje po monetach 2 zł

    coins += amount_to_pay // 1   # reszta to monety 1 zł

    return coins          # zwracamy minimalną liczbę monet
