def maior_elemento(vetor):
    maior = vetor[0]
    for elemento in vetor:
        if elemento > maior:
            maior = elemento
    return maior

def menor_elemento(vetor):
    menor = vetor[0]
    for elemento in vetor:
        if elemento < menor:
            menor = elemento
    return menor

def diferenca_maior_menor(vetor):
    maior = maior_elemento(vetor)
    menor = menor_elemento(vetor)
    return maior - menor

vetor = [1, 3, 2, 5, 4]
print("Diferença entre maior e menor valor:", diferenca_maior_menor(vetor))
