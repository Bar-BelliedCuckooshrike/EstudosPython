"""
Funções com retorno:
"""
def quadrado_de_3():
    return 3*3

retorno = quadrado_de_3() #uma variável pode receber uma função
print(f'o quadrado de 3 é: {retorno}')

#Podemos fazer operações matematicas junto com a função:
print(f'o quadrado de 3 + 2 é: {retorno + 2}')

#Retornar uma string:
def sayHi():
    return 'Hi everyone! :D'

print(sayHi())

#Função com varios returns:
def variosReturns():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'birl'

print(variosReturns())

#Função que retorna múltiplos valores:
def multiplosValores():
    return 2, 3, 4, 5

num1, num2, num3, num4 = multiplosValores() #se a função retorna vários valores, várias variáveis
                                            #podem recebe-la.
print(num1, num2, num3, num4) #entao printamos as variaveis que receberam os valores da função.

#Função para jogar a moeda(cara ou coroa):
from random import random #biblioteca Random que gera numeros aleatórios.

def cara_ou_coroa():
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'
print(cara_ou_coroa())