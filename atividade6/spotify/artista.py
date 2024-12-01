from interfaceartista import *

class Artista(ArtistaInterface):
    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._musicas = []

    def set_nome(self, nomenovo: str) -> None:
        self._nome = nomenovo

    def get_nome(self) -> str:
        return self._nome
    
    def adicionar_musica(self, musica: str, genero: str) -> None:
        self._musicas.append({'musica': musica, 'genero': genero})

    def get_musicas(self) -> list:
        return self._musicas