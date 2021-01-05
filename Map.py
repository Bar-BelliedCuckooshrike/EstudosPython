"""
Map:

com MAP fazemos o mapeamento de valores para uma função.
"""

import math

def area(r): #calcula a área de um circulo com raio r.
    return math.pi * (r**2)
print(area(3))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

print('--------------------------')

#Forma 1 - comum:
areas = []
for r in raios:
    areas.append((area(r)))
print(areas)

print('--------------------------')

#Forma 2 - Map:
#Map é uma função que recebe dois parâmetros: o primeiro, a função; o segundo, um iterável.
#Retorna um Map Object
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

print('--------------------------')

#Forma 3 - Map com Lambda:
print(list(map(lambda r: math.pi * (r**2), raios)))

print('--------------------------')

#Mais um exemplo:
cidades = [('Curitiba', 20), ('São Paulo', 22), ('Minas Gerais', 31), ('Buenos Aires', 19), ('Los Angeles', 26),
           ('Nova York', 3), ('Londres', 13)]
print(cidades)

#F = 9/5 * c + 32:
celcius_to_F = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(celcius_to_F, cidades)))


#O MAP é simples, basta colocar a função e o iterável.
