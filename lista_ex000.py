pessoas = list()
dados = list()
acumulador = 0
maior = 0
menor = 0
while True:
    dados.append(str(input('Digite o Nome:')))
    dados.append((float(input('Digite o peso:'))))
    pessoas.append((dados[:]))
    dados.clear()
    acumulador = acumulador + 1
    resposta = str(input('Quer continuar ? [S/N]'))
    x = resposta.upper()
    if x == 'N':
        break
print(f'Foram contablizados {len(pessoas)}, individuos')
print(f'Os dados Salvos foram {pessoas}')
contador = 0
peso = []
while contador < len(pessoas):
    if pessoas[1] > 100:
        pessoas

