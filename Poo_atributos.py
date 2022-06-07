"""
POO  - Atributos

Atributos ->Representam as caracteristicas do objeto. Ou seja, pelos atributos
nos conseguimos representar computacionalmente os estados de um objeto

Em Python, dividimos os atributos em 3 grpos:

    - Atributos de Instancia:
    - Atributos de CLasse:
    - Atribtos Dinámicos:

# Atributos de Instâncias: São atributos declarado dentro do metodo construtor

# Obs: Metodo construtor: É um metodo especial utilizado para a construção do objeto.
Em python por convenção , ficou estabelecido que, todo o atriibuto de uma calsse e publico.
Ou seja, pode ser acessado em todo projeto.
Caso queiramos demonstra que o atributo deve ser tratado como privadom ou seja,
que deve ser acessado/utilizado somente dentro da propria classe onde está declarado.
utiliza-se __ duplo underline no inicio do nome.

# Atributos publicos e atributos privados



user = Acesso('user@gmail', '123456')

print(user.email)
user.mostrasenha()
p1 = Produto('Playstation', 'Video Game', 4500)
p2 = Produto('Xbox s', "Video Game", 4200)

print(p1.valor) #acesso possivel, mas incorreto de uma tributo de classe
print(p2.valor)

# OBS: Nao precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print((Produto.imposto))  #Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)


"""

class Lampada:
    def __int__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False



class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limmite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha
    def mostrasenha(self):
        print(self.__senha)
    def mostraemail(self):
        print(self.email)



# O que significa atributos de isnstâncias?

#Siginifica que ao criarmos instancias/objetos dee umca classe, todas as inistâncias
#terao esses atributos


"""
user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostrasenha()
user2.mostrasenha()
"""

#Atributos de Classe

#Atributos de classe, são atributos, claro, que sao declarados diretamente na classe, ou seja
#fora do construtor. Geralmente ja inicializamos um valor, e este valor e compartilhado entre
#todas as intancias da classe, ou seja, ao inves de cada instancia da classe ter seus prorpios
#valores como e o caso dos atribuidos de instancias, cini is arributos da classe todas as intancias
#terao o mesmo valor atribuido


class Produto:
    imposto = 1.05 # 0,05% de imposto
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


#Atributos dinamicos -> Um atributo de instancia que pode ser criado em tempo de execução

#Obs: O atributo dinamico sera exclusivo da instancia que o criou

p1 = Produto('Playstation 4 ', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

p2.peso = '5Kg'

#print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, valor:{p2.valor}, Peso{p2.peso}')

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

del p2.peso

print(p1.__dict__)
print(p2.__dict__)




