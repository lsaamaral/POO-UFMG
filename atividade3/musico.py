class Musico():
    def __init__(self, nome):
        self.nome = nome
    def tocar_instrumento(self):
        return "Tocando instrumento"

class Pianista(Musico):
    def __init__(self, nome):
        self.nome = nome
    def tocar_instrumento(self):
        return "Estou tocando a nona sinfonia"

class Percussionista(Musico):
    def __init__(self, nome):
        self.nome = nome
    def tocar_instrumento(self):
        return "Tocando percussão sempre no ritmo sincronizado"

def testar_classes():
    erros = []

    musico = Musico("Djavan")
    if musico.tocar_instrumento() != "Tocando instrumento":
        erros.append(f"Erro em Musico: Esperado 'Tocando instrumento', mas foi retornado '{musico.tocar_instrumento()}'")

    pianista = Pianista("Lee")
    if pianista.tocar_instrumento() != "Estou tocando a nona sinfonia":
        erros.append(f"Erro em Pianista: Esperado 'Estou tocando a nona sinfonia', mas foi retornado '{pianista.tocar_instrumento()}'")

    percussionista = Percussionista("Melly")
    if percussionista.tocar_instrumento() != "Tocando percussão sempre no ritmo sincronizado":
        erros.append(f"Erro em Percussionista: Esperado 'Tocando percussão sempre no ritmo sincronizado', mas foi retornado '{percussionista.tocar_instrumento()}'")

    if erros:
        for erro in erros:
            print(erro)
    else:
        print("Todos os testes passaram.")


def main():
    pianista = Pianista("Gabee")
    print(pianista.tocar_instrumento())

    testar_classes()

main()
