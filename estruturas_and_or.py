""""
Estruturas Logicas: and (e), or (ou), not (nao), if (e)

Operadores unários:
    - not, is
Operadores Binarios
   - and, or

Para o 'and', os dois valores prescisam ser True
para o 'OR',só um dos valores prescisa ser True
"""

ativo = True
logado = False

if ativo or logado:
    print('Bem-vindo usuario')
else:
    print('Voce prescisa ativar sua conta, check seu email')
