class Studentas:
    def __init__(self, vardas, amzius, pazymys, miestas, adresas):
        self.vardas = vardas
        self.amzius = amzius
        self.pazymys = pazymys
        self.miestas = miestas
        self.adresas = adresas

def tiesine_paieska(studentai, raktazodis):
    rasti_studentai = []
    for studentas in studentai:
        if raktazodis.lower() in studentas.vardas.lower():
            rasti_studentai.append(studentas)
    return rasti_studentai


def dvejetaine_paieska(studentai, raktazodis):
    studentai = sorted(studentai, key=lambda x: x.vardas.lower())
    pradzia = 0
    pabaiga = len(studentai) - 1
    rasti_studentai = []

    while pradzia <= pabaiga:
        vidurys = (pradzia + pabaiga) // 2
        if raktazodis.lower() == studentai[vidurys].vardas.lower():
            rasti_studentai.append(studentai[vidurys])
            # Patikrinti papildomus raktazodžio pasikartojimus
            i = vidurys - 1
            while i >= 0 and studentai[i].vardas.lower() == raktazodis.lower():
                rasti_studentai.append(studentai[i])
                i -= 1
            i = vidurys + 1
            while i < len(studentai) and studentai[i].vardas.lower() == raktazodis.lower():
                rasti_studentai.append(studentai[i])
                i += 1
            break
        elif raktazodis.lower() < studentai[vidurys].vardas.lower():
            pabaiga = vidurys - 1
        else:
            pradzia = vidurys + 1

    return rasti_studentai


def rikiavimas_pagal_skaiciu(studentai, key):
    return sorted(studentai, key=key)


def rikiavimas_pagal_abecele(studentai, key):
    return sorted(studentai, key=key)


def main():
    studentai = [
        Studentas("Jonas Petrauskas", 21, 8.7, "Vilnius", "Gedimino pr. 123"),
        Studentas("Petras Jonaitis", 20, 9.2, "Kaunas", "Laisvės al. 45"),
        Studentas("Ona Mikalauskienė", 22, 8.1, "Kaunas", "Vytauto pr. 67"),
        Studentas("Gabija Petrauskaitė", 19, 9.5, "Vilnius", "Saulėtekio al. 14"),
        Studentas("Tomas Kazlauskas", 21, 7.9, "Klaipėda", "Liepų g. 3"),
        Studentas("Mantas Jankauskas", 20, 8.3, "Vilnius", "Gedimino pr. 88"),
        Studentas("Eglė Butėnaitė", 22, 9.1, "Kaunas", "Vilniaus g. 21"),
        Studentas("Simona Navickaitė", 19, 9.6, "Klaipėda", "Taikos pr. 55"),
    ]

    pasirinkimas = ""
    while pasirinkimas != "0":
        print("Pasirinkite veiksmą:")
        print("1. Ieškoti pagal vardą")
        print("2. Ieškoti pagal kategoriją")
        print("3. Rikiuoti pagal skaičių")
        print("4. Rikiuoti pagal abėcėlę")
        print("0. Baigti programą")
        pasirinkimas = input("Įveskite veiksmo numerį: ")

        if pasirinkimas == "1":
            raktazodis = input("Įveskite ieškomą vardo dalį: ")
            rasti_studentai = tiesine_paieska(studentai, raktazodis)
            if rasti_studentai:
                for studentas in rasti_studentai:
                    print(f"Vardas: {studentas.vardas}")
                    print(f"Amžius: {studentas.amzius}")
                    print(f"Pažymys: {studentas.pazymys}")
                    print(f"Miestas: {studentas.miestas}")
                    print(f"Adresas: {studentas.adresas}")
                    print("-----------------------------")
            else:
                print("Studentų nerasta.")
            print()
        elif pasirinkimas == "2":
            print("Kategorijos:")
            print("1. Amžius")
            print("2. Vardas")
            print("3. Pažymys")
            print("4. Miestas")
            print("5. Adresas")
            kategorijos_pasirinkimas = input("Įveskite kategorijos pasirinkimą (1-5): ")

            raktazodis = input("Įveskite ieškomą reikšmę: ")
            rasti_studentai = []

            if kategorijos_pasirinkimas == "1":
                for studentas in studentai:
                    if str(studentas.amzius) == raktazodis:
                        rasti_studentai.append(studentas)
            elif kategorijos_pasirinkimas == "2":
                for studentas in studentai:
                    if studentas.vardas.lower() == raktazodis.lower():
                        rasti_studentai.append(studentas)
            elif kategorijos_pasirinkimas == "3":
                for studentas in studentai:
                    if str(studentas.pazymys) == raktazodis:
                        rasti_studentai.append(studentas)
            elif kategorijos_pasirinkimas == "4":
                for studentas in studentai:
                    if studentas.miestas.lower() == raktazodis.lower():
                        rasti_studentai.append(studentas)
            elif kategorijos_pasirinkimas == "5":
                for studentas in studentai:
                    if studentas.adresas.lower() == raktazodis.lower():
                        rasti_studentai.append(studentas)
            else:
                print("Neteisingas kategorijos pasirinkimas.")

            if rasti_studentai:
                for studentas in rasti_studentai:
                    print(f"Vardas: {studentas.vardas}")
                    print(f"Amžius: {studentas.amzius}")
                    print(f"Pažymys: {studentas.pazymys}")
                    print(f"Miestas: {studentas.miestas}")
                    print(f"Adresas: {studentas.adresas}")
                    print("-----------------------------")
            else:
                print("Studentų nerasta.")
            print()
        elif pasirinkimas == "3":
            print("Rikiavimo pagal skaičių pasirinkimai:")
            print("1. Amžius")
            print("2. Pažymys")

            rikiavimo_pasirinkimas = input("Įveskite rikiavimo pasirinkimą (1-2): ")

            if rikiavimo_pasirinkimas == "1":
                studentai = rikiavimas_pagal_skaiciu(studentai, key=lambda x: x.amzius)
            elif rikiavimo_pasirinkimas == "2":
                studentai = rikiavimas_pagal_skaiciu(studentai, key=lambda x: x.pazymys)
            else:
                print("Neteisingas rikiavimo pasirinkimas.")

            for studentas in studentai:
                print(f"Vardas: {studentas.vardas}")
                print(f"Amžius: {studentas.amzius}")
                print(f"Pažymys: {studentas.pazymys}")
                print(f"Miestas: {studentas.miestas}")
                print(f"Adresas: {studentas.adresas}")
                print("-----------------------------")
            print()
        elif pasirinkimas == "4":
            print("Rikiavimo pagal abėcėlę pasirinkimai:")
            print("1. Vardas")
            print("2. Miestas")
            print("3. Adresas")

            rikiavimo_pasirinkimas = input("Įveskite rikiavimo pasirinkimą (1-3): ")

            if rikiavimo_pasirinkimas == "1":
                studentai = rikiavimas_pagal_abecele(studentai, key=lambda x: x.vardas.lower())
            elif rikiavimo_pasirinkimas == "2":
                studentai = rikiavimas_pagal_abecele(studentai, key=lambda x: x.miestas.lower())
            elif rikiavimo_pasirinkimas == "3":
                studentai = rikiavimas_pagal_abecele(studentai, key=lambda x: x.adresas.lower())
            else:
                print("Neteisingas rikiavimo pasirinkimas.")

            for studentas in studentai:
                print(f"Vardas: {studentas.vardas}")
                print(f"Amžius: {studentas.amzius}")
                print(f"Pažymys: {studentas.pazymys}")
                print(f"Miestas: {studentas.miestas}")
                print(f"Adresas: {studentas.adresas}")
                print("-----------------------------")
            print()
        elif pasirinkimas == "0":
            print("Programa baigta.")
        else:
            print("Neteisingas veiksmo numeris. Bandykite dar kartą.")
        print()


if __name__ == "__main__":
    main()