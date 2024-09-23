def contar_pares(vetor):
    contador = 0
    for elemento in vetor:
        if elemento % 2 == 0:
            contador += 1
    return contador

vetor = [1, 2, 3, 4, 5]
print("Quantidade de elementos pares:", contar_pares(vetor))
