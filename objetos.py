"""
POO - Objetos

Obejtos -> São instancias das classs,ou seja, apos o mapeamentos do objeto do mundo real sua
representacao computacional. Devemos poder ciar quantos objetos forem necessarios. Podemos pensar
nos objetos/intancias de uma calsse como variaveis do tipo definido na classe


"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligado = False

    def checa_lampada(self):
        return self.lampada

    def liga_desligada(self):
        if self.__lifado:
            self.__ligado = False
        else:
            self.__ligada = True


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Usuario:
    def __inint(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

lamp1 = Lampada('Branca', '110', '6400k')

cc1 = ContaCorrente(5000, 20000)

user1 = Usuario('Ramon', 'Costa', 'ramon.fc17@gmail.com', "123456")