# dodawanie zadań w postaci nazwa/priorytet
def dodaj(tasks):
    taskname = input("Treść zadania: ")
    priority = input("Priorytet (wysoki/sredni/niski): ")
    tasks.append({"title": taskname, "priority": priority, "done": False})
    print("Dodano.\n")

# wyświetlanie zadań z listy w postaci [X]/[V] nazwa (priorytet)
def lista(tasks):
    if not tasks:
        print("Brak zadań.\n")
        return
    for i, j in enumerate(tasks, 1):
        mark = "[V]" if j["done"] else "[X]"
        print(f"{i}. {mark} {j['title']} ({j['priority']})")
    print()

# oznaczanie zadania jako wykonane
def zrob(tasks):
    try:
        n = int(input("Numer zadania: "))
        tasks[n-1]["done"] = True
        print("Oznaczono jako zrobione.\n")
    except:
        print("Zły numer.\n")

# usuwanie zadania
def usun(tasks):
    try:
        n = int(input("Numer do usunięcia: "))
        tasks.pop(n-1)
        print("Usunięto.\n")
    except:
        print("Zły numer.\n")

# zapis do pliku
def save(tasks):
    with open("tasks.txt", "w", encoding="utf-8") as taskfile:
        for task in tasks:
            taskfile.write(f"{task['title']}|{task['priority']}|{task['done']}\n")
    print("Zapisano.\n")

# wczytywanie z pliku
def load():
    tasks = []
    try:
        with open("tasks.txt", "r", encoding="utf-8") as taskfile:
            for line in taskfile:
                taskname, priority, status = line.strip().split("|")
                tasks.append({"title": taskname, "priority": priority, "done": status == "True"})
    except FileNotFoundError:
        pass
    return tasks

# sortowanie zadan po priorytecie
def sortuj(tasks):
    priorytety = ["wysoki", "sredni", "niski"]
    nowa_lista = []
    for p in priorytety:
        for zad in tasks:
            if zad["priority"] == p:
                nowa_lista.append(zad)
    tasks[:] = nowa_lista  # : oznacza wszystkie elementy
    lista(tasks)

# główna pętla programu
def main():
    tasks = load()
    while True:
        cmd = input("Co robisz? (dodaj/lista/zrob/usun/zapis/wczytaj/sort/koniec): ")

        if cmd == "dodaj":
            dodaj(tasks)
        elif cmd == "lista":
            lista(tasks)
        elif cmd == "zrob":
            zrob(tasks)
        elif cmd == "usun":
            usun(tasks)
        elif cmd == "zapis":
            save(tasks)
        elif cmd == "wczytaj":
            tasks = load()
        elif cmd == "sort":
            sortuj(tasks)
        elif cmd == "koniec":
            break
        else:
            print("Nie rozumiem.\n")

main()
