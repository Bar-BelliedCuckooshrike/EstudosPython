"""
Atributos:

- Representam as características do objeto. Pelos atributos, nós conseguimos
representar computacionalmente os estados de um objeto;

- Em Python, dividimos os atributos em 3 grupos:
    1. Atributos de instância;
    2. Atributos de classe;
    3. Atributos dinâmicos.

- Atributos de instância: são declarados dentro do método construtor.

- O duplo underline(__) é uma característica 'private'.

- Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público,
ou seja, pode ser acessado em todo o projeto. Caso queiramos demonstrar que determinado
atributo deve ser tratado como privado, ou seja, que deve ser acessado somente dentro
da própria classe onde está declarado, usamos duplo 'underline/underscore' no início
de seu nome. Isso é conhecido também como 'Name Mangling'.
"""

#classes com atributos de instância públicos:
class Lampada:
    #método construtor:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numConta, limite, saldo):
        self.numConta = numConta
        self.limite = limite
        self.saldo = saldo

class Produto:
    #atributo de classe
    imposto = 1.05
    contador = 0

    #atributo de instância:
    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

#classes com atributos de instância privados:
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

#acessando os atributos:
user = Acesso('felipesilva.cnt@gmail.com', '123456felipe')
user2 = Acesso('felipe_augusto08@hotmail.com', 'felipe123456')
print(user.email)
user.mostra_senha()
print(user2.email)
user2.mostra_senha()

#como em 'class Acesso' não podemos acessar o atributo privado 'senha', criamos
#um método dentro da classe para mostrar a senha. Se o email fosse privado,
#fariamos o mesmo para acessá-lo.

p1 = Produto('Playstation 4', 'Video-Game', 2300)
p2 = Produto('Xbox One', 'Caixa', 2000)

#não precisamos criar uma instância de classe para acessar um atributo de classe:
print(Produto.imposto)

print(p1.id)
print(p2.id)