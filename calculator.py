while True:
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    operacja = input("Wybierz operację (+, -, *, /): ")
    liczba2 = float(input("Podaj drugą liczbę: "))

    if operacja == "+":
        wynik = liczba1 + liczba2
    elif operacja == "-":
        wynik = liczba1 - liczba2
    elif operacja == "*":
        wynik = liczba1 * liczba2
    elif operacja == "/":
        if liczba2 == 0:
            wynik = "Błąd: Dzielenie przez 0"
        else:
            wynik = liczba1 / liczba2
    else:
        wynik = "Nieznana operacja"

    print("Wynik:", wynik)
    print("--------------------")
    
