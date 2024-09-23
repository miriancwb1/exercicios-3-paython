def produto_elementos(vetor):
    produto = 1
    for elemento in vetor:
        produto *= elemento
    return produto

vetor = [1, 2, 3, 4, 5]
print("Produto dos elementos:", produto_elementos(vetor))