from typing import List
from calendario import Calendario
from interface import DisciplinaInterface

class Disciplina(DisciplinaInterface):
    def __init__(self, nome: str, horas_por_dia: float, calendario: Calendario):
        self._nome = nome
        self._horas_por_dia = horas_por_dia
        self._calendario = calendario
    
    def calcular_horas_totais(self) -> float:
        try: 
            dias_uteis = self._calendario.calcular_dias_uteis()
            return dias_uteis * self._horas_por_dia
        except Exception as e:
            print(f"Erro: {e}")
            return 0.0