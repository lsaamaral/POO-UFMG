class FazBolo():
    def __init__(self, massa, recheio, cobertura, temperatura):
        self.massa = massa
        self.recheio = recheio  
        self.cobertura = cobertura
        self.temponoforno = 0 # Não foi utilizada para esse código
        self.temperatura = temperatura # Faria mais sentido esse atributo ser tipo_fogo
    def assar(self, tempo):
        if tempo < 0:
            print("O tempo para assar o bolo não pode ser negativo")
            return
        
        print(f"Você está querendo assar o bolo no fogo {self.temperatura} por {tempo} minutos.")

        if self.temperatura == "alto":
            if tempo < 10:
                print("O bolo está cru")
            elif tempo == 10:
                print("O bolo está perfeito")
            else:
                print("O bolo queimou")
        elif self.temperatura == "médio":
            if tempo < 30:
                print("O bolo está cru")
            elif tempo == 30:
                print("O bolo está perfeito")
            else:
                print("O bolo queimou")
        elif self.temperatura == "baixo":
            if tempo < 45:
                print("O bolo está cru")
            elif tempo == 45:
                print("O bolo está perfeito")
            else:
                print("O bolo queimou")
        else:
            print("O tipo de fogo é inválido, utilize 'alto', 'médio' ou 'baixo'")
    
bolo1 = FazBolo("Neutra", "Abacaxi", "Geleia de Abacaxi", "alto")
bolo2 = FazBolo("Chocolate", "Maracuja", "Chantilly Amarelo", "médio")
bolo3 = FazBolo("Baunilha", "Morango", "Chantilly Rosa", "baixo")

# Teste assando bolo fogo alto
bolo1.assar(5)
bolo1.assar(10)
bolo1.assar(20)

# Teste assando bolo fogo médio
bolo2.assar(15)
bolo2.assar(30)
bolo2.assar(40)

# Teste assando bolo fogo baixo
bolo3.assar(43)
bolo3.assar(45)
bolo3.assar(50)

# Teste valores inválidos
bolo1.assar(-10)
bolo4 = FazBolo("Red velvet", "Baunilha", "Cream Cheese", "Altíssima")
bolo4.assar(10)

