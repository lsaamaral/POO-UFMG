class Funcionario():
    def __init__(self, salariob):
        self.salariob = salariob
    def calcular_pagamento(self):
        return self.salariob

class Assalariado(Funcionario):
    def __init__(self, salariob):
        super().__init__(salariob)

class Horista(Funcionario):
    def __init__(self, novosalario):
        super().__init__(salariob=novosalario)
    def calcular_pagamento(self, hora):
        return self.salariob * hora

def testar_funcionario():
    erros = []

    assalariado = Assalariado(4000)
    if assalariado.calcular_pagamento() != 4000:
        erros.append(f"Erro em Assalariado: Esperado 4000, mas foi retornado {assalariado.calcular_pagamento()}")

    horista = Horista(4000)
    if horista.calcular_pagamento(5) != 4000 * 5:
        erros.append(f"Erro em Horista: Esperado {4000 * 5}, mas foi retornado {horista.calcular_pagamento(5)}")

    if erros:
        for erro in erros:
            print(erro)
    else:
        print("Todos os testes passaram")

def main():
    assalariado = Assalariado(4000)
    horista = Horista(4000)
    print(assalariado.calcular_pagamento())
    print(horista.calcular_pagamento(5))

    testar_funcionario()

main()