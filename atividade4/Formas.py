from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
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

class Retangulo(FormaGeometrica):
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
           
class Quadrado(FormaGeometrica):
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
           
class Triangulo(FormaGeometrica):
    def calcular_area(self):
        if len(self.lados) < 3:
           super().le_lados()
           if self.quantidade_lados != 3:
                raise ValueError("Um triângulo deve ter 3 lados")
        lado1, lado2, lado3 = self.lados
        s = (lado1+lado2+lado3)/2
        a = (s(s-lado1)(s-lado2)(s-lado3)) ** (1/2)
        return a
    
    def calcular_perimetro(self):
        if len(self.lados) < 3:
            super().le_lados()
            if self.quantidade_lados != 3:
                raise ValueError("Um triângulo deve ter 3 lados")
                
        p = self.lados[0] + self.lados[1] + self.lados[2]
        return p

    def triangulo_retangulo(self):
        if len(self.lados) < 3:
            super().le_lados()
            if self.quantidade_lados != 3:
                raise ValueError("Um triângulo deve ter 3 lados")

        a, b, c = sorted(self.lados)
        
        if abs(c**2 - (a**2 + b**2)) < 1e-5:
            print("É triângulo retângulo")
        else:
            print("Não é triângulo retângulo")
        
    
def main():
    retangulo1 = Retangulo()
    quadrado1 = Quadrado()
    triangulo1 = Triangulo()

    print(retangulo1.calcular_area())
    print(quadrado1.calcular_area())
    triangulo1.triangulo_retangulo()


main()