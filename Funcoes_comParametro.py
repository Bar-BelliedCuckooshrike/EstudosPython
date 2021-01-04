"""
Funções com parâmetro:
"""
def quadrado(numero):
    return numero ** 2

print(quadrado(4))
print(quadrado(5))
print(quadrado(6))

def olaHumano(humano):
    print(f'olá, {humano}')
olaHumano('felipe')

def nome_completo(nome, sobrenome):
    return f'seu nome completo é: {nome} {sobrenome}'
print(nome_completo('Felipe', 'Augusto'))