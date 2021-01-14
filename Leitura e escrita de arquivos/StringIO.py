"""
StringIO:

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional, o software precisa
de permissão:
    - Permissão de leitura do arquivo;
    - Permissão de escrita do arquivo;

- StringIO: utilizado para ler e criar arquivos em memória.
"""
#exemplo 01:
#primeiro fazemos o import:
from io import StringIO

mensagem = 'este é apenas uma string qualquer'

#podemos criar um arquivo em memória já com uma string inserida
#ou mesmo vazio, para inserirmos um texto depois.

arquivo = StringIO(mensagem) #equivalente a: arquivo = open('arquivo.txt', 'w')

#agora, tendo o arquivo, podemos usar tudo o que já sabemos sobre leitura/escrita de arquivos.
print(arquivo.read())

#escrevendo outro texto:
arquivo.write(' outro texto qualquer')
arquivo.seek(0)
print(arquivo.read())
