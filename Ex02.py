"""
    2) Faça um algoritmo recursivo que imprima os números de 1 até 20 na
tela chamando 20 vezes a função recursiva.
"""

def ate20(numero):
    if (numero < 21):
        print(numero)
        return ate20(numero + 1)
ate20(1)