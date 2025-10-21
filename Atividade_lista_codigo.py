L = [20, 7, 40, 3, 0]

def maior(lista):
    Maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > Maior:
            Maior = lista[i]
    return Maior
print(f"o maior número é {maior(L)}")

