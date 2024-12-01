from jogador import *

class EstatisticasJogadores():
    def __init__(self, jogadores):
        self.jogadores = jogadores

    def exibir_estatisticas(self):
        for jogador in self.jogadores:
            jogador.exibir_estatisticas()