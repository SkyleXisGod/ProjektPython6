def student_info():
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    rok = int(input("Rok studiów: "))
    kierunek = input("Kierunek: ")
    oceny = input("Podaj oceny oddzielone spacją: ").split()
    nowe_oceny = []
    for o in oceny:
        liczba = float(o)
        nowe_oceny.append(liczba)
    oceny = nowe_oceny

    srednia = sum(oceny) / len(oceny)

    print("\n--- Obliczenia prostokąta ---")
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    pole = a * b
    obwod = 2 * (a + b)

    student = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok": rok,
        "kierunek": kierunek,
        "oceny": oceny,
        "srednia": srednia,
        "pole_prostokata": pole,
        "obwod_prostokata": obwod
    }

    print("\nRaport studenta:")
    for i in student:
        wartosc = student[i]
        print(i, ":", wartosc)

    return student

student_info()
