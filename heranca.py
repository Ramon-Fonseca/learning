"""
POO - Herança (inheritance)

A ideia de herança e a da reaproveitar codigo. Tambem exxtender nossas classes

OBS. Com herança a partir de uma classe existente, nos extendemos outra clases
que passa a herda atributos e metodos de classes herdada.

Cliente
     - nome:
     - Sobrenome
     - cpf:
     - renda:

Funcionario
      - nome:
      - sobrenome
      - cpf
      - matricula

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome =nome

        Quando uma clase herda de outra clase, e classe herdada e conhecida por:
        - super Classe;
        - Classe mae:
        - Classe Pai;
        - Classe Base;
        - Classe Generica;

Quando uma classe herda dde outra calsse, ela e chamada:




"""
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'



class Cliente(Pessoa):
    """Cliente herda de pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Formas n'ao comuns de acessar dados da super classe
        self.__renda = renda




class Funcionario(Pessoa):
    """CLiente herda de pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Steve', 'Strange', '123.456.789-00', 5000)
funcionario = Funcionario('Peter', 'parke', '987.654.321-11', '123456')

print(cliente1.__dict__)
print(funcionario.__dict__ )




