valores = []
valores.append(5)
valores.append(9)
valores.append(4)




#bloco recebe valores digitados e insere em uma lista
"""
for cont in range(0, 5):
    valores.append(int((input('Digire os 5 valores'))))

#nesse bloco mostra o valor e a indice

for c, v in enumerate(valores):
    print(f'no indereço {c}, encontrei o valor:{v}...')
print('Cheguei no final da Lista.')"""
"""
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

pessoas = list()
pessoas.append(dados[:])"""
"""
teste = list()
teste.append('Gustavo')
teste.append('40')
galera = list()
#Galera recebe uma copia da lista teste
galera.append(teste[:]) 
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)"""

"""
galera = [['joao', 19], ['Ana', 33], ['Joaquin', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')"""
galera= list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a idade: ')))
    galera.append(dados[:])
    dados.clear()
totmaior = 0
totmenor = 0
print('-='*30)
for p in galera:
    if p[1] <= 18:
        print(f'{p[0]} e de menor')
        totmenor = totmenor + 1
    else:
        print(f'{p[0]} e de maior ')
        totmaior = totmaior + 1
print('-='*30)
print(f'Temos {totmenor} menores de idade e {totmaior} maiores de idade')


