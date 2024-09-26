import os  
import random  


os.system("cls")






pytania_odpowiedzi = [
    ("Kto stworzył język Python?", "Guido van Rossum"),
    ("W którym roku stworzono język Python?", "1991"),
    ("Jaka jest najnowsza stabilna wersja Pythona (stan na wrzesień 2024)?", "Python 3.11"),
    ("Jakie rozszerzenie pliku ma skrypt Pythona?", ".py"),
    ("Jakie słowo kluczowe używamy, aby zdefiniować funkcję w Pythonie?", "def"),
    ("Jak zapisujemy komentarze w Pythonie?", "#"),
    ("Jakie są podstawowe typy danych w Pythonie?", "int, float, str, bool, list, tuple, dict, set"),
    ("Czym jest zmienna w Pythonie?", "Miejsce w pamięci przechowujące dane"),
    ("Jak w Pythonie wyświetlamy tekst na ekranie?", "print()"),
    ("Jakie jest domyślne kodowanie w Pythonie?", "UTF-8"),
    ("Jak w Pythonie tworzymy pętlę for?", "for i in range():"),
    ("Jak zdefiniować pętlę while w Pythonie?", "while warunek:"),
    ("Jak zakończyć działanie pętli w Pythonie?", "break"),
    ("Jak przejść do kolejnej iteracji pętli w Pythonie?", "continue"),
    ("Jak zdefiniować zmienną globalną wewnątrz funkcji?", "global"),
    ("Jaka jest różnica między listą a krotką w Pythonie?", "Lista jest zmienną, a krotka nie."),
    ("Jakie są wbudowane struktury danych w Pythonie?", "list, tuple, dict, set"),
    ("Czym jest wyrażenie lambda w Pythonie?", "Anonimowa funkcja"),
    ("Czym jest Python interpreter?", "Program wykonujący kod Pythona"),
    ("Co to jest PEP 8?", "Zasady stylu pisania kodu w Pythonie"),
    ("Jakie narzędzie używamy do zarządzania pakietami w Pythonie?", "pip"),
    ("Czym jest moduł w Pythonie?", "Plik zawierający definicje i instrukcje Pythona"),
    ("Jak zaimportować moduł w Pythonie?", "import nazwa_modulu"),
    ("Co oznacza wartość None w Pythonie?", "Brak wartości"),
    ("Jakie słowo kluczowe używamy do obsługi wyjątków w Pythonie?", "try"),
    ("Co oznacza słowo kluczowe 'pass' w Pythonie?", "Nic nie robi, pomija blok kodu"),
    ("Jak w Pythonie tworzymy listę składającą się z liczb od 0 do 9?", "list(range(10))"),
    ("Czy możemy pisać w VSC kod Pythona?", "tak"),
    ("Jakie słowo kluczowe używamy do stworzenia klasy w Pythonie?", "class"),
    ("Czym jest atrybut klasy w Pythonie?", "Właściwość klasy przechowująca dane"),
    ("Jak zdefiniować konstruktor klasy w Pythonie?", "__init__"),
    ("Jak zapisujemy instrukcję warunkową?", "if"),
    ("Jakie są instrukcję warunkowe w Pythonie?", "if, elif, else"),
]


def quiz():
    score = 0
    liczba_pytan = 33
    zadane_pytania = random.sample(pytania_odpowiedzi, liczba_pytan)
    
    for i, (pytanie, poprawna_odpowiedz) in enumerate(zadane_pytania, 1):
        print(f"Pytanie {i}: {pytanie}")
        odpowiedz = input("Twoja odpowiedź: ")
        
        if odpowiedz.lower() == poprawna_odpowiedz.lower():
            print("Poprawna odpowiedź!\n")
            score += 1
        else:
            print(f"Niepoprawna odpowiedź. Poprawna odpowiedź to: {poprawna_odpowiedz}\n")
    
    print(f"Twój wynik: {score}/{liczba_pytan} poprawnych odpowiedzi.")


quiz()