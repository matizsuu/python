while True:
    choise = input("Konwersja stopni Celsjusza na Fahrenheita (C) lub Fahrenheita na stopnie Celsjusza (F) ")
    temperature = float(input("Podaj temperature: "))
    if choise == "C":
        result = temperature * 1.8 + 32
    elif choise == "F":
        result = (temperature - 32) / 1.8
    else:
        result = "Błąd: Nieprawidłowy wybór"
    
    print(result)
