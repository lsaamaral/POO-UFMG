from abc import ABC, abstractmethod

class ArtistaInterface(ABC):
    @abstractmethod
    def get_nome(self) -> str:
        pass

    @abstractmethod
    def set_nome(self, nome: str) -> None:
        pass

    @abstractmethod
    def get_musicas(self) -> list:
        pass
    
    @abstractmethod
    def adicionar_musica(self, musica: str, genero: str) -> None:
        pass

