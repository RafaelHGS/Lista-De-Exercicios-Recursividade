"""
    1) Faça um algoritmo recursivo que imprima os números de 20 até 1 na
tela chamando 20 vezes a função recursiva.
"""

def de20Ate1(numero):
    if(numero > 0):
        print(numero)
        return de20Ate1(numero - 1)


de20Ate1(20)