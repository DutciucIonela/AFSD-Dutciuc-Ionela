#Date initiale
meniu=['papanasi'] * 10 + ['ceafa'] * 3 + ['guias'] * 6
preturi = [['papanasi',7], ['ceafa',10], ['guias'5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"] #coada FIFO
comenzi =  ["guias", "ceafa", "ceafa", "papanasi", "ceafa"] #coada FIFO
tavi = ["tava"] * 7  #stiva LIFO
istoric_comenzi = []

#1. Comenzi
for student, comanda in zip(studenti, comenzi):
    if len(tavi) == 0:
        print("Nu mai sunt tavi disponibile.")
        break
        #Procesam comanda
        print(f"{student} a comandat {comanda}.")
        studenti.pop(0) #Se elimina studentul din coada
        tavi.pop() #Se elimina tava din stiva
        comenzi.pop(0) #Se elimina comanda din coada
        istoric_comenzi.append(comanda)
#2. Inventar
#Se va calcula numarul de portii comandate pentru fiecare produs
comenzi_count = {produs: istoric_comenzi.count(produs) for produs in set(istoric_comenzi)}
#Afisarea inventarului
print(f"S au comandat {comenzi_count.get('guias',0)} guias, {comenzi_count.get('ceafa',0)} ceafa, {comenzi_count.get('papanasi',0)} papanasi.")
print(f"mai sunt {len(tavi)} tavi disponibile")
print(f"mai este ceafa: {'ceafa' in meniu}.")
print(f"mai sunt papanasi: {'papanasi' in meniu}.")
print(f"mai este guias: {'guias' in meniu}.")
#3. Finante
#Vom calcula totalul de incasari
total_incasari = sum([pret for produs, pret in preturi if produs in comenzi_count.keys()])
print(f"La cantina s-au incasat {total_incasari} lei.")
#Afisarea produselor care costa cel mult 7 lei
produse_ieftine = [produs for produs in preturi if produs[0] <= 7]
print(f"Produsele care costa cel mult 7 lei sunt: {produse_ieftine}")