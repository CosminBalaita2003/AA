import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
import random
import math

n, precizie, nr_etape, chromosome_length, ind, p = 0, 0, 0, 0, 0, 0 # n = dimensiune populatie, precizie = precizia, nr_etape = numarul de etape, chromosome_length = lungimea cromozomului, ind = indice, p = precizia
maxx, p_recombinare, p_mutatie, minn, a, b = 0, 0, 0, 0, 0, 0 # maxx = maximul, p_recombinare = probabilitatea de recombinare, p_mutatie = probabilitatea de mutatie, minn = minimul, a = capatul din stanga al intervalului, b = capatul din dreapta al intervalului
cromozomi, new_gen = [], [] # cromozomi = lista de cromozomi, new_gen = lista de cromozomi pentru generatia urmatoare
vals, probs, intervale = [], [], [] # vals = valorile cromozomilor, probs = probabilitatile, intervale = intervalele 
viz, recombinare, aux = [], [], [] # viz = vector de vizitare, recombinare = vector de recombinare, aux = vector auxiliar

def transf_binar(nr): # functie pentru transformarea unui numar in binar
    binary = bin(nr)[2:].zfill(chromosome_length)
    return binary

def rotunjire(nr, p): # functie pentru rotunjire
    value = int(nr * p)
    return value / p

def functie2(x): # functie pentru calculul valorii functiei
    return c[0] * x ** 2 + c[1] * x + c[2]

def cautare_binara(x): 
    st, dr = 0, n - 1
    while st <= dr:
        mij = (st + dr) // 2
        if intervale[mij] <= x < intervale[mij + 1]:
            return mij
        if x < intervale[mij]:
            dr = mij - 1
        else:
            st = mij + 1
    return -1

def citire():
    global n, a, b, c, precizie, p_recombinare, p_mutatie, nr_etape 
    with open("date.in", "r") as file:
        n = int(file.readline().strip())  # citire dimensiune populatie
        a, b = map(float, file.readline().strip().split())  # citire domeniu de definitie
        c = list(map(int, file.readline().strip().split()))  # citire coeficienti
        precizie = int(file.readline().strip())  # citire precizie
        p_recombinare = float(file.readline().strip())  # citire probabilitate de recombinare
        p_mutatie = float(file.readline().strip())  # citire probabilitate de mutatie
        nr_etape = int(file.readline().strip())  # citire numar de etape
    print("Citire efectuata")

def afiare_evolutie():
    with open("evolution.txt", "r") as file:
        evolution_data = file.read()
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, evolution_data)

def main():
    global n, precizie, chromosome_length, p, maxx, a, b, cromozomi, new_gen, vals, probs, intervale, viz, recombinare, aux, ind, minn 
    citire()

    p = 10 ** precizie # calcul precizie
    chromosome_length = math.ceil(math.log2((b - a) * p)) # calcul lungime cromozom
    d = (b - a) / (2 ** chromosome_length - 1) # calcul pas

    with open("evolution.txt", "w") as file:
        file.write("Populatia initiala:\n")
        for i in range(1, n + 1): # generare populatie initiala
            x = random.randint(0, (1 << chromosome_length) - 1) # generare cromozom
            val_x = d * x + a # calcul valoare x 
            file.write(f"{i}: {transf_binar(x)} x= {val_x:.6f} f= {functie2(val_x):.6f}\n") 
            cromozomi.append(x) # adaugare cromozom in lista

        for gen in range(nr_etape): # pentru fiecare etapa
            
            total_fitness = sum(functie2(d * x + a) for x in cromozomi) # calcul fitness total 
            probs = [functie2(d * x + a) / total_fitness for x in cromozomi] # calcul probabilitati

            intervale = [sum(probs[:i+1]) for i in range(n)] # calcul intervale
            if gen == 0:
                file.write("\nProbabilitati selectie:\n")
                for i, prob in enumerate(probs, 1):
                    file.write(f"cromozom {i} probabilitate {prob:.9f}\n")
                file.write("\nIntervale probabilitati selectie:\n")
                for i, interval in enumerate(intervale):
                    file.write(f"{i} {intervale[i-1] if i > 0 else 0:.9f} {interval:.9f} " + ("\n" if i == n - 1 else "")) 
            
                    file.write("\nu= ")
                selected_chromosomes = []
                for _ in range(n):
                    u = random.random() 
                    selected_chromosome_index = next(i for i, interval in enumerate(intervale) if u < interval) # selectare cromozom
                    selected_chromosomes.append(selected_chromosome_index) # adaugare cromozom in lista
                    
                    file.write(f"{u:.6f} selectam cromozomul {selected_chromosome_index + 1}\n") 

                    recombinare = [i for i in range(n) if random.random() < p_recombinare] # selectare cromozomi pentru recombinare
            if gen == 0:
                file.write("\nCromozomii selectati pentru recombinare:\n")
                for i, index in enumerate(recombinare, 1):
                    file.write(f"{i}: {transf_binar(cromozomi[index])} x= {d * cromozomi[index] + a:.6f} f= {probs[index]:.6f}\n")
        
                file.write("\nProbabilitatea de incrucisare: " + str(p_recombinare) + "\n")
                file.write("Recombinare dintre cromozomii:\n")
                for i in range(0, len(recombinare), 2): # recombinare
                    if i + 1 < len(recombinare): 
                        file.write(f"cromozomul {recombinare[i] + 1} cu cromozomul {recombinare[i + 1] + 1}:\n")
                        punct1 = random.randint(1, chromosome_length - 1) # selectare punct de recombinare
                        punct2 = random.randint(1, chromosome_length - 1) # selectare punct de recombinare
                        if punct2 < punct1:
                            punct1, punct2 = punct2, punct1
                        file.write(f"{transf_binar(cromozomi[recombinare[i]])} {transf_binar(cromozomi[recombinare[i + 1]])} intre punct {punct1} {punct2}\n")
                        aux1 = cromozomi[recombinare[i]]
                        aux2 = cromozomi[recombinare[i + 1]]
                        
                        mask = (1 << (punct2 - punct1 + 1)) - 1
                        mask = mask << punct1
                        cromozomi[recombinare[i]] = (cromozomi[recombinare[i]] & ~mask) | (aux2 & mask)
                        cromozomi[recombinare[i + 1]] = (cromozomi[recombinare[i + 1]] & ~mask) | (aux1 & mask)

                        
                        
                        file.write(f"Rezultat {transf_binar(cromozomi[recombinare[i]])} {transf_binar(cromozomi[recombinare[i + 1]])}\n")

                       
            if gen ==0 :
                file.write("\nDupa recombinare:\n")
                for i, chromozome in enumerate(cromozomi, 1):
                    file.write(f"{i}: {transf_binar(chromozome)} x= {d * chromozome + a:.6f} f= {functie2(d * chromozome + a):.6f}\n")
            if gen==0: 
                file.write("\nProbabilitatea de mutatie: " + str(p_mutatie) + "\n")
                file.write("Au fost modificati cromozomii:\n")
                for i, chromozome in enumerate(cromozomi, 1):
                    if random.random() < p_mutatie:
                        file.write(f"{i}\n")
                        bit = 1 << random.randint(0, chromosome_length - 1)
                        cromozomi[i - 1] ^= bit
                file.write("\nDupa mutatie:\n")
                for i, chromozome in enumerate(cromozomi, 1):
                    file.write(f"{i}: {transf_binar(chromozome)} x= {d * chromozome + a:.6f} f= {functie2(d * chromozome + a):.6f}\n")
        
            maxx = max(functie2(d * x + a) for x in cromozomi)
            if gen == 0:
                file.write("\nEvolutia maximului:\n")
                for _ in range(n):
                    file.write(f"{maxx:.6f}\n")

def on_start_button_click():
    main()
    afiare_evolutie()
    root.after(1000, afiare_evolutie)
   
# Crearea interfetei grafice cu Tkinter
root = tk.Tk()
root.title("Evoluție algoritm evolutiv")

# Crearea unui camp de text pentru afisarea evolutiei
text_area = scrolledtext.ScrolledText(root, width=80, height=30, wrap=tk.WORD)
text_area.pack(expand=True, fill='both', side='left')

# Buton pentru a initia algoritmul si a afisa evolutia
start_button = tk.Button(root, text="Start Evoluție", command=on_start_button_click)
start_button.pack()

root.mainloop()