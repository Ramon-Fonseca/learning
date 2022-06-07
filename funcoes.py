"""
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')



a = 5

teste(a)
print(f'A fora vale{a}')
"""
"""
def  soma(a=0 ,b=0 ,c=0 ):
    s = a + b + c
    return s


r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma = (6)

print(f'Os resultados foram {r1}, {r2} e {r3}', end='')
"""
"""
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados dão {f1}, {f2} e {f3}')
"""
"""
def eleitor(data):
    ano = date.today().year
    voto = ano - data
    if voto < 16:
        print(f' VOce tem {voto}, e não obrigado a votar')
    elif  16 <= voto < 18:
        print(f'Você tem {voto}, e voce tem voto facultativo')
    elif 18 <= voto <= 65:
        print(f'Voce tem {voto}, e é obrigado a votar')
    elif voto > 65:
        print(f'Voce tem {voto}, voce não e obrigado a votar')




from datetime import date

print('-'*30)
ano = int(input('Em que ano você nasceu?: '))

eleitor(ano)"""