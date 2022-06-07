cadastro = list()
alunos = dict()

alunos['Nome'] = str(input('Digite o nome do Aluno: '))
alunos['nota'] = float(input(('Digite a nota')))

cadastro.append(alunos.copy())
print('-='*30)
print(cadastro)

if alunos['nota'] >=  7:
