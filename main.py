
'''
Crie um Programa que recebe dados de um aluno com nome
e suas notas em supostos 3 trimestres de aulas,
retornando o nome do aluno e a média de suas notas.
'''


def registrar_aluno():

    # Criar o dicionário para armazernar os dados do aluno
    aluno = {}

    # Receber o nome do aluno
    aluno['nome'] = input('Digite o nome do aluno: ')

    # Receber as notas dos três trimestres
    aluno['notas'] = []
    for i in range(1, 4):
        nota = float(input(f'Digite a nota do {i}º trimestre: '))
        aluno['notas'].append(nota)
    # Calcular a média
    aluno['media'] = sum(aluno['notas']) / len(aluno['notas'])

    return aluno


def mostrar_aluno(aluno):
    print('-'*30)
    print('\nDados do aluno:')
    print(f'Nome: {aluno["nome"]}')
    print(f'Notas: {aluno["notas"]}')
    print(f'Media: {aluno["media"]:.2f}')

aluno = registrar_aluno()
mostrar_aluno(aluno)