from interface import CalendarioInterface
from typing import List
from datetime import date, timedelta
import calendar

class Calendario(CalendarioInterface):
    def __init__(self, inicio: date, fim: date, feriados: list[date]):
        self._inicio = inicio
        self._fim = fim
        self._feriados = feriados

    def calcular_dias_uteis(self) -> int:
        try:
            dias_uteis = 0
            atual = self._inicio
            while atual <= self._fim:
                if atual.weekday() < 5 and atual not in self._feriados:
                    dias_uteis += 1
                atual += timedelta(days=1)
            return dias_uteis
        except Exception as e:
            print(f"Erro: {e}")
            return 0
