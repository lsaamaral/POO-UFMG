class Cliente():
    def __init__(self, nome, dias_estadia, consumo_restaurante):
        if dias_estadia < 0:
            raise ValueError("Dias de estadia não podem ser negativos.")
        if consumo_restaurante < 0:
            raise ValueError("Consumo do restaurante não pode ser negativo.")
        
        self.nome = nome
        self.dias_estadia = dias_estadia
        self.consumo_restaurante = consumo_restaurante
    def getNome(self):
        return self.nome
    def getDiasEstadia(self):
        return self.dias_estadia
    def getConsumoRestaurante(self):
        return self.consumo_restaurante
    def fornecaValorConta(self):
        custo_estadia = self.dias_estadia * 100
        custo_restaurante = self.consumo_restaurante * 50
        return custo_estadia + custo_restaurante

class Hotel():
    def __init__(self, nome_hotel):
        self.nome_hotel = nome_hotel
    def getNome(self):
        return self.nome_hotel
    def determineContaCliente(self, cliente):
        return cliente.fornecaValorConta()
    
def main():
    cliente1 = Cliente("Isa", 4, 8)
    hotel1 = Hotel("Beira Mar")
    conta1 = hotel1.determineContaCliente(cliente1)
    print(f"O cliente {cliente1.getNome()} que ficou {cliente1.getDiasEstadia()} dias no hotel {hotel1.getNome()} teve a conta de {conta1} reais, considerando {cliente1.getDiasEstadia()} dias de hospedagem e {cliente1.getConsumoRestaurante()} refeições.")
    
    try:
        clienteerro = Cliente("Fabio", -5, -9)
        contaerro = hotel1.determineContaCliente(clienteerro)
        print(f"O cliente {clienteerro.getNome()} que ficou {clienteerro.getDiasEstadia()} dias no hotel {hotel1.getNome()} teve a conta de {contaerro} reais, considerando {clienteerro.getDiasEstadia()} dias de hospedagem e {clienteerro.getConsumoRestaurante()} refeições.")
    except ValueError as e:
        print(f"Erro ao criar cliente: {e}")
main()