"""
    3) Faça um algoritmo recursivo que some os valores de um vetor.
"""

def somaVetor(vet):
    if len(vet) == 1:
        return vet[0]
    else:
        return vet[0] + somaVetor(vet[1:])

vet = list(range(0, 100))

print(somaVetor(vet))