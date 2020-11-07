'''
Crie um dicionário para armazenar uma listagem de alunos.
 - Utilize como chave o RA do aluno e como valor o nome do aluno.
 - O RA de cada aluno deve ser composto por um número inteiro de 7 dígitos.
 - Caso o RA informado não esteja no formato correto, deve gerar uma
   exceção ValueError
 - Caso o RA informado já exista no dicionário, deve ser gerada uma
   exceção do tipo TypeError

Implemente a função buscar, que recebe como parâmetros de entrada o dicionário
 e o RA de um aluno e retorna o nome desse aluno.
 - Caso o RA não exista no dicionário, a função deve gerar uma exceção KeyError
'''
def buscar(alunos, ra):
    return alunos[ra]

alunos = {}
for i in range(3):
    try:
        ra = int(input('RA: '))
        if ra in alunos:
            raise TypeError                   # gerar uma exceção
        if ra < 1000000 or ra >= 10000000:    # verifica se tem 7 digitos
            raise ValueError                  # gerar uma exceção
        nome = input('Nome: ')
        alunos[ra] = nome
    except TypeError:
        print('RA ja esta cadastrado.')
    except ValueError:
        print('RA não está no formato correto')
print(alunos)

try:
    nome = buscar(alunos, 1234567)
    print(nome)
except KeyError:
    print("ERRO")