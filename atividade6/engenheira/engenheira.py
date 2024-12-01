from typing import Type
from interface import FormasInterface

class Engenheira:
    def __init__(self, nome):
        self.nome = nome

    def medir_area(self, terreno: Type[FormasInterface]):
        area = terreno.calcular_area()
        print(f"A área do terreno é: {area}")

    def medir_perimetro(self, terreno: Type[FormasInterface]):
        perimetro = terreno.calcular_perimetro()
        print(f"O perímetro do terreno é: {perimetro}")
