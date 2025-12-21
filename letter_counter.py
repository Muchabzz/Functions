# letter_counter.py

def count_letter(text, letter):
    """Zwraca ile razy dana litera pojawia się w tekście"""
    text = text.lower()       # wszystko na małe litery
    letter = letter.lower()   # litera też na małe
    return text.count(letter) # metoda count zlicza wystąpienia
