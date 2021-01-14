"""
Leitura de arquivos:

para ler o conteúdo de um arquivo em python, usamos a função integrada 'open()',
que literalmente significa 'abrir'.

open() -> A forma mais simples de utilização é passando apenas um parâmetro de entrada,
que neste caso é o nome/caminho do arquivo a ser lido. Essa função retorna um '_io.TextIOWrapper',
e é com ele que trabalhamos.

obs: por padrão, a função 'open()' abre o arquivo para leitura. Este arquivo deve existir ou
então teremos o erro 'FileNotFoundError'

obs: para abrir um arquivo que nao está nas pastas do python, usamos o 'r' antes do caminho do arquivo.
"""

# exemplo:
arquivo = open(r'C:\Users\Felipe\Desktop\passosGit.txt')
print(arquivo.read()) #utilizar '.read()' para ler o conteúdo do arquivo
print(type(arquivo))
