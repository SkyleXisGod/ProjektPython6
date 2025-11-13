def planer_podrozy():
    km = float(input("Ile kilometrów? "))
    spalanie = float(input("Podaj średnie spalanie w l/100km: "))
    cena_paliwa = float(input("Podaj cenę paliwa za litr: "))
    pasazerowie = input("Podaj liczbę osób (opcjonalnie): ")

    zuzycie = (km / 100) * spalanie
    koszt = zuzycie * cena_paliwa

    print(f"\nZużyjesz {zuzycie:.2f} litrów paliwa.")
    print(f"Koszt podróży: {koszt:.2f} zł.")

    # wyświetlanie kosztu na osobę tylko, jeżeli użytkownik coś wpisał
    if pasazerowie.strip() != "":
        koszt_na_osobe = koszt / int(pasazerowie)
        print(f"Koszt na osobę: {koszt_na_osobe:.2f} zł.")

    if km > 500:
        print("Długa trasa – zaplanuj przerwy na odpoczynek!")

planer_podrozy()

# zmienna:.2f -> aby ograniczyło ilość zer 