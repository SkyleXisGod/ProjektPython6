def sklep():
    produkty = ("chleb", "masło", "ser", "jabłka", "kiełbasa", "woda", "pepsi", "makaron", "sól", "cukier")
    koszyk = []

    # dodawanie 3 produktow uzytkownika
    for i in range(3):
        produkt = input(f"Podaj produkt nr {i+1}: ")
        produkt = produkt.lower()
        # wyswietlanie stosownej informacji, jest lub nie ma
        if produkt in produkty:
            koszyk.append(produkt)
        else:
            print(f"Produkt '{produkt}' jest niedostępny.")

    koszyk.sort()
    print("\nTwój koszyk:", koszyk)

sklep()
