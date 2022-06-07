"""pessoas = {'nome': 'Gustavo', 'Sexo':'M', 'Idade':23}
print((f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')"""

"""pessoas = {'nome': 'Ramon', 'Sexo': 'M', 'Idade': 23}
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')"""

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Digite o Estado: '))
    estado['sigla'] = str(input('Digite a Sigla: '))
    brasil.append(estado.copy())

for c in brasil:
    for v in e.values():
        print(v)



