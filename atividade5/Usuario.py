from abc import ABC, abstractmethod

class Usuario(ABC):
    @abstractmethod
    def cadastrar(self):
        pass

class UsuarioComum(Usuario):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email
    
    def cadastrar(self):
        return f"{self.nome}, {self.email}"

class UsuarioAdministrador(UsuarioComum):
    def __init__(self, nome, email, nivel_acesso):
        super().__init__(nome, email)
        self.nivel_acesso = nivel_acesso

    def cadastrar(self):
        return f"{self.nome}, {self.email}, {self.nivel_acesso}"

class Sistema():
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario: Usuario):
        if any(u.email == usuario.getEmail() for u in self.usuarios):
            print(f"Usuario com email {usuario.getEmail()} ja possui cadastro")
        else:
            self.usuarios.append(usuario)
            print(f"Email {usuario.getEmail()} cadastrado")

    def exportar_usuarios(self, nome_arquivo):
        with open(nome_arquivo, "w") as arquivo:
            for usuario in self.usuarios:
                arquivo.write(usuario.cadastrar() + "\n")
        print(f"Banco de dados salvo em {nome_arquivo}")

sistema = Sistema()
usuariocomum = UsuarioComum("Joao Silva", "joao@gmail.com")
usuarioadm = UsuarioAdministrador("Ana Paula", "ana@gmail.com", "superadmin")

sistema.adicionar_usuario(usuariocomum)
sistema.adicionar_usuario(usuarioadm)
sistema.adicionar_usuario(usuariocomum)

sistema.exportar_usuarios("atividade5/usuarios.txt")
