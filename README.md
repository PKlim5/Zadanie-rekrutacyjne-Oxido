# Działanie aplikacji

### 1. Struktura projektu
├── venv/                - środowisko wirtualne Pythona
├── .env                 - plik zawierający klucz API OpenAI
├── artykul.html         - plik wyjściowy z wygenerowanym kodem HTML
├── main.py              - główny plik aplikacji
├── artykul.txt          - plik z treścią artykułu do przetworzenia
├── podglad.html         - plik z przykładowym wyglądem wygenerowanej strony
├── szablon.html         - szablon do podglądu wstawionego kodu HTML

### 2. Opis działania poszczególnych funkcji wewnątrz main.py:

#### a) Konfiguracja API OpenAI
- Aplikacja korzysta z biblioteki dotenv, aby wczytać klucz API OpenAI z pliku .env.
- Klucz API jest przypisany do openai.api_key, co umożliwia autoryzowane zapytania do API OpenAI.

#### b) Funkcja read_article(file_path)
- Odczytuje treść artykułu z pliku tekstowego (domyślnie artykul.txt).
- Zwraca tekst artykułu jako ciąg znaków.

#### c) Funkcja choose_prompt(article_text)
- Pozwala użytkownikowi wybrać jeden z trzech gotowych promptów lub wprowadzić własny.
- Prompt jest podstawą do zapytania API OpenAI, gdzie artykuł zostaje przekształcony na HTML.
- Funkcja łączy wybrany prompt z treścią artykułu i zwraca całą zapytanie jako prompt.

#### d) Funkcja generate_html_content(prompt)
- Wysyła zapytanie do API OpenAI z wykorzystaniem modelu gpt-4 i promptu od użytkownika.
- Pobiera odpowiedź z wygenerowanym kodem HTML i zwraca go jako html_content.
- W przypadku błędu funkcja zwraca None i wyświetla komunikat o błędzie.


#### e) Funkcja save_html_file(html_content, file_path)
- Zapisuje wygenerowany kod HTML do pliku artykul.html.
- Jeśli html_content jest None, informuje użytkownika o błędzie.

#### f) Funkcja main()
Jest to główna pętla programu:
- Odczytuje treść artykułu.
- Umożliwia użytkownikowi wybór promptu.
- Generuje kod HTML za pomocą OpenAI API.
- Zapisuje wynikowy HTML do pliku artykul.html.
- Pyta użytkownika, czy chce przetworzyć kolejny artykuł. Jeśli nie, kończy działanie programu.

# Instrukcja obsługi projektu

## Wymagania wstępne
- **Python** w wersji 3.7 lub wyższej
- Środowisko programistyczne, np. [Visual Studio Code](https://code.visualstudio.com/)
- Klucz API do **OpenAI**

## Instalacja i uruchomienie

### 1. Sklonuj lub pobierz repozytorium
- Sklonowanie repozytorium za pomocą komendy: git clone https://github.com/PKlim5/Zadanie-rekrutacyjne-Oxido
Można również pobrać repozytorium jako plik ZIP i rozpakować go na komputerze.

### 2. Otwórz projekt w środowisku programistycznym
Uruchom Visual Studio Code lub inne wybrane środowisko IDE.
Otwórz folder z repozytorium w środowisku.

### 3. Dodaj klucz API
W katalogu głównym projektu znajduje się plik .env.
Otwórz plik i dodaj swój klucz API w następujący sposób: OPENAI_API_KEY="twój_klucz_api"

### 4. Utwórz i uruchom środowisko wirtualne
Aby uniknąć problemów z zależnościami, zaleca się korzystanie ze środowiska wirtualnego.
Utwórz środowisko wirtualne za pomocą komendy: python -m venv venv
Następnie aktywuj środowisko: .\venv\Scripts\activate

### 5. Zainstaluj wymagane pakiety
Przed uruchomieniem projektu zainstaluj wszystkie zależności: pip install -r requirements.txt

### 6. Uruchom aplikację
W środowisku wirtualnym uruchom plik main.py: python main.py

### 7. Wybierz prompt
Po uruchomieniu programu zobaczysz listę dostępnych promptów. Wybierz jeden z nich, wpisując przypisaną cyfrę, lub wpisz swój własny prompt.

### 8. Poczekaj na odpowiedź
Aplikacja wyśle zapytanie do API OpenAI i zapisze odpowiedź.

### 9. Generowanie artykułu
Po zakończeniu operacji, jeśli wszystkie kroki zostały wykonane poprawnie, pojawi się komunikat o wygenerowaniu pliku artykul.html.
Można przenieść zawartość artykul.html do pliku szablon.html w sekcji <body></body>, aby zastosować gotowy szablon.

### 10. Podgląd pliku HTML
Otwórz plik szablon.html w przeglądarce, jeśli korzystasz z Visual Studio Code, można uruchomić plik za pomocą rozszerzenia Live Server.
Alternatywnie, otwórz plik ręcznie w eksploratorze plików.

## Uwagi
Aby powtórzyć działanie programu, wpisz odpowiednią komendę ("tak") po odpowiednim komunikacie.
W przypadku problemów z uruchomieniem środowiska wirtualnego, upewnij się, że masz zainstalowany Python w systemowej ścieżce oraz skonfigurowane uprawnienia do uruchamiania skryptów.

## Autor
Przemysław Klimek