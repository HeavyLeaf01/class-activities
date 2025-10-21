def media(L):
    Soma = 0
    for v in L:
        Soma += v
    return Soma / len(L)

L = [7.0, 9.0, 10, 5.5, 7.5]

print(f"Média:{media(L)}")