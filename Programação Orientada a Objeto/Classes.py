"""
Classes:

- Em POO(programação orientada a objeto), classes nada mais são que modelos dos objetos
do mundo real sendo representados computacionalmente.

- Classes podem conter:
    1. Atributos -> Características do objeto;
    2. Métodos (funções) -> Representam o comportamento do objeto. São subprogramas que realizam
    alguma ação sobre um objeto.

- Em Python usamos a palavra reservada 'class' para definir uma classe.

- Utilizamos a palavra 'pass', em Python, quando temos um bloco de código
que ainda não está implementado.

- Quando nomeamos uma classe em Python, usamos, por convenção, o nome com inicial em maiúsculo;
se o nome for composto, usa-se as iniciais de ambas as palavras em maiúsculo, todas juntas.
"""

class Lampada:
    pass

lamp = Lampada()
print(type(lamp))
