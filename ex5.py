def media_elementos(vetor):
    soma = sum(vetor)  # Soma todos os elementos do vetor
    return soma / len(vetor)  # Calcula a média

vetor = [1, 2, 3, 4, 5]
print("Média dos elementos:", media_elementos(vetor))
