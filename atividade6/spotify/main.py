from artista import *
from playlist import *

def main():
    artista1 = Artista("Artista A")
    artista2 = Artista("Artista B")

    artista1.adicionar_musica("Roots Bloody Roots", "Metal")
    artista1.adicionar_musica("Musica1", "Jazz")
    artista2.adicionar_musica("Evil Papagali", "Metal")
    artista2.adicionar_musica("Musica2", "MPB")

    playlist = Playlist("Playlist so as melhores")

    playlist.adicionar_musica_playlist(artista1, "Roots Bloody Roots")
    playlist.adicionar_musica_playlist(artista2, "Evil Papagali")
    
    playlist.exibir_playlist()

    playlist.salvar_playlist_arquivo("playlist.txt")

main()
