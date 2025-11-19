def analizuj_tekst():
    tekst = input("Podaj tekst: ")

    # formatowanie tekstu
    tekst = tekst.strip()
    tekst = tekst.lower()
    tekst_sformatowany = tekst.replace("python", "PYTHON")

    # odwracanie słów
    slowa = tekst_sformatowany.split()
    tekst_odwrocony = ""
    for slowo in slowa:
        tekst_odwrocony += slowo[::-1] + " "
    tekst_odwrocony = tekst_odwrocony.strip()

    licznik_liter = {}
    for znak in tekst_sformatowany:
        if znak.isalpha():  # sprawdzamy, czy to litera
            if znak in licznik_liter:
                licznik_liter[znak] += 1
            else:
                licznik_liter[znak] = 1

    print("\nWynik analizy:")
    print("tekst_sformatowany:", tekst_sformatowany)
    print("tekst_odwrocony   :", tekst_odwrocony)
    print("licznik_liter     :", licznik_liter)

    wynik = {
        "tekst_sformatowany": tekst_sformatowany,
        "tekst_odwrocony": tekst_odwrocony,
        "licznik_liter": licznik_liter
    }

    return wynik


analizuj_tekst()
