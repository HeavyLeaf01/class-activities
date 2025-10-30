from random import *
#bacteria: klebsiella
QtdPares = int(input("Quantos pares de bases você deseja?: "))
QtdParesTela = int(input("De quantos em quantos pares você deseja que apareça na tela: "))
bases = ['A', 'C', 'T', 'G']


def defbase(QtdPares):
    fita1=[]
    fita2=[]
    basesAT = 0
    basesCG = 0
    for k in range(QtdPares):
        fita1.append(bases[randint(0,3)])

        base1 = fita1[k]
        if base1 == "A":
            base2 = "T"
        elif base1 == "C":
            base2 = "G"
        elif base1 == "T":
            base2 = "A"
        elif base1 == "G":
            base2 = "C"

        fita2 +=[base2]
        if base1 == "A":
            basesAT += 1
        elif base1 == "C":
            basesCG += 1
        elif base1 == "T":
            basesAT += 1
        elif base1 == "G":
            basesCG += 1
        
    return (fita1, fita2, basesCG, basesAT)
    

cores = {'A' : "\033[0;31mA",
         'U' : "\033[0;32mU",
         'T' : "\033[0;32mT",
         'G' : "\033[0;34mG",
         'C' : "\033[0;37mC",
         '-' : "\033[0;36m-",
         '|' : "\033[0;36m|"}
fita1, fita2, basesCG, basesAT = defbase(QtdPares)
for i in range(0, QtdPares, QtdParesTela):
    escolha = input("Você deseja ver a próxima parte da sequência? (s/n): ")
    if escolha.lower() != "s":
        break

    for j in range(i, min(i + QtdParesTela, QtdPares)):
        print(f"{cores['|']}{cores[fita1[j]]}{cores['-']}{cores['-']}{cores[fita2[j]]}{cores['|']}")



#RNA

RNA = input("Você deseja ver o RNA? (s/n)")
if RNA.lower() == "s":  
    
    for i in range(len(fita1)):
        
        if fita1[i] == 'T':
            fita1[i] = 'U'
        if fita2[i] == 'T':
            fita2[i] = 'U'

    
    for j in range(QtdPares):
        print(f"{cores['|']} {cores[fita1[j]]}     {cores[fita2[j]]} {cores['|']}")
else:
    print("\033[0;31mFIM DA EXECUÇÃO")
basesAT = basesAT / QtdPares * 100 / 2

print(f"A {basesAT:.1f}%\nT {basesAT:.1f}%\n")

basesCG = basesCG / QtdPares * 100 / 2

print(f"C {basesCG:.1f}%\nG {basesCG:.1f}%\n")

