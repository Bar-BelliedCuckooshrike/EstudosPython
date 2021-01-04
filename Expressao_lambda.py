"""
Expressão Lambda:

são funções sem nome, ou seja, funções anônimas;
uma expressão lambda pode ter mais de um argumento.
"""

#Função simples:
def funcao(x):
    return 3 * x + 1
print(funcao(7))

#Expressão lambda:
lambda x: 3 * x + 1

#Utilizando a expressão lambda:
calc = lambda x: 3 * x + 1 #essa não é a forma ideal de utilização.
print(calc(5))

#Utilizando uma expressão lambda com mais de um argumento:
calcular = lambda x, y: 2 * x**2 + y
print(calcular(3, 4))

#Outro exemplo:
autores = ['Liev Tolstoi', 'Gustave Flaubert', 'James Joyce', 'Gilberto Freire', 'Ítalo Calvino']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())#ordena alfabeticamente pelo sobrenome.
print(autores)

#Função quadrática: f(x) = ax² + bx + c:
def geradora_funcao_quadratica(a, b, c):
    return  lambda x: a * x**2 + b * x + c
teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

