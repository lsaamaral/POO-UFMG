from abc import ABC, abstractmethod

class CalendarioInterface(ABC):
    @abstractmethod
    def calcular_dias_uteis(self) -> int:
        pass

class DisciplinaInterface(ABC):
    @abstractmethod
    def calcular_horas_totais(self) -> float:
        pass