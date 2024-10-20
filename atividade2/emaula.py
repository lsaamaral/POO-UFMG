# class Musico():
#     def __init__(self, nome):
#         self.nome = nome
#     def tocar_instrumento(self):
#         print("Tocando instrumento")

# class Pianista(Musico):
#     def __init__(self, nome):
#         self.nome = nome
#     def tocar_instrumento(self):
#         print("Estou tocando a nona sinfonia")

# class Percussionista(Musico):
#     def __init__(self, nome):
#         self.nome = nome
#     def tocar_instrumento(self):
#         print("Tocando percussão sempre no ritmo sincronizado")


# def main():
#     pianista = Pianista("Fabio Jr")
#     print(pianista.tocar_instrumento())

# main()

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

def main():
    assalariado = Assalariado(4000)
    horista = Horista(4000)
    print(assalariado.calcular_pagamento())
    print(horista.calcular_pagamento(5))

main()