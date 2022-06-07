"""
Decoradores (decorators)

O que são decorators?

- Decorators são funções:
- Decorators envolvem outras funções e aprimoram seus comportamentos
- Decoratoes tambem são exemplos de Migher Order Functions:
- Decorators tem uma sintaxe propria, usando '@' (Syntact Sugar / Açucar sintetico)

"""

# Decorators como funcoes (sintaxe nao recomendada / Se,Açucar Sintetico)
"""
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer voce')
        funcao()
        print('Tenha um ótimo dia?')
    return sendo


def saudacao():
    print('Sej ebem-vindo a Geek University')
    def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer te conhcer !!!')
        funcao()
        print('Tenha um excelente dia!')

    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é pedro')


apresentando()

|-------------------------------------------------|
| Home    | Servicos       | Produtos |           |
---------------------------------------------------
https://www.suaempresa.com.br/home
https://www.suaempresa.com.br/servico
https://www.suaempresa.com.br/produtos
https://www.suaempresa.com.br/admin

def checar_login(request):
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')
        

def home(request):
    return'pode acecssar home
    
def servicos(request):
    return 'pode acessar serviços
@checar_login
def produtos(request):
    :return 'pode acessar produtos

@checa_login
def admin(request):
     :return 'Pode acessar admin'


"""
 #Obs. não confunda decorator function, com decorator