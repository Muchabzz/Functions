import math

def triangle_area(a, b, c):
    # Obliczanie pół obwodu
    s = (a + b + c) / 2
    # Obliczanie pola powierzchni
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Przykład użycia funkcji
print('Pole trójkąta (3, 4, 5):', triangle_area(3, 4, 5))
print('Pole trójkąta (5, 12, 13):', triangle_area(5, 12, 13))
print('Pole trójkąta (7, 24, 25):', triangle_area(7, 24, 25))
