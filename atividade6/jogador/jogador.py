from interface import *

class Jogador(EstatisticasInterface):
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos
        self.partidas_jogadas = len(pontos)

    def calcular_total_pontos(self):
        return sum(self.pontos)
    
    def calcular_media_pontos(self):
        if self.partidas_jogadas > 0:
            media = sum(self.pontos) / self.partidas_jogadas
        else:
            media = 0
        return media
    
    def exibir_estatisticas(self):
        total_pontos = self.calcular_total_pontos()
        media_pontos = self.calcular_media_pontos()
        print(f"O jogador {self.nome} possui o total de {total_pontos} pontos, com uma média de {media_pontos} pontos por partida")
        print(f"Quantidade de partidas jogadas: {self.partidas_jogadas}")