import re  # Import modulu re pro regulární výrazy


class Pojistenci:
    def __init__(self):
        self.databaze_pojistencu = []  # Inicializace prázdné databáze

    def __str__(self):
        vysledek = []  # Seznam pro uložení formátovaných záznamů

        # Hlavička tabulky
        vysledek.append(f"{'Příjmení':<15} {'Jméno':<15} {'Věk':<5} {'Telefonní číslo':<15}"
                        f"\n--------------------------------------------------")

        # Formátování záznamů do sloupců
        for zaznam in self.databaze_pojistencu:
            vysledek.append(f"{zaznam['prijmeni']:<15} {zaznam['jmeno']:<15} {zaznam['vek']:<5} {zaznam['telefonni_cislo']:<15}")
        return "\n".join(vysledek)  # Vrátí všechny záznamy jako jeden řetězec oddělený novými řádky


# Třída pro přidávání nových pojištěnců do databáze
class PridaniPojistence:
    @staticmethod
    def validace_jmena(jmeno):
        return jmeno.isalpha() and jmeno.istitle()  # Kontrola, zda jméno obsahuje pouze písmena a začíná velkým písmenem

    @staticmethod
    def validace_telefonniho_cisla(telefonni_cislo):
        return re.match(r'^\+?\d+$', telefonni_cislo) is not None  # Kontrola, zda telefonní číslo obsahuje pouze číslice a volitelně znak '+'

    @staticmethod
    def validace_veku(vek):
        return vek.isdigit() and 0 <= int(vek) <= 122  # Kontrola, zda je věk číslo mezi 0 a 122

    def pridej_zaznam(self, pojisteni):
        prijmeni = ""
        jmeno = ""
        telefonni_cislo = ""
        vek = 0

        prijmeni_validovano = False
        while not prijmeni_validovano:
            prijmeni = input("\nZadej příjmení pojištěnce: ")
            if self.validace_jmena(prijmeni):
                prijmeni_validovano = True
            else:
                print("\nZadané příjmení je nesprávné. Příjmení musí obsahovat pouze písmena a začínat velkým písmenem.")

        jmeno_validovano = False
        while not jmeno_validovano:
            jmeno = input("Zadej jméno pojištěnce: ")
            if self.validace_jmena(jmeno):
                jmeno_validovano = True
            else:
                print("\nZadané jméno je nesprávné. Jméno musí obsahovat pouze písmena a začínat velkým písmenem.")

        telefonni_cislo_validovano = False
        while not telefonni_cislo_validovano:
            telefonni_cislo = input("Zadej telefonní číslo pojištěnce: ")
            if self.validace_telefonniho_cisla(telefonni_cislo):
                telefonni_cislo_validovano = True
            else:
                print("\nZadané telefonní číslo je nesprávné. Telefonní číslo musí obsahovat pouze číslice bez dodatečných mezer. Je také možné zadat předčíslí, které začíná znaménkem '+'.")

        vek_validovano = False
        while not vek_validovano:
            vek = input("Zadej věk pojištěnce: ")
            if self.validace_veku(vek):
                vek = int(vek)
                vek_validovano = True
            else:
                print("\nZadaný věk není správný. Zadané číslo musí být vyšší než 0 a nižší než 122.")

        # Kontrola, zda již záznam se stejnými údaji neexistuje
        for zaznam in pojisteni.databaze_pojistencu:
            if zaznam['prijmeni'] == prijmeni and zaznam['jmeno'] == jmeno and zaznam['vek'] == vek and zaznam['telefonni_cislo'] == telefonni_cislo:
                print("\nZáznam pro tuto osobu již existuje. Zadejte prosím znovu.")
                self.pridej_zaznam(pojisteni)  # Restartování procesu přidávání záznamu
                return

        # Přidání nového záznamu do databáze
        pojisteni.databaze_pojistencu.append({
            "prijmeni": prijmeni,
            "jmeno": jmeno,
            "telefonni_cislo": telefonni_cislo,
            "vek": vek
        })

        print("\nOsoba byla úspěšně přidána do databáze. Pro pokračování zvolte klávesu 'Enter'...")
        input()


# Třída pro zobrazení všech pojištěnců v databázi
class ZobrazeniPojistencu:
    @staticmethod
    def zobraz_zaznamy(pojisteni):
        print(f"\n{pojisteni}")  # Vytiskne všechny záznamy pomocí metody __str__ třídy Pojistenci
        print("\nToto jsou záznamy které se aktuálně nacházejí v databázi. Pro pokračování zvolte klávesu 'Enter'...")
        input()


# Třída pro vyhledávání pojištěnců v databázi
class VyhledaniPojistence:
    @staticmethod
    def vyhledej_zaznam(pojisteni, prijmeni, jmeno):
        # Kontrola, zda záznam existuje v databázi
        nalezeno = False
        for zaznam in pojisteni.databaze_pojistencu:
            if zaznam['prijmeni'] == prijmeni and zaznam['jmeno'] == jmeno:
                print(f"\n{zaznam['prijmeni']:<15} {zaznam['jmeno']:<15} {zaznam['vek']:<5} {zaznam['telefonni_cislo']:<15}")
                nalezeno = True
        if not nalezeno:
            print("\nPod tímto jménem se v databázi nenachází žádný pojištěnec.")
        print("\nVýše jsou viditelné výsledky vyhledávání. Pro pokračování zvolte klávesu 'Enter'...")
        input()


# Hlavní funkce programu
def main():
    pojistenci = Pojistenci()  # Inicializace databáze pojištěnců
    pridani_pojistence = PridaniPojistence()  # Inicializace třídy pro přidávání pojištěnců
    vyhledavani = VyhledaniPojistence()  # Inicializace třídy pro vyhledávání pojištěnců
    zobrazeni = ZobrazeniPojistencu()  # Inicializace třídy pro zobrazení pojištěnců

    program_spusten = True
    while program_spusten:
        print("----------------------------------------")
        print("Evidence pojištěnců")
        print("----------------------------------------")
        print("\n1. Přidání nového záznamu do databáze")
        print("2. Vyhledání záznamu v databázi")
        print("3. Výpis všech záznamů z databáze")
        print("4. Ukončení programu")

        moznost = input("\nProsím zvolte číslo jedné z těchto možností: ")

        if moznost == '1':
            pridani_pojistence.pridej_zaznam(pojistenci)  # Přidání nového záznamu
        elif moznost == '2':
            prijmeni_vyhledavani = input("\nZadejte příjmení osoby kterou chcete vyhledat: ")
            jmeno_vyhledavani = input("Zadejte jméno osoby kterou chcete vyhledat: ")
            vyhledavani.vyhledej_zaznam(pojistenci, prijmeni_vyhledavani, jmeno_vyhledavani)  # Vyhledání záznamu
        elif moznost == '3':
            print("Databáze:")
            zobrazeni.zobraz_zaznamy(pojistenci)  # Zobrazení všech záznamů
        elif moznost == '4':
            program_spusten = False
            print("Program byl úspěšně ukončen.")  # Ukončení programu
        else:
            print("Vámi zvolená možnost se nenachází v seznamu viditelněm výše. Prosím zadejte znovu.")


# Spuštění hlavní funkce
if __name__ == "__main__":
    main()
