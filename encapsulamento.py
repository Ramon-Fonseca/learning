"""
Public, Protected, private

print(conta1.__dict__)

print(conta1.Conta.__titural)

------------------------------------------
print(conta1.__dict__)

conta1.depositar(150)

print(conta1.__dict__)


conta1.sacar(2000)

print(conta1.__dict__)
"""

class Conta:
      contador = 400
      def __init__(self, titular, saldo, limite):
          self.__numero = Conta.contador
          self.__titular = titular
          self.__saldo = saldo
          self.__limite = limite
          Conta.__contador = self.__numero


      def extrato(self):
          print(f'Saldo de {self.__saldo}, do titular {self.__titular} com limite de {self.__limite}')


      def depositar(self, valor):
          if valor > 0:
              self.__saldo += valor
          else:
              print('Valor de deposito invalido, ')



      def sacar(self, valor):
          if valor > 0 :
              if self.__saldo >= valor:
                self.__saldo -= valor
              else:
                print('Saldo insuficiente')
          else:
              print('O valor deve ser positivo')

      def trasnferir(self, valor, conta_destino):
          #1- Remover o valor da conta de origem
          self.__saldo -= valor
          self.__saldo -= 10 #taxa de transferencia, paga pelo titular

          # 2 - Adciona o valor na conta de destino
          conta_destino.__saldo += valor


#

conta1 = Conta('Wayne', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Tony', 300, 2000)
conta2.extrato()

conta2.trasnferir(100, conta1)

conta1.extrato()
conta2.extrato()





# testando

conta1 = Conta('Geek', 150.00, 1500)
conta2 = Conta('Bruce wayne', 300, 2000)