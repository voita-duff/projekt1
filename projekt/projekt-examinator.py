import os
import random
import time
from datetime import datetime
from colorama import Fore, Style

# Intervaly znamkovani
GRADES = {        
    1: (90, 100),
    2: (75, 90),
    3: (60, 75),
    4: (45, 60),
    5: (0, 45)
}

# Adresare ke zdrojum otazek a vysledkum testu
QUESTIONS_FOLDER = "Testy_zdroj_otazek"
RESULTS_FOLDER = "Testy_vysledky"

# Zmena working dir na projektovy root
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Vymaze konzoli
def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

# Nacte z txt souboru otazky
def load_questions_from_directory():
    # Pole otazek
    questions = []

    # Vsechny soubory v adresari
    for filename in os.listdir(QUESTIONS_FOLDER):
        if filename.endswith(".txt"):
            
            # Cesta k adresi, pak je otevreme
            path = os.path.join(QUESTIONS_FOLDER, filename)
            with open(path, 'r', encoding='utf-8') as file:
                author = file.readline().strip()
                text = file.read().strip()
                
                #questions_in_file = parse_questions(content, author, filename)
                blocks = text.split("\n\n\n")

                # Iterujeme bloky otazek
                for block in blocks:
                        lines = block.strip().split("\n")

                        question = {
                            'title': "",
                            'answers': [],
                            'correct': "",
                            'author': author,
                            'file': filename
                        }

                        for i, line in enumerate(lines):
                            # Prvni radek je otazka
                            if (i == 0):
                                 question['title'] = lines[i][8:].strip() ###
                            # Dalsi radky jsou odpovedi
                            else:
                                 # Je to spravna odpoved?
                                 if (lines[i].startswith("1;")):
                                    question['correct'] = lines[i][3:].strip()
                                 # Zaradime odpoved do zeznamu  
                                 question['answers'].append(lines[i][3:].strip())

                        questions.append(question)
    return questions

# Zamicha pole question
def shuffle_answers(questions):
    for question in questions:
        # Zamichame answers
        random.shuffle(question['answers'])

# Zepta se na cele jmeno
def get_full_name():
    full_name = input("Zadejte své celé jméno: ")
    return full_name

# Zepta se pocet otazek
def get_questions_count(total_questions):
    while True:
        try:
            questions_count = int(input(f"Zadejte počet otázek (max {total_questions}): "))
            if 1 <= questions_count <= total_questions:
                return questions_count
            else:
                print(f"[!] Zadejte číslo v rozsahu 1 až {total_questions}")
        except ValueError:
            print("[!] Zadejte platné číslo")

# Zepta se na konkretni otazku
def ask_question(question, index):
    clear_console()
    
    # Otazka s autorem, zdrojem a poradovym cislem
    print(Fore.LIGHTBLACK_EX + f"{question['author']} (zdroj: {question['file']})" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Otázka {index + 1}: {question['title']}\n" + Style.RESET_ALL)
    
    for i, answer in enumerate(question['answers']):
        print(f"{i + 1}. {answer}")

    # POUZE TEST: vypis spravne odpovedi
    ####print(Fore.MAGENTA + f"({question['correct']})" + Style.RESET_ALL)

    print()
    
    while True:
        try:
            user_answer = int(input("Zadejte číslo správné odpovědi: "))
            if 1 <= user_answer <= len(question['answers']):
                return question['answers'][user_answer - 1] == question['correct']
            else:
                print(f"[!] Zadejte číslo v rozsahu 1 až {len(question['answers'])}")
        except ValueError:
            print("Prosím zadejte platné číslo.")

# Oznamkuje odpovedi
def calculate_grade(score, questions_count):
    success_rate = (score / questions_count) * 100
    for grade, (min_percent, max_percent) in GRADES.items():
        if min_percent <= success_rate <= max_percent:
            return grade, success_rate
    return 5, success_rate

# Zapis do souboru ve vyzadovanem formatu
def save_test_result(full_name, total_questions, score, grade, success_rate, wrong_answers):
    # Casova znacka ve formatu
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Cilovy soubor
    filename = f"{full_name}_{timestamp}_{total_questions}_{grade}.txt"
    os.makedirs(RESULTS_FOLDER, exist_ok=True)
    filepath = os.path.join(RESULTS_FOLDER, filename)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(f"Vypracoval/a: {full_name}\n")
        file.write(f"Otázek v testu: {total_questions}\n")
        file.write(f"Výsledná známka: {grade}\n")
        file.write(f"Procentní úspěšnost: {success_rate:.2f} %\n")
        file.write(f"Stupnice: {GRADES}\n")
        file.write(f"Datum a čas vyhodnocení: {datetime.now().strftime('%d.%m.%Y, %H:%M:%S')}\n")
        if wrong_answers:
            file.write("\nChybně zodpovězeno:\n")
            for question in wrong_answers:
                file.write(f"\nOtázka: {question['title']}\n")
                for answer in question['answers']:
                    file.write(f"{answer}\n")

# Hlavni vstup do programu
def run_test():
    # Nacteme otazky
    questions = load_questions_from_directory()

    # Zeptame se na jmeno a pocet otazek
    full_name = get_full_name()
    questions_count = get_questions_count(len(questions))

    # Vygenerujeme nahodne otazky v zadanem poctu
    selected_questions = random.sample(questions, questions_count)
 
    # Zamichame odpovedi u vybranych otazek
    shuffle_answers(selected_questions)

    # Jake ma score a seznam spatnych otazek
    score = 0
    wrong_answers = []

    # Zobrazení otázek a zaznamenání odpovědí
    for i, question in enumerate(selected_questions):
        if ask_question(question, i):
            score += 1
        else:
            wrong_answers.append(question)

    # Výpočet známky a úspěšnosti
    grade, success_rate = calculate_grade(score, questions_count)

    # Výpis výsledků
    print(Fore.CYAN + "\nTest byl dokončen." + Style.RESET_ALL)
    print(f"Správně:\t\t{score}/{questions_count}")
    print(f"Procentní úspěšnost:\t{success_rate:.2f}%")
    print(f"Výsledná známka:\t{grade}")
    print()

    # Ulozeni vysledku
    save_test_result(full_name, questions_count, score, grade, success_rate, wrong_answers)

if __name__ == "__main__":
    clear_console()
    
    while True:
        run_test()
        repeat = input("Chcete test zopakovat? (ano/ne): ").lower()
        if repeat != "ano":
            break
