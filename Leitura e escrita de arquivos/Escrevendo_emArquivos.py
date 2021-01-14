"""
Escrevendo em arquivos:

- Após indicar o caminho do arquivo, usamos o 'w' (write/escrever) para realizar a escrita.

- Ao abrir um arquivo, usamos a função 'write()' para escrever nele. Essa função recebe
uma string como parâmetro.

- Abrindo um arquivo para escrita com 'w', se o arquivo não existir, será criado.
Caso ele já exista, o anterior será apagado e um novo será criado; dessa forma, todo
o conteúdo no arquivo anterior é perdido.

obs: Ao abrir um arquivo para leitura, não podemos realizar a escrita neste, apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita não podemos lê-lo, somente escrever.

"""

#exemplo 01:
with open(r'C:\Users\Felipe\Desktop\testesPython\TestePython.txt', 'w') as pythonTest: #escrevemos
    pythonTest.write('Escrever dados em arquivo é izi demais, mlk seloco.\n')
    pythonTest.write('podemos colocar quantas linha quisermos.\n')
    pythonTest.write('ultima linha.\n')

arquivo = open(r'C:\Users\Felipe\Desktop\testesPython\TestePython.txt')
print(arquivo.read()) #lemos o que foi escrito

#exemplo 02 - escrevendo várias vezes a mesma palavra num arquivo:
with open(r'C:\Users\Felipe\Desktop\testesPython\novoPython.txt', 'w') as newPython:
    newPython.write('mongolão\n' * 30)

#exemplo 03 - recebendo dados do usuário e escrevendo no arquivo:
with open(r'C:\Users\Felipe\Desktop\testesPython\UsuarioPython.txt', 'w') as userPython:
    while True:
        refri = input('Informe um refri ou digite sair:')
        if refri != 'sair':
            userPython.write(refri + '\n')
        else:
            break


