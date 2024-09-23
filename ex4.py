def menor_elemento(vetor):
    menor = vetor[0]
    for elemento in vetor:
        if elemento < menor:
            menor = elemento
    return menor

vetor = [1, 3, 2, 5, 4]
print("Menor elemento:", menor_elemento(vetor))