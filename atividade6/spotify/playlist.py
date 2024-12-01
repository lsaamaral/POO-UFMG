from artista import *
from typing import List

class Playlist:
    def __init__(self, nome_playlist: str) -> None:
        self._nome_playlist = nome_playlist
        self._musicas_na_playlist = []

    def adicionar_musica_playlist(self, artista: Artista, musica: str) -> None:
        for item in self._musicas_na_playlist:
            if item['musica'] == musica and item['artista'] == artista.get_nome():
                print(f"A música '{musica}' já foi adicionada à playlist.")
                return
        
        for musica_artista in artista.get_musicas():
            if musica_artista['musica'] == musica:
                self._musicas_na_playlist.append({
                    'artista': artista.get_nome(),
                    'musica': musica,
                    'genero': musica_artista['genero']
                })
                print(f"Musica '{musica}' adicionada na playlist '{self._nome_playlist}'")
                return

        print(f"Musica '{musica}' nao encontrada no repertório do artista {artista.get_nome()}")

    def exibir_playlist(self) -> None:
        if not self._musicas_na_playlist:
            print(f"A playlist '{self._nome_playlist}' esta vazia")
            return
        
        print(f"Playlist: {self._nome_playlist}")
        for item in self._musicas_na_playlist:
            print(f"- {item['musica']} de {item['artista']} ({item['genero']})")

    def salvar_playlist_arquivo(self, arquivo_nome: str) -> None:
        with open(arquivo_nome, 'w') as file:
            file.write(f"Playlist: {self._nome_playlist}\n")
            for item in self._musicas_na_playlist:
                file.write(f"{item['musica']} - {item['artista']} ({item['genero']})\n")
        print(f"A playlist foi salva no arquivo '{arquivo_nome}'")
