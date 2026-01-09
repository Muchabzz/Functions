def f(x, y):
    count = 0  # licznik liczb ujemnych parzystych

    for number in range(x, y + 1):
        if number < 0 and number % 2 == 0:
            count += 1

    return count
