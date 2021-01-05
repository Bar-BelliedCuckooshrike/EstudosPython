"""
Raise - levantando erros:

- Raise -> lança exceções;
- Obs: Raise não é uma função, mas uma palavra reservada, feito <def> ou qualquer outra em python;
- Resumindo: pense no <raise> como sendo util para que possamos criar nossas proprias exceções
e mensagens de erro;
- A forma geral de utilização é:
    raise TipoDoErro('mensagem de erro')
"""
#Assim feito o <return>, o <raise> finaliza a função, ou seja, nada após ele será executado.

#Exemplo real:
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('O texto precisa ser string')
    if type(cor) is not str:
        raise TypeError('A cor precisa ser string')
    if cor not in cores:
        raise ValueError(f'Somente estas cores estão disponíveis: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Caderno', 'branco')