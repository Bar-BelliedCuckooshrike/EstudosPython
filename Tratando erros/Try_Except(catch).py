"""
Try/Except(catch):

- Utilizamos o bloco try/except para tratar erros que podem ocorrer
em nósso código, previnindo, assim, que o programa pare de funcionar
e o usuário receba mensagens de erro inesperadas.

- A forma geral mais simples é:
try:
    //execução problemática
except:
    //o que deverá ser feito em caso de erro
"""

#Exemplo 1 - tratando um erro genérico:
try:
    uoco()
except:
    print('Deu algum erro aí, mlk')

print('-------------------------------------')

#Exemplo 2 - tratando um erro específico:
try:
    peça()
except NameError as err: #colocando o <as + QualquerNome> podemos puxar a mensagem de erro e mostrá-la.
    print(f'A aplicação gerou o seguinte erro: {err}')

print('-------------------------------------')

#Podemos efetuar diversos tratamentos de erros de uma vez:
try:
    birl()
except NameError as errA:
    print(f'Deu NameError: {errA}')
except TypeError as errB:
    print(f'Deu TypeError: {errB}')

print('-------------------------------------')

#Exemplo 3:
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
dic = {'nome': 'urso'}
print(pega_valor(dic, 'nome'))