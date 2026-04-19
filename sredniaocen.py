# Pobranie liczby ocen od użytkownika
liczba_ocen = int(input("Podaj liczbę ocen, które chcesz wprowadzić: "))

suma_ocen = 0

# Pętla for do odczytania serii ocen
for i in range(liczba_ocen):
    ocena = float(input(f"Podaj ocenę nr {i + 1} (w skali 1-6): "))
    suma_ocen += ocena

# Obliczenie średniej
srednia = suma_ocen / liczba_ocen

# Wyświetlenie średniej
print(f"\nTwoja średnia wynosi: {srednia:.2f}")

# Instrukcja warunkowa sprawdzająca zaliczenie
if srednia >= 3.0:
    print("Gratulacje! Uczeń zdał przedmiot.")
else:
    print("Niestety, uczeń nie zdał przedmiotu.")