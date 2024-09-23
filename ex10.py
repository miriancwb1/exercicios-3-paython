def vetor_ordenado(vetor):
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False
    return True

vetor = [1, 2, 3, 4, 5]
print("Vetor está ordenado:", vetor_ordenado(vetor))
