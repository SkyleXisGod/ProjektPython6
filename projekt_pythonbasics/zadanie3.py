def statystyka_ocen():
    wyniki = (45, 67, 82, 90, 55, 74, 100, 61)
    suma = 0

    # obliczanie średniej
    for wynik in wyniki:
        suma += wynik
    srednia = suma / len(wyniki)

    print(f"Średnia ocen: {srednia:.2f}")

    # wyniki > srednia
    wyniki_powyzej = []
    for wynik in wyniki:
        if wynik > srednia:
            wyniki_powyzej.append(wynik)
    print("Wyniki powyżej średniej:", wyniki_powyzej)

    # osoby zdajace
    zdali = []
    for wynik in wyniki:
        if wynik >= 60:
            zdali.append(wynik)
    print(f"Liczba osób, które zdały: {len(zdali)}")

    # sprawdzenie maksa
    for wynik in wyniki:
        if wynik == 100:
            print("Gratulacje dla najlepszego uczestnika!")

statystyka_ocen()
