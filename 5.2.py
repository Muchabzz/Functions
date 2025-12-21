def m_to_cm(n):
    """Konwertuje metry na centymetry."""
    return n * 100

def cm_to_m(n):
    """Konwertuje centymetry na metry."""
    return n / 100

def cm_to_inches(cm):
    """Konwertuje centymetry na cale."""
    # 1 cal = 2.54 cm
    return cm / 2.54

def feet_inches_to_cm(feet, inches):
    """Konwertuje stopy i cale na centymetry."""
    # 1 stopa = 12 cali
    # 1 stopa = 30.48 cm
    # 1 cal = 2.54 cm
    cm_from_feet = feet * 30.48
    cm_from_inches = inches * 2.54
    return cm_from_feet + cm_from_inches

if __name__ == "__main__":
    # Testowanie istniejących funkcji
    print("--- Konwersje bazowe (m/cm) ---")
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    
    # Testowanie dodanych funkcji
    print("\n--- Konwersje Cale/Stopy ---")
    # 100 cm / 2.54 = 39.37 cala
    print(f'100cm = {cm_to_inches(100):.2f} cali') 
    
    # 5 stóp = 5 * 30.48 = 152.4 cm
    # 10 cali = 10 * 2.54 = 25.4 cm
    # Razem: 152.4 + 25.4 = 177.8 cm
    print(f'5 stóp i 10 cali = {feet_inches_to_cm(5, 10):.2f}cm')
    print(f'1 stopa i 0 cali = {feet_inches_to_cm(1, 0)}cm')