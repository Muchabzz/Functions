def month(n):
    #Zwraca nazwę miesiąca dla podanej liczby 1..12
    names = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
    
    if 1 <= n <= 12:
        return names[n-1]  # listy w Pythonie liczymy od 0
    else:
        return "Invalid month number"