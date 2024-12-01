from abc import ABC, abstractmethod

class EstatisticasInterface(ABC):
    @abstractmethod
    def calcular_total_pontos(self):
        pass

    @abstractmethod
    def calcular_media_pontos(self):
        pass

    @abstractmethod
    def exibir_estatisticas(self):
        pass