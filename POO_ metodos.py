"""
Poo - Metodos

- Meotods (Funcoes) -> Representam os comportamentos do obejto. Ou seja,as ações
que este objeto pode realizaar no seu sistema

Em python,dividimos os metodos, em 2 grupos: Metodos de instancia
e Metodos de Classe0

$metodos de Intancia

#O metodo dunder init __init__ e um metodo especial chamado de construtor e
sua funcao e construir o objeto a partir da classe

Obs. Todo elemento em python que inicia e finaliza com duplo underline e chamado de dunder (Double Underline)

Obs. Os metodos/funcoes em python sao chamados de metodos magicos
nao e aconselhado. Python possui varios metodos com esta fome de nomeclatura poder ser que mudemos o comportamento
dessas funcoes magicas internas da linguagem. Entao, evite ao maximo. De preferencia nunca o faça.

#Métodos são escritos em letras minusculas. Se o nome for composto, sera separado com underline
user1 = Usuario('Angelia', 'Jolie', 'angelinajolie@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())
print(user2.nome_completo())

print(f'senha User 1: {user1._Usuario__senha}') # Acesso de forma errada de uma tributo de clase


"""

class Lampada:

    def __index__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.luminosidade = luminosidade
        self.ligado = False


class ContaCorrente:

    contador  = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.saldo = saldo

        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem) ) / 100


from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    contador = 0
    @classmethod
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return  f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False





nome = input('Informe nome')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('informe senha:')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha incorreta !!!')
    exit(42)

print('Usuario Cadastrado com sucesso: ')


# Metodo de Classe



senha = input('Digite a senha de aceso: ')

if user.checa_senha(senha):
    print('Acessp permitido')
else:
    print('Acesso negado')

print(f'Senha User criptografada: {user._Usuario__senha}')#Acesso errado

