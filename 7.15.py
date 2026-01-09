def f(detector):
    people = 0  # aktualna liczba osób w pokoju

    for znak in detector:
        if znak == "+":
            people += 1
        elif znak == "-":
            people -= 1

        if people >= 3:
            return True

    return False

print(f("+-+++-+---"))     # True
print(f("+-+-+-+-"))       # False
print(f("+-++-+--"))       # False
print(f("+-++-++-+---"))   # True
