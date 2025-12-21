# Converts letter to corresponding ICAO word
def icao(letter):
<<<<<<< HEAD
    letter = letter.capitalize() #.capitalize zmienia pierwszą litere na dużą a pozostałe na małe
=======
    letter = letter.capitalize()
>>>>>>> b4770c5f2e0d0ca7ff2ce14518d1262a0494f257
    if letter == 'A':
        icao_name = 'Alfa'
    elif letter == 'B':
        icao_name = 'Bravo'
    elif letter == 'C':
        icao_name = 'Charlie'
    elif letter == 'D':
        icao_name = 'Delta'
    elif letter == 'E':
        icao_name = 'Echo'
    elif letter == 'F':
        icao_name = 'Foxtrot'
    elif letter == 'G':
        icao_name = 'Golf'
    elif letter == 'H':
        icao_name = 'Hotel'
    elif letter == 'I':
        icao_name = 'India'
    elif letter == 'J':
        icao_name = 'Juliett'
    elif letter == 'K':
        icao_name = 'Kilo'
    elif letter == 'L':
        icao_name = 'Lima'
    elif letter == 'M':
        icao_name = 'Mike'
    elif letter == 'N':
        icao_name = 'November'
    elif letter == 'O':
        icao_name = 'Oscar'
    elif letter == 'P':
        icao_name = 'Papa'
    elif letter == 'Q':
        icao_name = 'Quebec'
    elif letter == 'R':
        icao_name = 'Romeo'
    elif letter == 'S':
        icao_name = 'Sierra'
    elif letter == 'T':
        icao_name = 'Tango'
    elif letter == 'U':
        icao_name = 'Uniform'
    elif letter == 'V':
        icao_name = 'Victor'
    elif letter == 'W':
        icao_name = 'Whiskey'
    elif letter == 'X':
        icao_name = 'X-ray'
    elif letter == 'Y':
        icao_name = 'Yankee'
    elif letter == 'Z':
        icao_name = 'Zulu'
    else:
        icao_name = '???'

    return icao_name

# Function usage
name = input('Enter your name: ')
print('ICAO words for spelling out your name:')

for char in name:
<<<<<<< HEAD
    if char.isalpha():  # sprawdza czy znak to litera
        word = icao(char) #wywołuje funkcje i przypisuje do każdej litery imienia odpowiedni icao
        print(word, end=" ")  # wypisuje imie za pomocą icao
print()
=======
    if char.isalpha():  # Check if the character is a letter
        word = icao(char)
        print(word, end=" ")  # Print each ICAO word separated by a space
print()  # Print a new line at the end
>>>>>>> b4770c5f2e0d0ca7ff2ce14518d1262a0494f257
