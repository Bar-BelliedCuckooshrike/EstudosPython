"""
Listas:

em python, podemos colocar qualquer tipo de dado numa lista.
"""
lista1 = [1, 99, 22, 4, 88, 13, 13]

lista2 = ['g', 'e', 'f', 'l']

lista3 =[]

lista4 = list(range(11))

lista5 = list('Trinca Ferro')

# Podemos checar se determinado valor está contido na lista:
num = 7
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

# Podemos ordenar crescentemente uma lista:
lista1.sort()
lista5.sort()
print(lista1)
print(lista5)

# Podemos encontrar o número de ocorrências de um valor em uma lista:
print(lista1.count(13))
print(lista5.count('r'))

# Adicionar elementos em listas:
"""
Para adicionar elementos em listas, utilizamos a função append.

Obs: com append, só conseguimos adicionar um elemento por vez.
Obs: com extend, podemos colocar mais de um elemento por vez (mas apenas mais de um).
"""


print(lista1)
lista1.append(55)
print(lista1)

lista1.append([8, 9, 10, 11]) #adicionar numa lista um elemento do tipo lista
print(lista1)

if [8, 9, 10, 11] in lista1:
    print('encontrei a lista dentro da lista1')
else:
    print('nao encontrei a lista dentro da lista1 :c')

lista1.extend([123, 44, 67, 'Trinca Ferro']) #adicionar esses elementos dentro da lista, nao sendo lista dentro de lista
print(lista1)



