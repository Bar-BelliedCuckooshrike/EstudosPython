"""
Filter:

Serve para filtrar dados de uma determinada coleção.
"""
#Biblioteca para trabalhar com dados estatísticos:
import statistics

#Dados coletados de algum sensor:
dados =[1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando a média dos dados utilizando a função mean():
media = statistics.mean(dados)
print(f'Média: {media}')

#Assim como a função Map(), a filter() recebe dois parâmetros, sendo uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'venezuela']
result = filter(lambda pais: len(pais) > 0, paises)
print(list(result))

#Exemplo complexo:
usuarios = [
    {'username': 'felipe', 'tweets': ['Eu gosto de batata palha!', 'Gosto de pizza']},
    {'username': 'bruno', 'tweets': ['Eu gosto de mediocridades', 'sou superficial!']},
    {'username': 'leandro', 'tweets': []},
    {'username': 'indio', 'tweets': []}
]
print(usuarios)
#Filtrar usuarios sem tweets(inativos):
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(f'Usuarios inativos: {inativos}')
