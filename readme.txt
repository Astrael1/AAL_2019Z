Szymon Małolepszy, 293149
Tablica mieszająca
W14 - wielokrotne wyliczanie funkcji skrótu przy kolizji
W22 - generowanie na podstawie próbki tekstu
W31 - enumeracja

Uruchamianie:
python3 generator.py -c -i filename.txt - skonfiguruj generator plikiem filename.txt
python3 generator.py -g N - wygeneruj N słów
python3 generator.py -g N -o filename.txt - wygeneruj N słów i zapisz do pliku filename.txt
python3 generator.py -g N -n K - wygeneruj N słów o długości K

-a - dopisz wyjście na końcu pliku

python3 program.py -t1 - read number N and add N words from input to table
python3 program.py -t2 - read number N and remove N words from input to table
python3 program.py -t3 - read number N and add N words from input to table, then read number M and remove M words from input
python3 program.py -t4 - read number N and add N words from input to table, then write all words added

-v - na koniec wypisz zawartość tablicy ( nie działa w trybie t4)
-t - wypisz czas wykonywania operacji (t1 - dodawanie, t2, t3 - usuwanie, t4 - enumeracja)

Wejście/wyjście:
Generator przyjmuje na wejście plik testowy w celu konfiguracji.
Zapisuje wyniki w pliku config.json. Na wyjście generator wypisuje liczbę wszystkich wyrazów N, a następnie wygenerowane wyrazy.

Program testujący przyjmuje na wejście liczbę wyrazów N, a następnie dokładnie tyle wyrazów. W trybie t3 należy wprowadzić dwa takie zestawy.
W zależności od parametrów program testujący wypisuje czas operacji i/lub zawartość tablicy po nich.

Algorytmy:
Funkcja skrótu opiera się na przemnażaniu kolejnych liczb wyrazu przez 300 (liczba wyższa od każdego kodu) oraz modulację przez 102499 (duża liczba pierwsza). Dodatkowo do każdego kodu znaku jest dodawana poprzednia wartość funkcji skrótu w celu spełnienia wymogów zadania.

Przy dodawaniu i usuwaniu elementów z tablicy prowadzony jest zapis wszystkich wartośći funkcji skrótu. Jeśli któraś się powtórzy - doszło do zapętlenia. W takim wypadku zgłaszany jest wyjątek.

Pliki:
table.py - zawiera implementację klasy tablicy mieszającej
generator.py - generator wymagany w zadaniu
program.py - program stworzony do testów; wywołuje różne metody tablicy mieszającej

