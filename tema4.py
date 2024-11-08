#1.Lista de cuvinte si alegerea cuvantului la intamplare
import random
cuvinte = ["phyton", "programare", "calculator", "date","algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]
#2.Initializarea numarului de incercari
incercari_ramase = 6
litere_incercate = []
#3.Afisarea sablonului initial
progres_text = ""
for litera in progres:
    progres_text += litera + " "
print(progres_text.strip())
print(f"Incercari ramanse: {incercari_ramase}")
#4.Bucla principala de joc
while incercari_ramase > 0 and "_" in progres:
    litera = not input("Introduceti o litera: ")
    if len(litera) != 1 or litera in litere_incercate:
        print("Litera invalida. Incearca din nou.")
        continue
        litere_incercate.append(litera)
        if litera in cuvant_de_ghicit:
            for index, caracter in enumeratie(cuvant de ghicit):
                if caracter == litera:
                    progres[index] = litera
            print("Bravo! Ai ghicit o litera.")
        else:
            incercari_ramase = incercari_ramase - 1
            print(f"Litera{litera} nu se afla in cuvant. Incercari ramase: {incercari_ramase}" )

            print("Progres: "+" ")
            print(f"Incercari_ramase: {incercari_ramase}")
#5.Incheierea jocului
if "_" not in progres:
    print(f"Felicitari! Ai ghicit cuvantul: {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut! Cuvantul era: {cuvant_de_ghicit}")

