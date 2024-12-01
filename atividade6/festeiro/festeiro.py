class Festeiro():
    def __init__(self, nome, cpf, cupomdesconto=None):
        self.nome = nome
        self.__cpf = cpf
        self._cupomdesconto = cupomdesconto

    def __verificar_idade(self):
        idade = int(input("Qual a sua idade?"))
        if idade >= 18:
            print("Ta liberado")
            self.__mostra_cpf()
        else:
            print("Voce e menor de idade malucao, nao vai beber")

    def __mostra_cpf(self):
        print(f"CPF do festeiro: {self.__cpf}")

    def pedir_bebida(self):
        bebida = input("E aí meu chapa qual vai ser a bebida?")

        if bebida.lower() in ['cerveja roxa', 'vodka camarada', 'cuba libre']:
            print(f"Voce escolheu {bebida}")
            self.__verificar_idade()
        else: 
            print(f"Voce escolheu {bebida}")

        if self._cupomdesconto:
            print("Voce possui um cupomzinho! Vai ganhar um descontao na bebida")

def main():
    festeiro1 = Festeiro("Joao", "12345678900", "DESCONTO10")
    festeiro1.pedir_bebida()

main()