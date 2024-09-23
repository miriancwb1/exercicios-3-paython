def soma_elementos(vetor):
    soma = 0
    for elemento in vetor:
        soma += elemento
    return soma

vetor = [1, 2, 3, 4, 5]
print("Soma dos elementos:", soma_elementos(vetor))