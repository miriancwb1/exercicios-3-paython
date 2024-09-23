def maior_elemento(vetor):
    maior = vetor[0]
    for elemento in vetor:
        if elemento > maior:
            maior = elemento
    return maior

vetor = [1, 3, 2, 5, 4]
print("Maior elemento:", maior_elemento(vetor))