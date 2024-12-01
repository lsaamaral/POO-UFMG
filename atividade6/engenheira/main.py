from formas import *
from engenheira import *

terreno_r = Retangulo()
terreno_q = Quadrado()

engenheira = Engenheira("Selma")

print("Medindo o terreno retangular: ")
engenheira.medir_area(terreno_r)
engenheira.medir_perimetro(terreno_r)

print("Medindo o terreno quadrado: ")
engenheira.medir_area(terreno_q)
engenheira.medir_perimetro(terreno_q)