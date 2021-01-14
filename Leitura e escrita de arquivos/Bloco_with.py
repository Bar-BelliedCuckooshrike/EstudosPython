"""
O Bloco 'With':

Para trabalhar com arquivos, seguimos alguns passos:
    1 - Abrimos o arquivo;
    2 - Manipulamos o arquivo;
    3 - Fechamos o arquivo.

O bloco 'with' é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco 'with'.
"""
#exemplo:
with open(r'C:\Users\Felipe\Desktop\TestePython.txt') as testePython:
    print(testePython.readlines())
    

#o bloco 'with' é a forma pythonica de manipular arquivos.