from abc import ABC, abstractmethod

class ExtratorDados(ABC):
    @abstractmethod
    def extrair_dados(self):
        pass

class ExtratorTXT(ExtratorDados):
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
    def extrair_dados(self):
        try:
            with open(self.caminho_arquivo, "r") as arquivo:
                linhas = arquivo.readlines()
                usuarios = [linha.strip() for linha in linhas if linha.strip()]
            return usuarios
        except FileNotFoundError:
            print(f"O arquivo {self.caminho_arquivo} nao foi encontrado.")
            return []
        except Exception as e:
            print(f"Erro lendo o arquivo: {e}")
            return []

    def exibir_dados(self, usuarios):
        if not usuarios:
            print("Nenhum dado para exibir")
        else:
            print("Usuarios cadastrados:")
            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. {usuario}")

def main():
    extrator = ExtratorTXT("atividade5/banco_usuarios.txt")

    dados = extrator.extrair_dados()

    extrator.exibir_dados(dados)

main()
