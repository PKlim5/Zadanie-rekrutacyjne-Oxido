import openai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

def read_article(file_path):
    """Funkcja odczytująca treść artykułu z pliku tekstowego."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def choose_prompt(article_text):
    """Funkcja umożliwiająca wybór promptu przez użytkownika."""
    
    prompts = [
    'Nie modyfikując tekstu artykułu przekształć go do formatu HTML, wykorzystując odpowiednie tagi HTML do strukturyzacji treści (<h1>, <h2>, <p>). Rozpoznaj tytuły, nagłówki oraz przypisy. '
    'Dodaj obrazy za pomocą tagu <img src="image_placeholder.jpg"> i dodaj do każdego obrazka atrybut alt zawierający prompt do wygenerowanie tej grafiki oraz podpis pod nim w tagu <figcaption>. '
    'Zawartość powinna być przeznaczona do wstawienia między tagi <body> i </body> (te pomijaj). Nie dodawaj CSS ani JavaScript. ',


    'Przekształć poniższy tekst w stronę HTML. Użyj odpowiednich tagów HTML rozpoznając rolę tekstu (tytuł, nagłówek itp.), takich jak nagłówki (<h1>, <h2>, <h3>), akapity (<p>) oraz listy. '
    'Dodaj obrazy w odpowiednich miejscach za pomocą tagu <img src="image_placeholder.jpg"> z atrybutem alt, który będzie zawierał prompt do wygenerowania tej grafiki oraz odpowiednim podpisem <figcaption>. '
    'Wygenerowany kod powinien zawierać wyłącznie zawartość do wstawienia między tagi <body> i </body> (te pomijaj). Nie uwzględniaj stylów ani JavaScript pozostaw tekst w oryginalnej formie. ',


    'Przeformatuj poniższy tekst na strukturę HTML z odpowiednimi tagami. Rozpoznaj sekcje, takie jak nagłówki, akapity, listy, oraz miejsca na przypisy. '
    'Dodaj tagi <img src="image_placeholder.jpg"> tam, gdzie sugerowane są ilustracje, wraz z atrybutem alt zawierającym prompt do wygenerowania obrazu. Umieść podpis pod każdym obrazkiem w tagu <figcaption>. '
    'Zwrócony kod HTML powinien być gotowy do wstawienia między <body> i </body> (te pomijaj), bez modyfikowania treści artykułu, dodawania CSS i JavaScript.'
    ]

    loop_active = True

    while loop_active:
        print("\nWybierz jeden z poniższych promptów lub wpisz własny:")
        for i, prompt in enumerate(prompts, 1):
            print(f"{i}. {prompts[i-1]}")
        print("4. Wpisz własny prompt")

        try:
            choice = int(input("\nPodaj numer opcji (1-4): "))

            if 1 <= choice <= 3:
                prompt = f'{prompts[choice - 1]} W odpowiedzi zawrzyj jedynie kod. Oto artykuł:\n"{article_text}"'
                loop_active = False
                return prompt

            elif choice == 4:
                print('Na koniec wpisanego promptu dodawana jest fraza - "Oto artykuł: <treść artykułu>". Nie ma potrzeby cytowania artykułu')
                custom_prompt = input("\nWpisz swój własny prompt: ")
                prompt = f'{custom_prompt} W odpowiedzi zawrzyj jedynie kod. Oto artykuł:\n"{article_text}"'
                loop_active = False
                return prompt

            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")
                loop_active = True
        
        except ValueError:
            print("Nieprawidłowy wybór. Wprowadź liczbę od 1 do 4.")
            loop_active = True


def generate_html_content(prompt):
    """Funkcja generująca kod HTML na podstawie promptu."""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "user",
                "content": prompt,
            }],
        )

        html_content = response['choices'][0]['message']['content']
        return html_content.strip()
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_html_file(html_content, file_path):
    """Funkcja zapisująca kod HTML do pliku artykul.html."""
    
    if html_content is None:
        print("Błąd: Nie udało się wygenerować kodu HTML.")
        return
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Plik HTML został zapisany jako {file_path}")


def main():
    loop_active = True

    while loop_active:
        article_text = read_article("artykul.txt")
        prompt = choose_prompt(article_text)
        html_content = generate_html_content(prompt)        
        save_html_file(html_content, "artykul.html")

        retry = input("\nCzy chcesz przetworzyć kolejny artykuł? (tak/nie): ").strip().lower()        
        if retry not in ["tak", "t"]:
            print("Zakończono działanie programu.")
            loop_active = False


if __name__ == "__main__":
    main()