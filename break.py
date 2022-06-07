for numero in range (1, 10):
    if numero == 6:
        break
    else:
        print(numero)
print('Sair do loop')

while True:
    comando = input('DIgite "Sair" para sair: ')
    if comando == 'sair':
        break