from abc import ABC, abstractmethod
from datetime import datetime

class MetodoPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass
    def salvar_pagamento(self, valor):
        pass

class CartaoCredito(MetodoPagamento):
    def __init__(self, numero_cartao, titular, validade, cvv):
        if not numero_cartao.isdigit() or len(numero_cartao) != 16:
            raise ValueError("Numero do cartao invalido, precisa ser 16 digitos.")
        if not cvv.isdigit() or len(cvv) != 3:
            raise ValueError("CVV invalido, precisa ser 3 digitos.")
        self.numero_cartao = numero_cartao
        self.titular = titular
        self.validade = validade
        self.cvv = cvv

    def processar_pagamento(self, valor):
        if valor <= 0:
            raise ValueError("O valor do pagamento deve ser positivo")
        print(f"Pagamento de R${valor:.2f} processado com sucesso pelo cartao de credito ({self.numero_cartao[-4:]})")
        self.salvar_pagamento(valor)

    def salvar_pagamento(self, valor):
        with open("atividade5/pagamentos.txt", "a") as arquivo:
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            arquivo.write(f"{data} - R${valor:.2f} - Cartao de Credito ({self.numero_cartao[-4:]})\n")


class PayPal(MetodoPagamento):
    def __init__(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Email invalido para o PayPal")
        self.email = email

    def processar_pagamento(self, valor):
        if valor <= 0:
            raise ValueError("O valor do pagamento deve ser positivo")
        print(f"Pagamento de R${valor:.2f} processado com sucesso pelo PayPal ({self.email})")
        self.salvar_pagamento(valor)

    def salvar_pagamento(self, valor):
        with open("atividade5/pagamentos.txt", "a") as arquivo:
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            arquivo.write(f"{data} - R${valor:.2f} - PayPal ({self.email})\n")


class TransferenciaBancaria(MetodoPagamento):
    def __init__(self, banco, agencia, conta):
        if not agencia.isdigit() or len(agencia) != 4:
            raise ValueError("Agencia invalida, precisa ser 4 digitos")
        if not conta.isdigit():
            raise ValueError("Numero da conta invalido")
        self.banco = banco
        self.agencia = agencia
        self.conta = conta

    def processar_pagamento(self, valor):
        if valor <= 0:
            raise ValueError("O valor do pagamento deve ser positivo")
        print(f"Pagamento de R${valor:.2f} processado com sucesso por transferencia bancaria (Banco: {self.banco}, Agencia: {self.agencia}, Conta: {self.conta})")
        self.salvar_pagamento(valor)

    def salvar_pagamento(self, valor):
        with open("pagamentos.txt", "a") as arquivo:
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            arquivo.write(f"{data} - R${valor:.2f} - Transferencia Bancaria (Banco: {self.banco}, Agencia: {self.agencia}, Conta: {self.conta})\n")

def main():
    try:
        cartao = CartaoCredito("1234567812345678", "João Silva", "12/25", "123")
        paypal = PayPal("joao.silva@example.com")
        transferencia = TransferenciaBancaria("Banco XYZ", "1234", "567890")

        cartao.processar_pagamento(150.75)
        paypal.processar_pagamento(300.00)
        transferencia.processar_pagamento(450.50)

    except ValueError as e:
        print(f"Erro ao processar pagamento: {e}")

main()
