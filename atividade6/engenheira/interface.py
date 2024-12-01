from abc import ABC, abstractmethod

class FormasInterface(ABC):
    def __init__(self):
        self.lados = []
        self.quantidade_lados = 0

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    def le_lados(self):
        while True:
            try:
                self.quantidade_lados = int(input("Digite a quantidade de lados: "))
                if self.quantidade_lados < 3:
                    raise ValueError("A quantidade de lados deve ser no mínimo 3")
                break
            except ValueError as e:
                print(e)
        
        for i in range(self.quantidade_lados):
            while True:
                try:
                    lado = float(input(f"Digite o comprimento do lado {i + 1}: "))
                    if lado <= 0:
                        raise ValueError("o valor do lado deve ser positivo")
                    self.lados.append(lado)
                    break
                except ValueError as e:
                    print(e)

    def mostra_lados(self):
        for i in range(i, self.quantidade_lados):
            print(f"Lado {i+1}: {self.lados[i]}")