liczba_ocen = int(input("Podaj liczbę ocen, które chcesz wprowadzić: "))

suma_ocen = 0

for i in range(liczba_ocen):
    ocena = float(input(f"Podaj ocenę nr {i + 1} (w skali 1-6): "))
    suma_ocen += ocena

srednia = suma_ocen / liczba_ocen

print(f"\nTwoja średnia wynosi: {srednia:.2f}")

if srednia >= 3.0:
    print("Gratulacje! Uczeń zdał przedmiot.")
else:
    print("Niestety, uczeń nie zdał przedmiotu.")
