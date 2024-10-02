class Bolo():
    def __init__(self, nome, recheio, massa, cobertura):
        self.nome = nome
        self.recheio = recheio
        self.massa = massa
        self.cobertura = cobertura
    def getCobertura(self):
        return self.cobertura
    def setCobertura(self, nova_cobertura):
        self.cobertura = nova_cobertura
    
bolo1 = Bolo("Bolo Jake", "Maracuja", "Baunilha", "Chantilly Amarelo")
bolo2 = Bolo("Bolo Aveiudo", "Banana", "Aveia", "Sem cobertura")
bolo3 = Bolo("Bolo Jake", "Maracuja", "Baunilha", "Sem cobertura")

print("Coberturas: \n" + bolo1.getCobertura() + "\n" + bolo2.getCobertura() + "\n" + bolo3.getCobertura())

bolo1.setCobertura("Sem cobertura")

print("Coberturas: \n" + bolo1.getCobertura() + "\n" + bolo2.getCobertura() + "\n" + bolo3.getCobertura())

