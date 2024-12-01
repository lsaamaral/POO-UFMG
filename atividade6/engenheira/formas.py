from interface import *

class Retangulo(FormasInterface):
    def calcular_area(self):
        if len(self.lados) < 3:
            super().le_lados()
            if self.quantidade_lados != 4:
                raise ValueError("Um retângulo deve ter 4 lados")
        if self.lados[0] != self.lados[1]:
            if self.lados[0] != self.lados[2]:
                if self.lados[0] != self.lados[3]:
                    raise ValueError("O retângulo precisa ter dois lados iguais")
            return self.lados[0] * self.lados[1]
        else:
            return self.lados[0] * self.lados[2]
        
    def calcular_perimetro(self):
        if len(self.lados) < 3:
           super().le_lados()
           if self.quantidade_lados != 4:
                raise ValueError("Um retângulo deve ter 4 lados")
        if self.lados[0] != self.lados[1]:
            return 2 * (self.lados[0] + self.lados[1])
        else:
            return 2 * (self.lados[0] + self.lados[2])
           
class Quadrado(FormasInterface):
    def calcular_area(self):
        if len(self.lados) < 3:
            super().le_lados()
            if self.quantidade_lados != 4:
                raise ValueError("Um quadrado deve ter 4 lados")
        if any(lado != self.lados[0] for lado in self.lados):
            raise ValueError("Todos os lados devem ser iguais em um quadrado")
        return self.lados[0] ** 2
        
    def calcular_perimetro(self):
        if len(self.lados) < 3:
            super().le_lados()
            if self.quantidade_lados != 4:
                raise ValueError("Um quadrado deve ter 4 lados")
        if any(lado != self.lados[0] for lado in self.lados):
            raise ValueError("Todos os lados devem ser iguais em um quadrado")
        return 4 * self.lados[0]
      