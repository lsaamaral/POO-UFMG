from jogador import *
from estatisticas import *

jogador1 = Jogador("Joao", [3, 8, 25, 26])
jogador2 = Jogador("Lucas", [4, 7, 4, 1])
jogador3 = Jogador("Fernando", [9, 2, 13, 20])

jogadores = [jogador1, jogador2, jogador3]

sistema = EstatisticasJogadores(jogadores)

sistema.exibir_estatisticas()