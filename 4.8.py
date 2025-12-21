def time_string(hours, minutes, time_format):
    """
    Zwraca ciąg znaków określający czas w podanym formacie ('24' lub '12').
    hours (0..23), minutes (0..59).
    """
    
    if time_format == '24':
        # Format 24-godzinny (HH:MM)
        return f"{hours:02}:{minutes:02}" #:02 to sposób formatowania liczby, żeby zawsze miała dwie cyfry.
        
    elif time_format == '12':
        # Format 12-godzinny (H:MMam/pm)
        
        # Określenie am/pm
        am_pm = "am" if hours < 12 else "pm"
        
        # Konwersja godziny 24-godzinnej na 12-godzinną (0 -> 12am, 13 -> 1pm)
        if hours == 0:
            h_12 = 12
        elif hours > 12:
            h_12 = hours - 12
        else:
            h_12 = hours
            
        minutes_str = f"{minutes:02}"
        
        return f"{h_12}:{minutes_str}{am_pm}"
        
    else:
        return "Invalid time format specified"

# Program testujący
def main_time_string():
    print(f"time_string(15, 38, '24') returns '{time_string(15, 38, '24')}'")
    print(f"time_string(8, 3, '24') returns '{time_string(8, 3, '24')}'")
    print(f"time_string(0, 5, '24') returns '{time_string(0, 5, '24')}'")
    print(f"time_string(11, 15, '12') returns '{time_string(11, 15, '12')}'")
    print(f"time_string(0, 7, '12') returns '{time_string(0, 7, '12')}'")
    print(f"time_string(7, 30, '12') returns '{time_string(7, 30, '12')}'")
    print(f"time_string(12, 46, '12') returns '{time_string(12, 46, '12')}'")
    print(f"time_string(13, 10, '12') returns '{time_string(13, 10, '12')}'")
    print(f"time_string(19, 2, '12') returns '{time_string(19, 2, '12')}'")

if __name__ == "__main__":
    main_time_string()