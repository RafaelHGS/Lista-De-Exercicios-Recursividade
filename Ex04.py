"""
    4) Faça um algoritmo recursivo que encontre o maior valor em um vetor
de inteiros
"""
import random

def maiorValor(vet):
    if len(vet) == 1:
        return vet[0]
    return (vet[0] + maiorValor(vet[1:]) + abs(vet[0] - maiorValor(vet[1:])))/2

def main():
    vet = []
    for numeroAleatorio in range(0,20):
        numeroAleatorio = random.randint(0,1000)
        vet.append(numeroAleatorio)
    print("\n\t\tEssa é a nossa lista/vetor gerado aleatoriamente:\n",vet, sep="")
    print(f"\nEsse é o maior valor encontrado em nossa lista/vetor: {maiorValor(vet):.0f}\n")


if __name__ == "__main__":
    main()
