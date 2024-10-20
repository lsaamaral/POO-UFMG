class Carro():
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.ligado = False
        self.velocidade = 0
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O carro {self.modelo} está agora ligado.")
        else:
            print(f"O carro {self.modelo} já está ligado.")
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O carro {self.modelo} está agora desligado.")
        else:
            print(f"O carro {self.modelo} já está desligado.")
    def acelerar(self, velocidade):
        if not self.ligado:
            raise ValueError(f"O carro {self.modelo} precisa estar ligado para acelerar.")
        if velocidade < 0:
            raise ValueError("A velocidade não pode ser negativa.")
        if velocidade > 200:
            raise ValueError("A velocidade não pode passar de 200 km/h.")
        self.velocidade = velocidade
        print(f"O carro {self.modelo} acelerou para {self.velocidade} km/h.")

class Motorista():
    def __init__(self, nome):
        self.nome = nome
    def dirigir(self, carro, velocidade):
        print(f"Motorista {self.nome} dirigindo.")
        if not carro.ligado:
            carro.ligar()
        if carro.ligado:
            carro.acelerar(velocidade)
        else:
            print(f"Não é possível acelerar o carro {carro.modelo} porque ele está desligado.")

def main():
    carro1 = Carro("Fuscao", "Preto")
    carro2 = Carro("Uno Mille", "Branco")

    motorista1 = Motorista("Francisco")
    motorista2 = Motorista("Casemiro")

    try: 
        motorista1.dirigir(carro1, 120)
        motorista2.dirigir(carro2, 150)

        carro2.desligar()
        motorista2.dirigir(carro2, 80) # Não é para um carro desligado acelerar
    except ValueError as e:
        print(f"Erro: {e}")

main()