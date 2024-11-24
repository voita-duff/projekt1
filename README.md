# projekt1
examinator

# Prg24-26_Project_01_Examinator_app

Project_01_Examinator_app.py

* Vytvořte terminálovou aplikaci, která bude čerpat otázky ze souborů z definovaného adresáře.
* Aplikace zatím nebude využívat OOP, resp. třídy a instance.
* Aplikaci vložíte jméno a příjmení zkoušeného.
* Aplikaci lze zadat počet otázek, které budou součástí aktuálního testu.
* Apliace náhodně vybere otázky, zamíchá jejich odpovědi, zobrazí postupně jednu po druhé, vždy smaže terminál, ať netřeba scrollovat.
* Aplikace vyhodnotí jednotlivé otázky.
* Na výstupu bude také počet správně a špatně zodpovězených otázek, procentní úspěšnost.
* Známka dle procentního rozdělení: <100-90>,(90-75>,(75-60>,(60-45>,(45-0>
* Možnost v kódu nastavit konstanty pro procentní rozdělení a jiné známkování - na jednom místě.
* Výsledek se vždy uloží do podadresáře "Vysledky_testu" ve tvaru: "prijmeni_jmeno_20241006_132845_pocetOtazek_znamka.txt"
* Formát souboru viz níže. 
* Možnost celý test zopakovat s nově vybranými otázkami ze souborů.
* U každé otázky bude vždy zobrazen autor a název souboru, ze kterého jsme čerpali.
* Aplikace hlídá vstupy od uživatele, množství otázek ze souboru a množství otázek v testu.


## SOUBOR S VÝSLEDKEM TESTU - definice
    Výsledek se vždy uloží do podadresáře "Vysledky_testu" 
    Pojmenování souboru bude ve tvaru: "prijmeni_jmeno_20241006_132845_pocetOtazek_znamka.txt"
    Uvnitř souboru bude vždy stejná struktura a vyhodnocení jednoho pokusu jednoho testu:


## SOUBOR S VÝSLEDKEM TESTU - ukázkový soubor "valek_vladislav_20241006_132845_10_2.txt"
        Vypracoval/a: Vladislav Válek
        Otázek v testu: 10
        Výsledná známka: 2
        Procentní úspěšnost: 80 %
        Stupnice: <100-90>,(90-75>,(75-60>,(60-45>,(45-0>
        Datum a čas vyhodnocení: 6.10.2024, 13:25:45

        ----------------------
        Chybně zodpovězeno:

        Otázka: Která z následujících možností představuje správnou syntaxi pro definici funkce v Pythonu? 
        definice funkce my_function(): 
        function my_function() {} 
        def my_function(): 
        fun my_function():

        Otázka: Který z následujících příkazů vytvoří řetězec v Pythonu? 
        'Hello, World!' 
        Hello, World! 
        12345 
        ["Hello", "World"]
        ----------------------


## SOUBOR S OTÁZKAMI - definice
Vždy musíte dodržet PŘESNĚ následující strukturu:
    Na prvním řádku je vždy uveden autor otázek.
    Každá otázka má před sebou 2x prázdný řádek.
    Otázka začíná slovem "Otázka:" a zadáním této otázky.
    Každá odpověď začíná nulou nebo jedničkou se středníkem a mezerou.
    Počet odpovědí je vždy 4, přitom je právě jedna z nich správná.
    Odpovědi ani otázky nejsou číslovány ani označeny písmeny - lze je tedy volně zamíchat, včetně míchání odpovědí.
    Název souboru s otázkami bude pojmenován dle vzoru: "valek_vladislav_otazky_libovolne_pojmenovani.txt"
    Bude uložen v podadresáři "Testy_zdroj_otazek"
Počet otázek v souboru bude minimálně 20. Lze jakkoliv využít cokoliv, každý autor ručí za správnost, nespoléhat se na ...


## SOUBOR S OTÁZKAMI - ukázkový soubor "valek_vladislav_otazky_albatros.txt"
        Autor: Vladislav Válek


        Otázka: Jakým způsobem se v Pythonu odliší blok řádků kódu, který patří k jedné funkci?
        0; Blok je uzavřen do trojitých uvozovek.
        0; Každý řádek začíná otazníkem.
        1; Všechny řádky jsou odsazeny ideálně o 4 mezery.
        0; Celý blok je uzavřen do složených závorek.


        Otázka: Která z následujících možností představuje správnou syntaxi pro definici funkce v Pythonu? 
        0; definice funkce my_function(): 
        0; function my_function() {} 
        1; def my_function(): 
        0; fun my_function():


        Otázka: Jakým způsobem definujeme seznam v Pythonu? 
        1; Použitím hranatých závorek: [1, 2, 3] 
        0; Použitím kulatých závorek: (1, 2, 3) 
        0; Použitím složených závorek: {1, 2, 3} 
        0; Pomocí příkazu create list


        Otázka: Jak lze v Pythonu získat délku seznamu my_list? 
        1; Použitím funkce len(my_list) 
        0; Použitím funkce size(my_list) 
        0; Použitím metody my_list.length() 
        0; Pomocí příkazu list_size(my_list)


        Otázka: Co vrátí následující příkaz: print(3 == 3)? 
        0; True, protože Python vrací vždy ve funkci print hodnotu True. 
        1; True, protože porovnání čísel je v Pythonu korektní a rovná se. 
        0; False, protože dvojité rovnítko není správný porovnávací operátor. 
        0; SyntaxError, protože je potřeba použít === pro porovnání.


        Otázka: Co se stane při pokusu o změnu prvku v n-tici (tuple)? Například my_tuple[0] = 10. 
        0; Prvek v n-tici bude změněn na novou hodnotu. 
        0; Python přepíše n-tici bez chybové hlášky. 
        0; Python automaticky vytvoří kopii n-tice. 
        1; Python vyvolá chybu, protože n-tice jsou neměnné (immutable).


        Otázka: Jakým způsobem lze importovat modul math a použít funkci sqrt pro výpočet druhé odmocniny v Pythonu? 
        1; import math; math.sqrt(16) 
        0; from sqrt import math(); sqrt(16) 
        0; import sqrt.math from math; sqrt(16) 
        0; include math.sqrt(16)


        Otázka: Který z následujících příkazů vytvoří řetězec v Pythonu? 
        1; 'Hello, World!' 
        0; Hello, World! 
        0; 12345 
        0; ["Hello", "World"]


        Otázka: Co se stane při použití příkazu my_list.append(10)? 
        0; Do seznamu bude vloženo číslo 10 na první pozici. 
        1; Do seznamu bude přidán prvek 10 na jeho konec. 
        0; Seznam bude zkopírován a číslo 10 bude přidáno do nové kopie. 
        0; Python vyvolá chybu, protože pro přidání prvku je potřeba použít add().
