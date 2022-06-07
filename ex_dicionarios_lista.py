lista = []
cadastro = dict()

soma = idade = 0

while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Digite o nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print(('Erro!!! Digite apenas M ou F, Por favor '))
    cadastro['idade'] = int(input('Digite a idade:'))
    soma = soma + cadastro['idade']
    lista.append(cadastro.copy())
    while True:
        resposta = str(input('Quer continuar: [S/N]')).upper()[0]
        if resposta in 'SN':
            break
        print('!!Erro, Digite apenas S ou N.')
    if resposta == 'N':
        break

print('-='*30)
print(lista)
media = soma / len(lista)

print((f'Ao todo foram cadastrados, {len(lista)} pessoas'))
print(f'A media de idade e igual a {media:5.2f}')
contador = 0
for p in lista:
    if p['sexo'] == 'Ff':
        print(f'{p["nome"]}', end='')





