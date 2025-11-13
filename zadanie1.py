def sprawdz_pelnioletnosc():
    rok_ur = int(input("Podaj rok urodzenia: "))
    ob_rok = 2025
    wiek = ob_rok - rok_ur
    
    # wyświetlanie wieku i informacji o pełnioletności
    print(f"Masz {wiek} lat.")
    if wiek >= 18:
        print("Jesteś pełnoletni.")
    else:
        print("Jesteś niepełnoletni.")

sprawdz_pelnioletnosc()
