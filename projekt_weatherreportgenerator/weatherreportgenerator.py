import random

def generuj_prognoze(miasto):
    # losowa temperatura od -10 do 35
    temperatura = random.randint(-10, 35)
    # losowe warunki pogodowe
    warunki = random.choice(["Słonecznie", "Deszczowo", "Zachmurzenie"])
    # prognozs jako słownik
    return {"miasto": miasto, "temp": temperatura, "warunki": warunki}

def pokaz_prognozy(lista_prognoz):
    if not lista_prognoz:
        print("Brak prognoz.\n")
        return
    # wyświetlemoie prognozy
    for prog in lista_prognoz:
        print(f"Miasto: {prog['miasto']}, Temperatura: {prog['temp']}°C, Warunki: {prog['warunki']}")
    print()

def analiza(lista_prognoz):
    if not lista_prognoz:
        print("Brak danych do analizy.\n")
        return ""

    # wartosci poczatkowe
    suma = 0
    max_temp = lista_prognoz[0]["temp"]
    min_temp = lista_prognoz[0]["temp"]
    miasto_max = lista_prognoz[0]["miasto"]
    miasto_min = lista_prognoz[0]["miasto"]

    # sprawdzenie min, max i zliczenie sumy ( po czym sredniej ) dla kazdej prognozy
    for prog in lista_prognoz:
        t = prog["temp"]
        suma += t

        # sprawdz max
        if t > max_temp:
            max_temp = t
            miasto_max = prog["miasto"]

        # sprawdz min
        if t < min_temp:
            min_temp = t
            miasto_min = prog["miasto"]

    srednia = suma / len(lista_prognoz)

    # wyświetl wyniki
    print(f"Średnia temperatura: {srednia:.1f}°C")
    print(f"Najwyższa temperatura: {max_temp}°C ({miasto_max})")
    print(f"Najniższa temperatura: {min_temp}°C ({miasto_min})\n")

    # zwracanie tekstu
    return f"Średnia temperatura: {srednia:.1f}°C\nNajwyższa temperatura: {max_temp}°C ({miasto_max})\nNajniższa temperatura: {min_temp}°C ({miasto_min})\n"

def zapisz_raport(lista_prognoz, podsumowanie):
    with open("raport.txt", "w", encoding="utf-8") as reportfile:
        reportfile.write("Prognozy pogodowe:\n")
        for prog in lista_prognoz:
            reportfile.write(f"Miasto: {prog['miasto']}, Temperatura: {prog['temp']}°C, Warunki: {prog['warunki']}\n")
        reportfile.write("\nPodsumowanie:\n")
        reportfile.write(podsumowanie)
    print("Raport zapisany do pliku raport.txt\n")

def main():
    lista_miast = []
    lista_prognoz = []

    while True:
        cmd = input("Co robisz? (dodaj/lista/analiza/zapis/koniec): ").strip().lower()

        if cmd == "dodaj":
            # wprowadz miasta oddzielone przecinkiem
            miasta_input = input("Wpisz miasta oddzielone przecinkiem: ")
            lista_miast = [m.strip() for m in miasta_input.split(",") if m.strip()]
            # generuj prognozy dla wprowadzonych miast
            lista_prognoz = [generuj_prognoze(miasto) for miasto in lista_miast]
            print("Wygenerowano prognozy.\n")

        elif cmd == "lista":
            pokaz_prognozy(lista_prognoz)

        elif cmd == "analiza":
            podsumowanie = analiza(lista_prognoz)

        elif cmd == "zapis":
            if not lista_prognoz:
                print("Brak prognoz do zapisania.\n")
            else:
                podsumowanie = analiza(lista_prognoz)
                zapisz_raport(lista_prognoz, podsumowanie)

        elif cmd == "koniec":
            break

        else:
            print("Nie rozumiem.\n")

main()
